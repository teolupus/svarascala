# SvaraScala

SvaraScala is a Python library for calculating musical frequencies across both Western and Indian classical music systems. It provides tools for working with scales, notes, swaras, ragas, and analyzing harmonic relationships.

## Features

### Western Music

- Calculate frequencies for any note in equal temperament tuning
- Support for various scale types (major, minor, harmonic minor, blues, etc.)
- Solfege name calculations (do, re, mi, etc.)
- Harmonic relationship analysis between notes

### Indian Classical Music

- Implementation of the 22-shruti system based on just intonation
- Support for the seven primary swaras (Sa, Re, Ga, Ma, Pa, Dha, Ni) with variants
- Built-in support for common ragas (Yaman, Bhairav, Bhairavi, etc.)
- Frequency calculations based on traditional ratios

## Installation

```bash
pip install svarascala
```

## Usage

### Western Music Examples

```python
from svarascala import WesternMusic

# Initialize with standard A4 = 440Hz
wm = WesternMusic()

# Get the frequency of middle C
c4_freq = wm.get_frequency('C', 4)
print(f"Middle C frequency: {c4_freq:.2f} Hz")  # 261.63 Hz

# Generate a C major scale
c_major = wm.get_scale('C', 4, 'major')
for note, freq in c_major.items():
    print(f"{note}: {freq:.2f} Hz")

# Check if two notes form a harmonic interval
is_harmonic, relation = wm.are_harmonic('C', 4, 'G', 4)
print(f"C4 and G4 are harmonic: {is_harmonic}, {relation}")  # True, 3:2 ratio (1.500)

# Calculate using solfege
do_freq = wm.get_solfege_frequency('Do', 4, 'C')
sol_freq = wm.get_solfege_frequency('Sol', 4, 'C')
print(f"Do frequency: {do_freq:.2f} Hz")  # 261.63 Hz
print(f"Sol frequency: {sol_freq:.2f} Hz")  # 392.00 Hz
```

### Indian Classical Music Examples

```python
from svarascala import IndianMusic

# Initialize with Sa at 220Hz (A3)
im = IndianMusic(reference_sa=220.0)

# Get frequencies of swaras
sa_freq = im.get_swara_frequency('Sa')
ma_freq = im.get_swara_frequency('Ma', 'shuddha')
pa_freq = im.get_swara_frequency('Pa')
print(f"Sa frequency: {sa_freq:.2f} Hz")  # 220.00 Hz
print(f"Ma frequency: {ma_freq:.2f} Hz")  # 293.33 Hz
print(f"Pa frequency: {pa_freq:.2f} Hz")  # 330.00 Hz

# Calculate all notes in a raga
yaman_freqs = im.calculate_raga_frequencies('Yaman')
for swara, freq in yaman_freqs.items():
    print(f"{swara}: {freq:.2f} Hz")

# Get all shrutis
all_shrutis = im.get_all_shrutis()
for shruti, freq in all_shrutis.items():
    print(f"{shruti}: {freq:.2f} Hz")
```

## Command Line Interface

SvaraScala comes with a command-line interface for quick calculations:

```bash
# Get information about a Western note
svarascala western-note C 4

# Generate a scale
svarascala western-scale C 4 --scale-type minor

# Get information about an Indian swara
svarascala indian-swara Ga --variant shuddha --reference 220.0

# Get all notes in a raga
svarascala indian-raga Yaman --reference 220.0
```

## Cross-Cultural Music Analysis

SvaraScala enables comparison between Western and Indian music systems:

```python
from svarascala import WesternMusic, IndianMusic

# Initialize both systems
wm = WesternMusic(reference_a4=440.0)
im = IndianMusic(reference_sa=220.0)  # Sa at A3

# Compare perfect fifth in both systems
western_fifth = wm.get_frequency('C', 4) / wm.get_frequency('G', 4)
indian_fifth = im.get_swara_frequency('Sa') / im.get_swara_frequency('Pa')

print(f"Perfect fifth ratio (Western): {western_fifth:.4f}")
print(f"Perfect fifth ratio (Indian): {indian_fifth:.4f}")
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.