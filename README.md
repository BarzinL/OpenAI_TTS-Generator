# Text-to-Speech and Audio Concatenation Tool

This project provides a set of Python scripts for converting text to speech using OpenAI's API and concatenating multiple MP3 files into a single audio file using `ffmpeg`.

Intended use case is to paste your written material into the input.txt file or to generate an input.txt file within the same directory as the code files and run the `main.py` script. The script is written in such a way that it will automatically chunk your pasted text by complete sentences so as to not run over the 4096 input token limit - this will create multiple MP3 files which are then joined together using FFMPEG, and this should create a seamless-sounding narrative reading of your text.

The default voice model chosen is `fable`, but you can change this to your voice model of choice by modifying the `voice` variable inside the `convert_text_to_speech` function.

## Features

- **Text-to-Speech Conversion**: Uses OpenAI's TTS model to convert text files into speech and save the output as MP3 files.
- **Audio File Concatenation**: Combines multiple MP3 files into a single output file using `ffmpeg`.

## Prerequisites

Before running the scripts, make sure you have the following installed:

- Python 3.x
- `ffmpeg` (for audio concatenation)
- OpenAI API key (for text-to-speech conversion)

### Python Dependencies

Install the required Python libraries by running:

```bash
pip install openai toml
```

## How to Use

### Text-to-Speech Conversion (`main.py`)

1. Replace `'your-api-key'` in the `settings.toml` file with your actual OpenAI API key.
2. If desired, change the `voice` variable form `fable` to your desired [voice model](https://platform.openai.com/docs/guides/text-to-speech/voice-options) within the `convert_text_to_speech` function.
3. Place your text file in the same directory or provide the correct path to the `input.txt` file.
4. Run the script to generate MP3 files for each chunk of the text:

```bash
python main.py
```

- The generated MP3 files will be saved as `output_part_N.mp3` and automatically concatenated into a `final_output.mp3` file.

### Audio Concatenation (`concatenate.py`)

**Please note: the `main.py` script will automatically invoke the audio concatenation function.**

However, if you wish to call this separately if you have multiple MP3 files (e.g., `output_part_1.mp3`, `output_part_2.mp3`, etc.), you can concatenate them into a single MP3 file:

```bash
python concatenate.py
```

- The final concatenated MP3 file will be saved as `final_output.mp3`.

## License

This project is licensed under the **Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0)**.

You are free to:
- Share and adapt the material for **non-commercial** purposes, as long as you give appropriate credit.
- If you adapt or modify the material, you must **distribute your contributions under the same license** (CC BY-NC-SA 4.0).

**No commercial use** of this software is permitted without permission from the author. For commercial inquiries, please contact [the author](mailto:barzin@duck.com).

For more details, see the [LICENSE](LICENSE) file.
