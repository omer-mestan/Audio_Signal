import numpy as np
from scipy.io import wavfile
import matplotlib
matplotlib.use('TkAgg')  # Interactive backend (можете да смените на 'Agg' за запис на файлове)
import matplotlib.pyplot as plt

sampling_rate = 44100

def generate_sine_wave(frequency, duration, amplitude):
    num_samples = int(sampling_rate * duration)
    time = np.linspace(0, duration, num_samples, endpoint=False)
    audio_signal = amplitude * np.sin(2 * np.pi * frequency * time)
    print(audio_signal)
    return audio_signal

def generate_rectangular_wave(frequency, duration, amplitude):
    num_samples = int(sampling_rate * duration)
    time = np.linspace(0, duration, num_samples, endpoint=False)
    audio_signal = amplitude * np.sign(np.sin(2 * np.pi * frequency * time))
    return audio_signal

def generate_asymetric_triangular_wave(frequency, duration, amplitude):
    num_samples = int(sampling_rate * duration)
    time = np.linspace(0, duration, num_samples, endpoint=False)
    period = 1 / frequency
    audio_signal = amplitude * ((2 / period)*(time%period) - 1)
    return audio_signal

def generate_symetric_triangular_wave(frequency, duration, amplitude):
    num_samples = int(sampling_rate * duration)
    time = np.linspace(0, duration, num_samples, endpoint=False)
    period = 1 / frequency
    audio_signal = 2*amplitude * (1 - 2/period*np.abs(time%period - period/2)) - 1
    return audio_signal

def visualize_signal(audio_signal, duration, title="Audio signal"):
    time = np.linspace(0, duration, len(audio_signal), endpoint=False)
    plt.figure(figsize=(10, 4))
    plt.plot(time, audio_signal)
    plt.title(title)
    plt.xlabel("Time (s)")
    plt.ylabel("Amplitude")
    plt.grid()
    plt.show()

def plot_positive_spectrum(signal, title="Signal Spectrum (Positive Frequencies Only)"):
    signal_fft = np.fft.fft(signal)
    frequencies = np.fft.fftfreq(len(signal), 1 / sampling_rate)
    positive_frequencies = frequencies[:len(frequencies)//2]
    positive_signal_fft = 2.0 / len(signal) * np.abs(signal_fft[:len(signal)//2])

    plt.figure(figsize=(10, 4))
    plt.plot(positive_frequencies, positive_signal_fft)
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Amplitude")
    plt.title(title)
    plt.grid(True)
    plt.show()

def save_signal_to_wav(filename, signal):
    max_amplitude = np.max(np.abs(signal))
    normalized_signal = (signal / max_amplitude * 32767).astype(np.int16)
    wavfile.write(filename, sampling_rate, normalized_signal)

def main():
    last_digit = 4  # Replace with the last digit of your faculty number
    frequency = 400 + last_digit * 10
    duration = 1  # seconds
    amplitude = 1.0

    # Generate and process sine wave
    sine_wave = generate_sine_wave(frequency, duration, amplitude)
    visualize_signal(sine_wave, duration, "Sine Wave")
    plot_positive_spectrum(sine_wave, "Sine Wave Spectrum")
    save_signal_to_wav("sine_wave.wav", sine_wave)

    # Generate and process rectangular wave
    rectangular_wave = generate_rectangular_wave(frequency, duration, amplitude)
    visualize_signal(rectangular_wave, duration, "Rectangular Wave")
    plot_positive_spectrum(rectangular_wave, "Rectangular Wave Spectrum")
    save_signal_to_wav("rectangular_wave.wav", rectangular_wave)

    # Generate and process asymmetric triangular wave
    asymmetric_triangle_wave = generate_asymetric_triangular_wave(frequency, duration, amplitude)
    visualize_signal(asymmetric_triangle_wave, duration, "Asymmetric Triangular Wave")
    plot_positive_spectrum(asymmetric_triangle_wave, "Asymmetric Triangular Wave Spectrum")
    save_signal_to_wav("asymmetric_triangle_wave.wav", asymmetric_triangle_wave)

    # Generate and process symmetric triangular wave
    symmetric_triangle_wave = generate_symetric_triangular_wave(frequency, duration, amplitude)
    visualize_signal(symmetric_triangle_wave, duration, "Symmetric Triangular Wave")
    plot_positive_spectrum(symmetric_triangle_wave, "Symmetric Triangular Wave Spectrum")
    save_signal_to_wav("symmetric_triangle_wave.wav", symmetric_triangle_wave)

if __name__ == "__main__":

    main()