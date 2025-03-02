#!/usr/bin/env python3
"""
Example of using the Navarasa (Nine Sentiments) map in SvaraScala.

This script demonstrates how to use the Navarasa map for melodic transitions
based on emotional qualities in Indian classical music, similar to how the
Camelot wheel is used for harmonic transitions in Western music.
"""

from svarascala import WesternMusic, IndianMusic, NavarasaMap


def print_section(title):
    """Print a section header."""
    print(f"\n{'-' * 70}")
    print(f" {title}")
    print(f"{'-' * 70}")


def format_freq(freq):
    """Format frequency to 2 decimal places."""
    return f"{freq:.2f} Hz"


def main():
    # Initialize the NavarasaMap
    nw = NavarasaMap(reference_sa=220.0)  # Set Sa to 220 Hz (A3)
    
    print_section("NAVARASA - THE WHEEL OF NINE EMOTIONS IN INDIAN MUSIC")
    
    print("The nine emotional states (rasas) and their associated characteristics:")
    print(f"\n{'Rasa':<12} {'English':<20} {'Mood':<12} {'Time':<15} {'Color':<12}")
    print(f"{'-'*12} {'-'*20} {'-'*12} {'-'*15} {'-'*12}")
    
    for rasa, info in nw.rasas.items():
        print(f"{rasa:<12} {info['english']:<20} {info['mood']:<12} {info['time']:<15} {info['color']:<12}")
    
    print_section("RAGAS ASSOCIATED WITH EACH RASA")
    
    # Show ragas for each rasa
    for rasa in nw.rasas:
        ragas = nw.get_raga_by_rasa(rasa)
        print(f"{rasa:<12} ({nw.rasas[rasa]['english']}): {', '.join(ragas)}")
    
    print_section("EMOTIONAL TRANSITION EXAMPLE: SRINGARA (LOVE) TO OTHER EMOTIONS")
    
    # Starting point
    start_rasa = "Sringara"  # Love/Erotic
    
    # Get rasa info
    rasa_info = nw.get_rasa_info(start_rasa)
    print(f"Starting with {start_rasa} ({rasa_info['english']}):")
    print(f"Mood: {rasa_info['mood']}, Associated time: {rasa_info['time']}")
    
    # Get compatible transitions
    transitions = nw.get_compatible_rasas(start_rasa)
    
    # Sort transitions by energy level
    sorted_transitions = sorted(transitions.items(), 
                               key=lambda x: x[1]['energy_level'], 
                               reverse=True)
    
    print("\nPossible transitions (ordered by energy level):")
    for rasa, details in sorted_transitions:
        print(f"\n→ {rasa} - {details['description']}")
        print(f"  {details['transition_type']} ({details['energy_difference']} change)")
        print(f"  Energy level: {details['energy_level']}/10")
        print("  Suggested ragas:")
        for raga in details['recommended_ragas'][:3]:  # Show top 3 ragas
            print(f"  - {raga}")
    
    print_section("COMPLEX TRANSITION EXAMPLE: MOVING BETWEEN CONTRASTING EMOTIONS")
    
    # Define contrasting emotions
    start = "Karuna"     # Compassion/Pathos
    end = "Veera"        # Heroism/Bravery
    
    # Get transition path
    path = nw.suggest_transition_path(start, end)
    
    print(f"To transition from {start} ({nw.rasas[start]['english']}) to {end} ({nw.rasas[end]['english']}):")
    
    if path:
        print(f"\nRecommended path: {' → '.join(path)}")
        
        print("\nDetails for each transition stage:")
        for i, rasa in enumerate(path):
            print(f"\nStage {i+1}: {rasa} ({nw.rasas[rasa]['english']})")
            print(f"Mood: {nw.rasas[rasa]['mood']}, Energy level: {nw.energy_levels[rasa]}/10")
            
            # Show recommended ragas
            ragas = nw.get_raga_by_rasa(rasa)
            primary_raga = ragas[0]
            print(f"Primary raga: {primary_raga}")
            
            # Show frequencies for primary raga
            if i < len(path) - 1:  # Don't show frequencies for the last stage to save space
                freqs = nw.get_raga_frequencies(primary_raga)
                print(f"Key swaras (with Sa = 220.00 Hz):")
                for swara, freq in list(freqs.items())[:3]:  # Show just the first few swaras
                    print(f"  - {swara}: {format_freq(freq)}")
    else:
        print(f"No clear path found within 3 steps. These emotions are too contrasting.")
        print("Consider using an intermediate rasa as a bridge.")
    
    print_section("BRIDGING WESTERN AND INDIAN MUSIC THROUGH NAVARASA")
    
    # Example ragas and their Western equivalents
    example_ragas = ["Yaman", "Bhairav", "Bhairavi"]
    
    print("Western equivalents for selected ragas (with DJ Camelot notation):")
    for raga in example_ragas:
        western_equiv = nw.get_western_equivalent(raga)
        rasas = nw.get_rasa_from_raga(raga)
        
        print(f"\n{raga} (Thaat: {western_equiv['thaat']}):")
        print(f"  Western equivalent: {western_equiv['scale_type']}")
        print(f"  Suggested key: {western_equiv['suggested_key']}")
        
        # Display Camelot notation (for DJs)
        if western_equiv['camelot_notation']:
            print(f"  Camelot notation: {western_equiv['camelot_notation']} " +
                  f"({western_equiv['suggested_key']} {western_equiv['scale_type'] == 'Natural Minor' or western_equiv['scale_type'] == 'Phrygian' or western_equiv['scale_type'] == 'Dorian' and 'minor' or 'major'})")
            
            # Show compatible keys in Camelot wheel
            print("  Compatible DJ keys (Camelot wheel):")
            for camelot, key in western_equiv['compatible_camelot_keys'].items():
                print(f"    {camelot}: {key}")
        else:
            print("  No direct Camelot wheel equivalent")
        
        print(f"  Associated rasas: {', '.join(rasas)}")
        print(f"  Western correlations: {', '.join(western_equiv['western_correlations'])}")
    
    print_section("DJ MIXING EXAMPLE USING RASA-BASED TRANSITIONS")
    
    # Example DJ set
    dj_set = [
        {"rasa": "Saantha", "raga": "Bhimpalasi", "description": "Opening set - calm, meditative"},
        {"rasa": "Adbutham", "raga": "Darbari", "description": "Building wonder and amazement"},
        {"rasa": "Sringara", "raga": "Yaman", "description": "Peak time - love and romance"},
        {"rasa": "Veera", "raga": "Bilawal", "description": "High energy - heroic emotions"},
        {"rasa": "Saantha", "raga": "Jaunpuri", "description": "Closing - return to tranquility"}
    ]
    
    print("Example DJ set using Navarasa wheel for emotional progression:")
    print(f"\n{'Time':<10} {'Rasa':<12} {'Raga':<15} {'Description':<30} {'Energy':<10}")
    print(f"{'-'*10} {'-'*12} {'-'*15} {'-'*30} {'-'*10}")
    
    for i, track in enumerate(dj_set):
        time_slot = f"{i+1}/5"
        energy = f"{nw.energy_levels[track['rasa']]}/10"
        print(f"{time_slot:<10} {track['rasa']:<12} {track['raga']:<15} {track['description']:<30} {energy:<10}")
    
    print("\nTransition analysis:")
    for i in range(len(dj_set) - 1):
        current = dj_set[i]
        next_track = dj_set[i+1]
        
        if next_track['rasa'] in nw.compatible_transitions[current['rasa']]:
            compatibility = "Direct transition (compatible)"
        else:
            compatibility = "Challenging transition (not directly compatible)"
        
        energy_diff = nw.energy_levels[next_track['rasa']] - nw.energy_levels[current['rasa']]
        if energy_diff > 0:
            energy_change = f"Energy boost (+{energy_diff})"
        elif energy_diff < 0:
            energy_change = f"Energy drop ({energy_diff})"
        else:
            energy_change = "Energy maintained"
        
        print(f"  {current['rasa']} → {next_track['rasa']}: {compatibility}, {energy_change}")
    
    print_section("DETAILED RAGA COMPARISON - INDIAN VS WESTERN (FOR DJS)")
    
    # Example comparative analysis
    comparison_raga = "Yaman"
    comparison = nw.compare_raga_to_western_scale(comparison_raga, western_root="C", octave=4)
    
    print(f"Comparing {comparison_raga} with {comparison['western_scale']}:")
    print(f"Thaat: {comparison['thaat']}")
    
    # Display Camelot notation for DJs
    if comparison['camelot_notation']:
        print(f"Camelot wheel position: {comparison['camelot_notation']}")
        
        print("\nCompatible DJ keys (Camelot wheel):")
        for camelot, key in comparison['compatible_camelot_keys'].items():
            print(f"  {camelot}: {key}")
    
    print(f"\nAssociated rasas: {', '.join(comparison['rasas'])}")
    
    print("\nIndian swaras:")
    for swara, freq in comparison['raga_frequencies'].items():
        print(f"  {swara:<15} {format_freq(freq)}")
    
    print("\nWestern scale notes:")
    for note, freq in comparison['western_frequencies'].items():
        print(f"  {note:<10} {format_freq(freq)}")

    print_section("CREATING A RASA-BASED VISUALIZATION OF HARMONIC RELATIONSHIPS")
    
    print("Navarasa Emotional Wheel (simplified text representation):")
    print("\n          Adbutham (Wonder) ←→ Haasya (Comedy)")
    print("            ↑    ↓                ↑    ↓")
    print("            ↑    ↓                ↑    ↓")
    print("     Sringara (Love) ←------→ Veera (Heroism)")
    print("         ↑    ↓                   ↑    ↓")
    print("         ↑    ↓                   ↑    ↓")
    print("     Saantha (Peace) ←------→ Raudra (Anger)")
    print("            ↑    ↓             ↑    ↓")
    print("            ↑    ↓             ↑    ↓")
    print("       Karuna (Pathos) ←→ Bhayaanaka (Fear) ←→ Beebhatsa (Disgust)")
    
    print("\nCompatible emotional transitions between Indian Navarasa sentiments.")
    print("The rasas are arranged to show natural progressions of emotional states.")
    print("Energy generally increases clockwise and decreases counter-clockwise.")

    print_section("DJ MIXING EXAMPLE USING RASA-BASED TRANSITIONS AND CAMELOT NOTATION")
    
    # Example DJ set with Western equivalents and Camelot notation
    wm = WesternMusic()  # For getting Camelot notation
    
    dj_set = [
        {"rasa": "Saantha", "raga": "Bhimpalasi", "description": "Opening set - calm, meditative"},
        {"rasa": "Adbutham", "raga": "Darbari", "description": "Building wonder and amazement"},
        {"rasa": "Sringara", "raga": "Yaman", "description": "Peak time - love and romance"},
        {"rasa": "Veera", "raga": "Bilawal", "description": "High energy - heroic emotions"},
        {"rasa": "Saantha", "raga": "Jaunpuri", "description": "Closing - return to tranquility"}
    ]
    
    # Add Western equivalents and Camelot notations
    for track in dj_set:
        western_equiv = nw.get_western_equivalent(track["raga"])
        track["western_key"] = western_equiv.get("suggested_key", "C")
        track["western_scale"] = western_equiv.get("scale_type", "Major")
        track["camelot"] = western_equiv.get("camelot_notation", "N/A")
    
    print("Example DJ set using Navarasa wheel for emotional progression:")
    print(f"\n{'Time':<8} {'Rasa':<10} {'Raga':<12} {'Western Key':<12} {'Camelot':<8} {'Description':<30} {'Energy':<8}")
    print(f"{'-'*8} {'-'*10} {'-'*12} {'-'*12} {'-'*8} {'-'*30} {'-'*8}")
    
    for i, track in enumerate(dj_set):
        time_slot = f"{i+1}/5"
        energy = f"{nw.energy_levels[track['rasa']]}/10"
        western = f"{track['western_key']} {track['western_scale']}"
        print(f"{time_slot:<8} {track['rasa']:<10} {track['raga']:<12} {western:<12} {track['camelot']:<8} {track['description']:<30} {energy:<8}")
    
    print("\nTransition analysis:")
    for i in range(len(dj_set) - 1):
        current = dj_set[i]
        next_track = dj_set[i+1]
        
        # Emotional transition analysis
        if next_track['rasa'] in nw.compatible_transitions[current['rasa']]:
            compatibility = "Direct transition (compatible)"
        else:
            compatibility = "Challenging transition (not directly compatible)"
        
        energy_diff = nw.energy_levels[next_track['rasa']] - nw.energy_levels[current['rasa']]
        if energy_diff > 0:
            energy_change = f"Energy boost (+{energy_diff})"
        elif energy_diff < 0:
            energy_change = f"Energy drop ({energy_diff})"
        else:
            energy_change = "Energy maintained"
        
        # Camelot wheel transition analysis
        camelot_analysis = ""
        if current['camelot'] != "N/A" and next_track['camelot'] != "N/A":
            if current['camelot'] == next_track['camelot']:
                camelot_analysis = f", Perfect Camelot match"
            elif next_track['camelot'] in wm.get_compatible_keys(current['camelot']):
                camelot_analysis = f", Compatible Camelot keys"
            else:
                camelot_analysis = f", Camelot key change"
        
        print(f"  {current['rasa']} → {next_track['rasa']}: {compatibility}, {energy_change}{camelot_analysis}")
        print(f"    Camelot transition: {current['camelot']} → {next_track['camelot']}")

if __name__ == "__main__":
    main()