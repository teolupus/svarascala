"""
Examples demonstrating the SvaraScala library with both Western and Indian musical scales

"From Ut to Sa, the circle forms,
Two ancient paths of sacred tones.
Resonare meets Rishabha's call,
Gandharva's flight to Mira soars.

Where Madhyama and Mi converge,
Panchama's fifth aligns with Sol.
Dhaivata dances with La's light,
As Ni and Sancte sound complete.

One breath, two voices, seven stars—
The universe in vibrant song."
— SavaraScala, 6ee6c386cfe3d78ae2e339befefef55f349d3fd4

"যে স্রোতে জগতের খেলা, সেই স্রোতে আমার প্রাণের খেলা,
তাহাতেই আমার আনন্দের তরঙ্গ বাজে।
আমার হৃদয়ের তার গাঁথা আছে জগতের সুরের সঙ্গে,
তাহাতেই আমার সঙ্গীত জাগে।"
— Rabindranath Tagore, "Gitanjali: Song Offerings", Verse 69

"The same stream of life that runs through my veins night and day runs through
the world and dances in rhythmic measures. It is the same life that shoots in
joy through the dust of the earth in numberless blades of grass and breaks into
tumultuous waves of leaves and flowers."

"""

from svarascala import WesternMusic, IndianMusic

def format_freq(freq):
    """Format frequency to 2 decimal places"""
    return f"{freq:.2f} Hz"

def print_header(title):
    """Print a formatted header"""
    print("\n" + "=" * 60)
    print(title.center(60))
    print("=" * 60)

def print_scale_comparison(title, scale_dict):
    """Print a nicely formatted scale"""
    print("\n" + title)
    print("-" * 40)
    for note, freq in scale_dict.items():
        print(f"{note:<10} {format_freq(freq)}")

