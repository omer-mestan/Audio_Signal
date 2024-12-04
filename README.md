# Audio Signal Synthesis and Music Generator

This project demonstrates the generation and visualization of various audio signal waveforms and the creation of a simple musical composition. The project was developed as part of a laboratory exercise at the Technical University.

## Features

### Audio Signal Synthesis
- **Supported Signal Types**:
  - Sine wave
  - Rectangular wave
  - Asymmetric triangular wave
  - Symmetric triangular wave
- **Visualizations**:
  - Time-domain signal plots
  - Frequency spectra
- **Output**:
  - Signals are saved as `.wav` files.

### Music Generator
- Generate a sequence of notes using sine waves.
- Save the musical composition as a `.wav` file.
- Includes an example melody ("Für Elise" by Beethoven).

## Installation

### Clone the Repository
1. Clone the repository:
   ```bash
   git clone https://github.com/omer-mestan/Audio_Signal.git
   cd Audio_Signal

Usage
Run Audio Signal Synthesis Program
bash
Копиране на код
python audio_signal_synthesis_template.py
Outputs:

.wav files for each waveform type (e.g., sine_wave.wav).
Visualizations of the signals in both time and frequency domains.
Run Music Generator Program
bash
Копиране на код
python music_generator.py
Output:

composed_music.wav: A musical composition generated using sine wave signals.
Example Output Files
Generated files:

sine_wave.wav
rectangular_wave.wav
asymmetric_triangle_wave.wav
symmetric_triangle_wave.wav
composed_music.wav
Project Structure
plaintext
Копиране на код
Audio_Signal/
├── audio_signal_synthesis_template.py   # Audio signal synthesis and visualization
├── music_generator.py                   # Music generator script
├── venv/                                # Optional Python virtual environment
├── requirements.txt                     # Project dependencies
└── README.md                            # Project documentation
Dependencies
Python: Version 3.8 or higher
Libraries:
numpy: For numerical computations
scipy: For signal processing
matplotlib: For visualizations
Future Enhancements
Add support for custom waveforms and user-defined signal parameters.
Extend the music generator to include multiple instruments and wave types.
Implement a graphical user interface (GUI) for easier interaction.
Include real-time audio playback during signal generation.
License
Licensed under the MIT License. See the LICENSE file for details.

Disclaimer
This project was developed as part of a laboratory exercise at the Technical University. It was created solely for educational purposes and does not represent original research or innovation.

