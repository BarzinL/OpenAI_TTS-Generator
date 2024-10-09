import os
import subprocess
import re
from pathlib import Path
import openai

# Replace 'your-api-key' with your actual OpenAI API key
openai.api_key = "your-api-key"

def split_text_into_chunks(text, max_length=4096):
    """
    Split the text into chunks under the max_length, ensuring that we split at sentence boundaries
    or at paragraph breaks to make the chunks sound more natural.
    """
    # Split text into sentences using regular expressions to capture punctuation
    sentences = re.split(r'(?<=[.!?]) +', text)

    chunks = []
    current_chunk = ""

    for sentence in sentences:
        # If adding this sentence to the current chunk doesn't exceed the max_length, add it
        if len(current_chunk) + len(sentence) + 1 <= max_length:
            current_chunk += sentence + " "
        else:
            # If it does exceed the max length, add the current chunk to the chunks list and start a new chunk
            chunks.append(current_chunk.strip())
            current_chunk = sentence + " "

    # Don't forget to add the last chunk
    if current_chunk:
        chunks.append(current_chunk.strip())

    return chunks

def convert_text_to_speech(file_path, output_file_prefix):
    try:
        # Read the content of the .txt file with UTF-8 encoding
        with open(file_path, 'r', encoding='utf-8') as file:
            text_content = file.read()

        # Split the text into chunks (each under 4096 characters)
        chunks = split_text_into_chunks(text_content)

        # List to keep track of all the output MP3 part files
        part_files = []

        # Process each chunk and save as individual MP3 files
        for i, chunk in enumerate(chunks):
            response = openai.audio.speech.create(
                model="tts-1",  # Standard TTS model
                voice="fable",  # Choose a voice (you can change this)
                input=chunk
            )

            # Save the audio file by streaming the content from the response
            chunk_output_file = f"{output_file_prefix}_part_{i + 1}.mp3"
            with open(chunk_output_file, 'wb') as output:
                for chunk_data in response.iter_bytes():  # Proper way to stream the audio data
                    output.write(chunk_data)

            print(f"MP3 chunk saved as {chunk_output_file}")
            part_files.append(chunk_output_file)  # Add to list of part files

        # Return the list of generated part files
        return part_files

    except Exception as e:
        print(f"An error occurred: {e}")

def concatenate_audio_files(part_files, output_file):
    """Concatenate MP3 files using ffmpeg."""
    try:
        # Create a temporary file to list the input MP3 files
        with open("file_list.txt", "w") as file_list:
            for part_file in part_files:
                file_list.write(f"file '{part_file}'\n")
        
        # Use ffmpeg to concatenate the audio files
        ffmpeg_command = ['ffmpeg', '-f', 'concat', '-safe', '0', '-i', 'file_list.txt', '-c', 'copy', output_file]
        subprocess.run(ffmpeg_command, check=True)
        print(f"Final MP3 file saved as {output_file}")

        # Clean up the temporary file list
        os.remove("file_list.txt")

    except Exception as e:
        print(f"An error occurred during concatenation: {e}")

if __name__ == "__main__":
    # Path to the input .txt file containing plaintext
    input_file = "input.txt"  # Change this to your input file path
    # Prefix for the output MP3 files (they will be numbered)
    output_file_prefix = "output"  # Change this to your desired prefix for output files
    # Final output MP3 file name
    final_output_file = "final_output.mp3"

    # Convert text to speech, get a list of the generated part files
    print("Initiating text-to-speech conversion process.")
    part_files = convert_text_to_speech(input_file, output_file_prefix)

    # If there are multiple part files, concatenate them
    if part_files and len(part_files) > 1:
        concatenate_audio_files(part_files, final_output_file)
    else:
        print("No need for concatenation, only one part was generated.")