def main():
    # Initialize both music systems
    western = WesternMusic(reference_a4=440.0)
    indian = IndianMusic(reference_sa=220.0)  # Sa at A3
    
    print_header("SvaraScala Music Scale Comparison")
    
    # Example 1: Raga Yaman (equivalent to Lydian mode in Western music)
    print_header("EXAMPLE 1: RAGA YAMAN")
    print("Raga Yaman is one of the fundamental ragas in Hindustani classical music.")
    print("It corresponds roughly to the Lydian mode in Western music.")
    
    # Get the Indian Raga Yaman frequencies
    yaman_freqs = indian.calculate_raga_frequencies("Yaman")
    
    # Display the frequencies of Raga Yaman
    print("\nIndian Classical: Raga Yaman (Sa = 220 Hz)")
    print("-" * 40)
    for swara, freq in yaman_freqs.items():
        print(f"{swara:<15} {format_freq(freq)}")
    
    # Western equivalent: F Lydian scale
    # F Lydian has the same pattern of whole and half steps as Raga Yaman
    f_lydian = western.get_scale("F", 4, "major")
    f_lydian[f"B4"] = western.get_frequency("B", 4)  # Add raised 4th
    f_lydian.pop(f"Bb4", None)  # Remove the perfect 4th
    
    print_scale_comparison("Western Equivalent: F Lydian Scale (A4 = 440 Hz)", f_lydian)
    
    # Example 2: Raga Bhairav
    print_header("EXAMPLE 2: RAGA BHAIRAV")
    print("Raga Bhairav is one of the oldest ragas in Hindustani classical music,")
    print("often performed in the early morning. It has a distinctive signature with")
    print("komal (flat) Re and Dha.")
    
    # Get the Indian Raga Bhairav frequencies
    bhairav_freqs = indian.calculate_raga_frequencies("Bhairav")
    
    # Display the frequencies of Raga Bhairav
    print("\nIndian Classical: Raga Bhairav (Sa = 220 Hz)")
    print("-" * 40)
    for swara, freq in bhairav_freqs.items():
        print(f"{swara:<15} {format_freq(freq)}")
    
    # Western equivalent: There's no exact equivalent, but closest is a mode of the double harmonic scale
    # We'll construct it manually - now using flat notation for consistency
    bhairav_western = {
        "C4": western.get_frequency("C", 4),       # Sa
        "Db4": western.get_frequency("Db", 4),     # komal Re
        "E4": western.get_frequency("E", 4),       # Ga
        "F4": western.get_frequency("F", 4),       # Ma
        "G4": western.get_frequency("G", 4),       # Pa
        "Ab4": western.get_frequency("Ab", 4),     # komal Dha
        "B4": western.get_frequency("B", 4),       # Ni
        "C5": western.get_frequency("C", 5)        # Sa (upper octave)
    }
    
    print_scale_comparison("Western Approximation: C Double Harmonic Scale (A4 = 440 Hz)", bhairav_western)
    
    # Example 3: Western Major Scale
    print_header("EXAMPLE 3: WESTERN C MAJOR SCALE")
    print("The C Major scale is the most fundamental scale in Western music,")
    print("using all white keys on the piano with no sharps or flats.")
    
    # Get the Western C Major scale
    c_major = western.get_scale("C", 4, "major")
    
    # Display the frequencies of C Major
    print_scale_comparison("Western: C Major Scale (A4 = 440 Hz)", c_major)
    
    # Indian equivalent: Similar to Bilawal thaat
    bilawal = {
        "Sa shuddha": indian.get_swara_frequency("Sa", "shuddha"),
        "Re shuddha": indian.get_swara_frequency("Re", "shuddha"),
        "Ga shuddha": indian.get_swara_frequency("Ga", "shuddha"),
        "Ma shuddha": indian.get_swara_frequency("Ma", "shuddha"),
        "Pa shuddha": indian.get_swara_frequency("Pa", "shuddha"),
        "Dha shuddha": indian.get_swara_frequency("Dha", "shuddha"),
        "Ni shuddha": indian.get_swara_frequency("Ni", "shuddha"),
        "Sa' shuddha": indian.reference_sa * 2  # Sa in upper octave
    }
    
    print_scale_comparison("Indian Equivalent: Bilawal Thaat (Sa = 220 Hz)", bilawal)
    
    # Example 4: Western Minor Blues Scale
    print_header("EXAMPLE 4: WESTERN A MINOR BLUES SCALE")
    print("The Blues scale is characteristic of blues, jazz, and rock music.")
    print("It introduces 'blue notes' that give the scale its distinctive sound.")
    
    # Get the Western A Minor Blues scale
    a_blues = western.get_scale("A", 4, "blues")
    
    # Display the frequencies of A Minor Blues
    print_scale_comparison("Western: A Minor Blues Scale (A4 = 440 Hz)", a_blues)
    
    # Indian equivalent: No direct equivalent, but we can approximate some aspects
    # Using a combination of komal swaras to approximate the blue notes
    blues_indian = {
        "Sa shuddha": indian.get_swara_frequency("Sa", "shuddha") * 2,  # A4 is Sa
        "Ga komal": indian.get_swara_frequency("Ga", "komal") * 2,      # Matches minor third
        "Ma shuddha": indian.get_swara_frequency("Ma", "shuddha") * 2,  # Perfect fourth
        "Ma tivra": indian.get_swara_frequency("Ma", "tivra") * 2,      # Approximates blues note
        "Pa shuddha": indian.get_swara_frequency("Pa", "shuddha") * 2,  # Perfect fifth
        "Ni komal": indian.get_swara_frequency("Ni", "komal") * 2,      # Minor seventh
    }
    
    print_scale_comparison("Indian Approximation (using komal & tivra swaras)", blues_indian)
    
    # Harmonic analysis across systems
    print_header("HARMONIC ANALYSIS ACROSS SYSTEMS")
    
    # Compare perfect fifth in both systems
    western_fifth = western.get_frequency("C", 4) / western.get_frequency("G", 4)
    indian_fifth = indian.get_swara_frequency("Sa") / indian.get_swara_frequency("Pa")
    
    print(f"Perfect fifth ratio (Western): {western_fifth:.4f}")
    print(f"Perfect fifth ratio (Indian): {indian_fifth:.4f}")
    print(f"Difference: {abs(western_fifth - indian_fifth):.6f}")
    
    # Compare major third in both systems
    western_third = western.get_frequency("C", 4) / western.get_frequency("E", 4)
    indian_third = indian.get_swara_frequency("Sa") / indian.get_swara_frequency("Ga", "shuddha")
    
    print(f"\nMajor third ratio (Western): {western_third:.4f}")
    print(f"Major third ratio (Indian): {indian_third:.4f}")
    print(f"Difference: {abs(western_third - indian_third):.6f}")
    
    print("\nNote: Western equal temperament slightly adjusts pure ratios for modulation,")
    print("while Indian classical music maintains pure harmonic ratios.")

if __name__ == "__main__":
    main()