# SvaraScala

SvaraScala is a Python library for calculating musical frequencies across both Western and Indian classical music systems. It provides tools for working with scales, notes, swaras, ragas, and analyzing harmonic relationships.

## Features

### Western Music

- Calculate frequencies for any note in equal temperament tuning
- Support for various scale types (major, minor, harmonic minor, blues, etc.)
- Solfege name calculations (do, re, mi, etc.)
- Harmonic relationship analysis between notes
- Camelot Wheel notation for harmonic mixing (used by DJs)

### Indian Classical Music

- Implementation of the 22-shruti system based on just intonation
- Support for the seven primary swaras (Sa, Re, Ga, Ma, Pa, Dha, Ni) with variants
- Built-in support for common ragas (Yaman, Bhairav, Bhairavi, etc.)
- Frequency calculations based on traditional ratios

## Installation

```bash
pip install svarascala
```

## Usage Examples

### Western Music

```python
from svarascala import WesternMusic

# Initialize with standard A4 = 440Hz
wm = WesternMusic()

# Get frequency of middle C
c4_freq = wm.get_frequency('C', 4)
print(f"C4 frequency: {c4_freq:.2f} Hz")  # 261.63 Hz

# Get C major scale
c_major = wm.get_scale('C', 4, 'major')
print("C major scale frequencies:")
for note, freq in c_major.items():
    print(f"{note}: {freq:.2f} Hz")

# Check if two notes are harmonic
is_harmonic, relation = wm.are_harmonic('C', 4, 'G', 4)
print(f"C4 and G4 are harmonic: {is_harmonic}, {relation}")
```

### Camelot Wheel for Harmonic Mixing

```python
from svarascala import WesternMusic

wm = WesternMusic()

# Get Camelot notation for a key
camelot = wm.get_camelot_notation('C', 'major')
print(f"C major in Camelot notation: {camelot}")  # 5B

# Get key from Camelot notation
key, scale_type = wm.get_key_from_camelot('5B')
print(f"5B in musical notation: {key} {scale_type}")  # C major

# Find compatible keys for harmonic mixing
compatible = wm.get_compatible_keys('5B')
print("Keys compatible with C major (5B):")
for camelot_code, key_name in compatible.items():
    print(f"  {camelot_code}: {key_name}")

# Get scale with Camelot information
scale_info = wm.get_scale_with_camelot('C', 4, 'major')
print(f"C major is {scale_info['camelot_notation']} in the Camelot Wheel")
print("Compatible keys for harmonic mixing:")
for camelot, key in scale_info['compatible_keys'].items():
    print(f"  {camelot}: {key}")
```

### Indian Classical Music

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

### Command Line Interface

```bash
# Get information about a Western note
python -m svarascala western-note C 4

# Get information about a Western scale
python -m svarascala western-scale C 4 --scale-type major

# Get information about an Indian swara
python -m svarascala indian-swara Sa

# Get information about an Indian raga
python -m svarascala indian-raga Yaman
```

