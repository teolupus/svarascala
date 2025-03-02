#!/usr/bin/env python3
"""
Example of using Western Modes functionality in SvaraScala.

This script demonstrates how to use the WesternModes class in the SvaraScala
library to explore the emotional qualities, frequency calculations, and
harmonic relationships of Western modal music.

"Dorian, backward looked to Greece
Phrygian, passion did release
Lydian, raise your glass in cheer
Mixolydian, the bard is here
Aeolian sighs with gentle breeze
Locrian breaks with dissonant keys
While Ionian, the major scale
In modern music does prevail."
— Anonymous
"""

from svarascala import WesternModes, WesternMusic, NavarasaMap


def print_section(title):
    """Print a section header."""
    print(f"\n{'-' * 70}")
    print(f" {title}")
    print(f"{'-' * 70}")


def format_freq(freq):
    """Format frequency to 2 decimal places."""
    return f"{freq:.2f} Hz"


def main():
    # Initialize the WesternModes class (with standard A4 = 440Hz tuning)
    wm = WesternModes()
    
    print_section("WESTERN MODES AND THEIR EMOTIONAL CHARACTERISTICS")
    
    print("The seven diatonic modes and their emotional associations:")
    print(f"\n{'Mode':<12} {'Primary Emotion':<15} {'Character':<30} {'Energy':<10}")
    print(f"{'-'*12} {'-'*15} {'-'*30} {'-'*10}")
    
    for mode, info in wm.modal_emotions.items():
        print(f"{mode:<12} {info['primary']:<15} {info['character']:<30} {info['energy_level']}/10")
    
    print_section("MODE FREQUENCIES DEMONSTRATION: DORIAN MODE")
    
    # Let's use D Dorian as our example (traditional Dorian starting note)
    mode_name = "Dorian"
    root_note = "D"
    octave = 4
    
    # Get mode frequencies
    dorian_freqs = wm.get_mode_frequencies(mode_name, root_note, octave)
    
    # Get mode info
    mode_info = wm.get_mode_info(mode_name)
    
    print(f"{root_note} {mode_name} Mode:")
    print(f"Primary emotion: {mode_info['primary']}")
    print(f"Character: {mode_info['character']}")
    print(f"Associated moods: {', '.join(mode_info['moods'])}")
    print(f"Historical parallel: {mode_info['western_parallel']}")
    print(f"Energy level: {mode_info['energy_level']}/10")
    print(f"Emotional intensity: {mode_info['emotional_intensity']}/10")
    
    print("\nScale frequencies:")
    print(f"{'Note':<10} {'Frequency':<15}")
    print(f"{'-'*10} {'-'*15}")
    for note, freq in dorian_freqs.items():
        print(f"{note:<10} {format_freq(freq)}")
    
    # Get historical information
    history = wm.get_historical_usage(mode_name)
    
    print("\nHistorical Usage:")
    print(f"Eras: {', '.join(history['eras'])}")
    print(f"Prominence: {history['prominence']}")
    print(f"Typical contexts: {', '.join(history['contexts'])}")
    
    # Get common chord progressions
    progressions = wm.get_common_chord_progressions(mode_name)
    
    print("\nCommon Chord Progressions:")
    for progression in progressions:
        print(f"  {progression}")
    
    print_section("EMOTIONAL TRANSITIONS BETWEEN MODES")
    
    # Let's see transitions from Dorian to other modes
    compatible_modes = wm.get_compatible_modes(mode_name)
    
    print(f"Possible modal transitions from {mode_name}:")
    for target_mode, details in compatible_modes.items():
        print(f"\n→ {target_mode} - {details['primary_emotion']}")
        print(f"  Character: {details['character']}")
        print(f"  {details['energy_transition']} ({details['energy_difference']} change)")
        print(f"  Emotional intensity: {details['emotional_intensity']}/10")
        print(f"  Recommended instruments: {', '.join(details['recommended_instruments'][:3])}")
    
    print_section("COMPLEX TRANSITION PATH BETWEEN CONTRASTING MODES")
    
    # Define contrasting modes
    start_mode = "Lydian"     # Bright, dreamlike
    end_mode = "Locrian"      # Dark, unstable
    
    # Get transition path
    path = wm.suggest_transition_path(start_mode, end_mode)
    
    print(f"To transition from {start_mode} ({wm.modal_emotions[start_mode]['primary']}) to {end_mode} ({wm.modal_emotions[end_mode]['primary']}):")
    
    if path:
        print(f"\nRecommended path: {' → '.join(path)}")
        
        print("\nDetails for each transition stage:")
        for i, mode in enumerate(path):
            mode_info = wm.get_mode_info(mode)
            print(f"\nStage {i+1}: {mode} ({mode_info['primary']})")
            print(f"Character: {mode_info['character']}")
            print(f"Energy level: {mode_info['energy_level']}/10")
            print(f"Emotional intensity: {mode_info['emotional_intensity']}/10")
            
            # Show chord progression for this mode
            progressions = wm.get_common_chord_progressions(mode)
            print(f"Suggested chord progression: {progressions[0]}")
    else:
        print(f"No clear path found within the default steps. These modes are too contrasting.")
        print("Consider using more intermediate modes as bridges.")
    
    print_section("COMPARING ALL MODES BASED ON THE SAME ROOT")
    
    # Let's compare all modes with C as the root
    root = "C"
    octave = 4
    
    print(f"All modes built on {root}{octave}:")
    print(f"\n{'Mode':<12} {'Scale Degrees':<30} {'Character':<30}")
    print(f"{'-'*12} {'-'*30} {'-'*30}")
    
    # Define major scale degree names for reference
    scale_degrees = ["1", "♭2", "2", "♭3", "3", "4", "♯4/♭5", "5", "♭6", "6", "♭7", "7"]
    
    for mode_name in wm.modes:
        # Get the intervals for this mode
        intervals = wm.get_mode_intervals(mode_name)
        
        # Convert intervals to scale degree names
        degree_names = [scale_degrees[interval] for interval in intervals]
        
        # Get the character
        character = wm.modal_emotions[mode_name]["character"]
        
        print(f"{mode_name:<12} {', '.join(degree_names):<30} {character:<30}")
    
    print_section("CROSS-CULTURAL CONNECTIONS: WESTERN MODES AND INDIAN RASAS")
    
    # Initialize the NavarasaMap for cross-cultural comparisons
    nv = NavarasaMap()
    
    print("Western modes and their corresponding Indian rasas:")
    print(f"\n{'Mode':<12} {'Western Emotion':<15} {'Corresponding Rasas':<40}")
    print(f"{'-'*12} {'-'*15} {'-'*40}")
    
    for mode, rasas in wm.mode_to_rasa_map.items():
        mode_info = wm.get_mode_info(mode)
        print(f"{mode:<12} {mode_info['primary']:<15} {', '.join(rasas):<40}")
    
    # Get more detailed cross-cultural information for Dorian mode
    comparison = wm.compare_mode_to_raga(mode_name, root_note, octave, nv)
    
    print(f"\nDetailed cross-cultural analysis for {root_note} {mode_name}:")
    print(f"Emotional character: {comparison['emotional_character']}")
    
    print("\nCorresponding Indian Rasas:")
    for rasa in comparison['corresponding_rasas']:
        try:
            rasa_info = nv.get_rasa_info(rasa)
            print(f"  {rasa} - {rasa_info['english']} (Mood: {rasa_info['mood']})")
        except ValueError:
            print(f"  {rasa}")
    
    if 'related_ragas' in comparison and comparison['related_ragas']:
        print("\nRecommended Indian Ragas:")
        for raga in comparison['related_ragas'][:5]:  # Show top 5
            print(f"  {raga}")
    
    print_section("PRACTICAL APPLICATION: COMPOSITION FRAMEWORK")
    
    # Let's create a simple composition framework based on modes
    composition_framework = [
        {"section": "Intro", "mode": "Mixolydian", "emotion": "Playful", "suggested_progression": "I - ♭VII - IV - I"},
        {"section": "Verse", "mode": "Dorian", "emotion": "Serious", "suggested_progression": "i - IV - VII - i"},
        {"section": "Chorus", "mode": "Lydian", "emotion": "Wonder", "suggested_progression": "I - II - I"},
        {"section": "Bridge", "mode": "Phrygian", "emotion": "Tension", "suggested_progression": "i - ♭II - i"},
        {"section": "Outro", "mode": "Ionian", "emotion": "Joy", "suggested_progression": "I - IV - V - I"}
    ]
    
    print("Example composition framework using modal emotions:")
    print(f"\n{'Section':<10} {'Mode':<12} {'Emotion':<10} {'Chord Progression':<20} {'Energy':<8}")
    print(f"{'-'*10} {'-'*12} {'-'*10} {'-'*20} {'-'*8}")
    
    for section in composition_framework:
        energy = f"{wm.modal_emotions[section['mode']]['energy_level']}/10"
        print(f"{section['section']:<10} {section['mode']:<12} {section['emotion']:<10} {section['suggested_progression']:<20} {energy:<8}")
    
    print("\nTransition analysis:")
    for i in range(len(composition_framework) - 1):
        current = composition_framework[i]
        next_section = composition_framework[i+1]
        
        # Check if direct transition exists
        if next_section['mode'] in wm.compatible_transitions[current['mode']]:
            compatibility = "Direct transition (compatible)"
        else:
            compatibility = "Challenging transition (requires bridge)"
        
        # Calculate energy change
        energy_diff = wm.modal_emotions[next_section['mode']]['energy_level'] - wm.modal_emotions[current['mode']]['energy_level']
        if energy_diff > 0:
            energy_change = f"Energy boost (+{energy_diff})"
        elif energy_diff < 0:
            energy_change = f"Energy drop ({energy_diff})"
        else:
            energy_change = "Energy maintained"
        
        print(f"  {current['section']} ({current['mode']}) → {next_section['section']} ({next_section['mode']}): {compatibility}, {energy_change}")
    
    print_section("VISUALIZING THE MODAL WHEEL")
    
    print("Western Modal Wheel (simplified text representation):")
    print("\n                 Lydian (Wonder)")
    print("                 ↙   ↑    ↘")
    print("       Ionian (Joy) ←→ Mixolydian (Playful)")
    print("          ↑    ↓           ↑   ↓")
    print("          ↑    ↓           ↑   ↓")
    print("       Dorian (Serious) ←→ Aeolian (Sadness)")
    print("          ↑    ↓")
    print("          ↑    ↓")
    print("      Phrygian (Tension) ←→ Locrian (Instability)")
    
    print("\nThis wheel shows compatible emotional transitions between Western modes.")
    print("The modes are arranged to show natural progressions of emotional states.")
    print("Moving clockwise generally increases tension, while counter-clockwise releases it.")
    print("New transitions allow for more fluid emotional movement between contrasting states.")

if __name__ == "__main__":
    main()