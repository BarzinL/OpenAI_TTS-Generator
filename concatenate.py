import os
import subprocess
import glob

def concatenate_audio_files(directory, output_file):
    """Concatenate MP3 files using ffmpeg."""
    try:
        # Find all the 'output_part_N.mp3' files in the directory, sorted in order
        part_files = sorted(glob.glob(os.path.join(directory, "output_part_*.mp3")))

        if not part_files:
            print("No 'output_part_N.mp3' files found in the directory.")
            return

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
    # Directory containing the part files
    directory = "."  # Change this if your files are in a different directory

    # Name of the final output file
    final_output_file = "final_output.mp3"

    # Call the function to concatenate the part files into one final MP3
    concatenate_audio_files(directory, final_output_file)