### Output "examples/westernindianbridge.py"
```
============================================================
             SvaraScala Music Scale Comparison              
============================================================

============================================================
                   EXAMPLE 1: RAGA YAMAN                    
============================================================
Raga Yaman is one of the fundamental ragas in Hindustani classical music.
It corresponds roughly to the Lydian mode in Western music.

Indian Classical: Raga Yaman (Sa = 220 Hz)
----------------------------------------
Sa shuddha      220.00 Hz
Re shuddha      247.50 Hz
Ga shuddha      275.00 Hz
Ma tivra        313.24 Hz
Pa shuddha      330.00 Hz
Dha shuddha     366.67 Hz
Ni shuddha      412.50 Hz

Western Equivalent: F Lydian Scale (A4 = 440 Hz)
----------------------------------------
F4         349.23 Hz
G4         392.00 Hz
A4         440.00 Hz
A#4        466.16 Hz
C5         523.25 Hz
D5         587.33 Hz
E5         659.26 Hz
B4         493.88 Hz

============================================================
                  EXAMPLE 2: RAGA BHAIRAV                   
============================================================
Raga Bhairav is one of the oldest ragas in Hindustani classical music,
often performed in the early morning. It has a distinctive signature with
komal (flat) Re and Dha.

Indian Classical: Raga Bhairav (Sa = 220 Hz)
----------------------------------------
Sa shuddha      220.00 Hz
Re komal        234.67 Hz
Ga shuddha      275.00 Hz
Ma shuddha      293.33 Hz
Pa shuddha      330.00 Hz
Dha komal       352.00 Hz
Ni shuddha      412.50 Hz

Western Approximation: C Double Harmonic Scale (A4 = 440 Hz)
----------------------------------------
C4         261.63 Hz
Db4        277.18 Hz
E4         329.63 Hz
F4         349.23 Hz
G4         392.00 Hz
Ab4        415.30 Hz
B4         493.88 Hz
C5         523.25 Hz

============================================================
              EXAMPLE 3: WESTERN C MAJOR SCALE              
============================================================
The C Major scale is the most fundamental scale in Western music,
using all white keys on the piano with no sharps or flats.

Western: C Major Scale (A4 = 440 Hz)
----------------------------------------
C4         261.63 Hz
D4         293.66 Hz
E4         329.63 Hz
F4         349.23 Hz
G4         392.00 Hz
A4         440.00 Hz
B4         493.88 Hz

Indian Equivalent: Bilawal Thaat (Sa = 220 Hz)
----------------------------------------
Sa shuddha 220.00 Hz
Re shuddha 247.50 Hz
Ga shuddha 275.00 Hz
Ma shuddha 293.33 Hz
Pa shuddha 330.00 Hz
Dha shuddha 366.67 Hz
Ni shuddha 412.50 Hz
Sa' shuddha 440.00 Hz

============================================================
           EXAMPLE 4: WESTERN A MINOR BLUES SCALE           
============================================================
The Blues scale is characteristic of blues, jazz, and rock music.
It introduces 'blue notes' that give the scale its distinctive sound.

Western: A Minor Blues Scale (A4 = 440 Hz)
----------------------------------------
A4         440.00 Hz
C5         523.25 Hz
D5         587.33 Hz
D#5        622.25 Hz
E5         659.26 Hz
G5         783.99 Hz

Indian Approximation (using komal & tivra swaras)
----------------------------------------
Sa shuddha 440.00 Hz
Ga komal   521.48 Hz
Ma shuddha 586.67 Hz
Ma tivra   626.48 Hz
Pa shuddha 660.00 Hz
Ni komal   782.22 Hz

============================================================
              HARMONIC ANALYSIS ACROSS SYSTEMS              
============================================================
Perfect fifth ratio (Western): 0.6674
Perfect fifth ratio (Indian): 0.6667
Difference: 0.000753

Major third ratio (Western): 0.7937
Major third ratio (Indian): 0.8000
Difference: 0.006299

Note: Western equal temperament slightly adjusts pure ratios for modulation,
while Indian classical music maintains pure harmonic ratios.
```

### Output "examples/camelot.py"
```
------------------------------------------------------------
 CONVERTING BETWEEN MUSICAL KEYS AND CAMELOT NOTATION
------------------------------------------------------------
Key             Camelot   
--------------- ----------
C major     5B
A minor     5A
G major     6B
F major     4B
D minor     4A
Eb major     2B


Camelot    Key            
---------- ---------------
5B         C major
5A         A minor
6B         G major
4B         F major
4A         D minor
3B         Bb major

------------------------------------------------------------
 FINDING COMPATIBLE KEYS FOR HARMONIC MIXING
------------------------------------------------------------
Finding compatible keys for C major (5B):

Compatible keys based on Camelot Wheel:
Camelot    Key             Relationship
---------- --------------- ------------------------------
5A         Am              Relative minor
4B         F               Perfect 5th down
6B         G               Perfect 5th up
6A         Em              Diagonal movement

------------------------------------------------------------
 SCALE WITH CAMELOT INFORMATION
------------------------------------------------------------
Scale: C major, Octave: 4
Camelot notation: 5B

Scale frequencies:
Note       Frequency (Hz)
---------- ---------------
C4         261.63
D4         293.66
E4         329.63
F4         349.23
G4         392.00
A4         440.00
B4         493.88

Compatible keys for harmonic mixing:
  5A: Am
  4B: F
  6B: G
  6A: Em

------------------------------------------------------------
 DJ TRANSITION EXAMPLES
------------------------------------------------------------
Example transitions from a track in C major (5B):
→ Am (5A): Energy reduction (same root note, switch to minor)
→ G (6B): Energy boost (move clockwise, stay in major)
→ F (4B): Energy reduction (move counter-clockwise, stay in major)
→ Em (6A): Dramatic change (diagonal movement)
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.