# Text-to-Speech and Audio Concatenation Tool

This project provides a set of Python scripts for converting text to speech using OpenAI's API and concatenating multiple MP3 files into a single audio file using `ffmpeg`.

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
pip install openai
```

## How to Use

### Text-to-Speech Conversion (`main.py`)

1. Replace `'your-api-key'` in the script with your actual OpenAI API key.
2. Place your text file in the same directory or provide the correct path to the `input.txt` file.
3. Run the script to generate MP3 files for each chunk of the text:

```bash
python main.py
```

- The generated MP3 files will be saved as `output_part_N.mp3`.

### Audio Concatenation (`concatenate.py`)

If you have multiple MP3 files (e.g., `output_part_1.mp3`, `output_part_2.mp3`, etc.), you can concatenate them into a single MP3 file:

```bash
python concatenate.py
```

- The final concatenated MP3 file will be saved as `final_output.mp3`.

## License

This project is licensed under the **Creative Commons Attribution-NonCommercial 4.0 International (CC BY-NC 4.0)**.

You are free to:
- Share and adapt the material for **non-commercial** purposes, as long as you give appropriate credit.

**No commercial use** of this software is permitted without permission from the author. For commercial inquiries, please contact [the author](mailto:barzin@duck.com).

For more details, see the [LICENSE](LICENSE) file.
