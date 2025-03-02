#!/usr/bin/env python3
"""
Example of using Camelot Wheel functions in SvaraScala.

This script demonstrates how to use the Camelot Wheel notation functions
that have been added to the WesternMusic class in the SvaraScala library.
"""

from svarascala import WesternMusic


def print_section(title):
    """Print a section header."""
    print(f"\n{'-' * 60}")
    print(f" {title}")
    print(f"{'-' * 60}")


def main():
    # Initialize the WesternMusic class
    wm = WesternMusic()
    
    print_section("CONVERTING BETWEEN MUSICAL KEYS AND CAMELOT NOTATION")
    
    # Example keys and their Camelot notations
    example_keys = [
        ('C', 'major'),
        ('A', 'minor'),
        ('G', 'major'),
        ('F', 'major'),
        ('D', 'minor'),
        ('Eb', 'major')
    ]
    
    # Get and display Camelot notation for each key
    print(f"{'Key':<15} {'Camelot':<10}")
    print(f"{'-'*15} {'-'*10}")
    for key, scale_type in example_keys:
        camelot = wm.get_camelot_notation(key, scale_type)
        print(f"{key} {scale_type:<9} {camelot}")
    
    print("\n")
    
    # Example Camelot notations
    example_camelot = ['5B', '5A', '6B', '4B', '4A', '3B']
    
    # Get and display musical key for each Camelot notation
    print(f"{'Camelot':<10} {'Key':<15}")
    print(f"{'-'*10} {'-'*15}")
    for camelot in example_camelot:
        key, scale_type = wm.get_key_from_camelot(camelot)
        print(f"{camelot:<10} {key} {scale_type}")
    
    print_section("FINDING COMPATIBLE KEYS FOR HARMONIC MIXING")
    
    # Example key for demonstrating compatible keys
    example_key = 'C'
    example_scale = 'major'
    example_camelot = wm.get_camelot_notation(example_key, example_scale)
    
    print(f"Finding compatible keys for {example_key} {example_scale} ({example_camelot}):")
    print("\nCompatible keys based on Camelot Wheel:")
    print(f"{'Camelot':<10} {'Key':<15} {'Relationship'}")
    print(f"{'-'*10} {'-'*15} {'-'*30}")
    
    compatible = wm.get_compatible_keys(example_camelot)
    
    # Add relationship descriptions
    relationships = {
        f"{int(example_camelot[:-1])}A": "Relative minor",
        f"{(int(example_camelot[:-1]) + 1) % 12 or 12}{example_camelot[-1]}": "Perfect 5th up",
        f"{(int(example_camelot[:-1]) - 1) % 12 or 12}{example_camelot[-1]}": "Perfect 5th down",
        f"{(int(example_camelot[:-1]) + 1) % 12 or 12}{'A' if example_camelot[-1] == 'B' else 'B'}": "Diagonal movement"
    }
    
    for camelot, key in compatible.items():
        relationship = relationships.get(camelot, "Other")
        print(f"{camelot:<10} {key:<15} {relationship}")
    
    print_section("SCALE WITH CAMELOT INFORMATION")
    
    # Get scale with Camelot information
    scale_info = wm.get_scale_with_camelot(example_key, 4, example_scale)
    
    print(f"Scale: {example_key} {example_scale}, Octave: 4")
    print(f"Camelot notation: {scale_info['camelot_notation']}")
    
    print("\nScale frequencies:")
    print(f"{'Note':<10} {'Frequency (Hz)'}")
    print(f"{'-'*10} {'-'*15}")
    for note, freq in scale_info['frequencies'].items():
        print(f"{note:<10} {freq:.2f}")
    
    print("\nCompatible keys for harmonic mixing:")
    for camelot, key in scale_info['compatible_keys'].items():
        print(f"  {camelot}: {key}")
    
    print_section("DJ TRANSITION EXAMPLES")
    
    # Show practical example for DJ transitions
    print("Example transitions from a track in C major (5B):")
    
    transitions = [
        ("5A", "Energy reduction (same root note, switch to minor)"),
        ("6B", "Energy boost (move clockwise, stay in major)"),
        ("4B", "Energy reduction (move counter-clockwise, stay in major)"),
        ("6A", "Dramatic change (diagonal movement)")
    ]
    
    for camelot, description in transitions:
        key, scale = wm.get_key_from_camelot(camelot)
        key_str = f"{key}{'m' if scale == 'minor' else ''}"
        print(f"→ {key_str} ({camelot}): {description}")


if __name__ == "__main__":
    main()