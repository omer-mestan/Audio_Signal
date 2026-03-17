# Audio Signal Synthesis and Music Composition

This repository focuses on the generation, visualization, and export of basic audio waveforms using Python. It also includes a simple music composition exercise based on sine-wave note generation.

The project was created in an educational context and is useful as a portfolio example because it combines mathematics, signal processing, waveform visualization, and audio file generation in one place.

## Project Overview

The repository is centered around two related tasks:

- synthesizing basic waveform signals
- generating a simple musical composition from individual notes

The work demonstrates how digital audio signals can be:

- generated mathematically
- visualized in the time domain
- analyzed in the frequency domain
- exported as `.wav` audio files

## Included Waveforms

The signal synthesis part of the project is designed around several common waveform types:

- sine wave
- rectangular wave
- asymmetric triangular wave
- symmetric triangular wave

Example output files already included in the repository:

- `sine_wave.wav`
- `rectangular_wave.wav`
- `asymmetric_triangle_wave.wav`
- `symmetric_triangle_wave.wav`

## Music Composition Part

The repository also includes a separate music-related exercise where notes are generated as sine waves and combined into a simple melody.

This demonstrates:

- note-based audio generation
- combining multiple generated tones into one composition
- exporting the final composition as a `.wav` file

The current template uses a short excerpt inspired by *Fur Elise* as an example note sequence.

## Repository Structure

Main files:

- `audio_signal_synthesis_template.py` - waveform generation, visualization, spectrum plotting, and WAV export
- `music_composition_template.py` - note-based music generation template
- `sine_wave.wav` - generated sine waveform example
- `rectangular_wave.wav` - generated rectangular waveform example
- `asymmetric_triangle_wave.wav` - generated asymmetric triangular waveform example
- `symmetric_triangle_wave.wav` - generated symmetric triangular waveform example

## Technologies Used

- Python
- NumPy
- SciPy
- Matplotlib

## Educational Focus

This project is especially useful for learning and demonstrating:

- basic digital signal synthesis
- waveform generation through mathematical formulas
- audio visualization
- Fourier transform / spectrum inspection
- WAV file creation in Python
- combining programming with audio and signal-processing concepts

## Important Note About The Code

The Python files in this repository are template-based educational exercises. Some sections are intentionally left incomplete and are meant to be filled in as part of the laboratory work.

That means the repository currently represents:

- the structure of the lab tasks
- example output files
- the core educational direction of the project

rather than a fully polished production-style audio library.

## How To Run

Create and activate a virtual environment if you want:

Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

macOS / Linux:

```bash
python -m venv venv
source venv/bin/activate
```

Install the required libraries:

```bash
pip install numpy scipy matplotlib
```

Then run one of the scripts:

```bash
python audio_signal_synthesis_template.py
```

or

```bash
python music_composition_template.py
```

## Expected Outputs

Depending on the completed implementation, the project can produce:

- waveform plots in the time domain
- frequency spectrum plots
- generated `.wav` files for the different signal types
- a generated music composition file

## Why This Project Matters

This repository is valuable because it shows a different side of programming compared to standard web or CRUD projects. It demonstrates work with:

- mathematical modeling
- signal processing concepts
- audio synthesis
- scientific and engineering-oriented Python programming

For a student portfolio, that helps show broader technical interest and the ability to work on projects outside traditional business applications.

## Possible Future Improvements

Some useful directions for improving this project would be:

- completing all template sections
- adding command-line parameters for waveform configuration
- generating more waveform types
- adding waveform comparison charts
- exporting spectrograms
- adding playback support
- building a small GUI for signal generation

## Author

**Yumer Mestan**  
GitHub: [omer-mestan](https://github.com/omer-mestan)
