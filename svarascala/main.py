"""
Command-line interface for SvaraScala.
"""

import argparse
import sys
from .western import WesternMusic
from .indian import IndianMusic

def format_freq(freq):
    """Format frequency to 2 decimal places"""
    return f"{freq:.2f} Hz"

def print_header(title):
    """Print a formatted header"""
    print("\n" + "=" * 60)
    print(title.center(60))
    print("=" * 60)

def western_note_info(args):
    """Display information about a Western note"""
    wm = WesternMusic(reference_a4=args.reference)
    
    try:
        freq = wm.get_frequency(args.note, args.octave)
        print(f"\nNote: {args.note}{args.octave}")
        print(f"Frequency: {format_freq(freq)}")
        
        # Show related harmonic notes
        print("\nHarmonic relationships:")
        for other_note in wm.notes:
            for other_octave in range(args.octave - 1, args.octave + 2):
                if other_note == args.note and other_octave == args.octave:
                    continue
                is_harmonic, relation = wm.are_harmonic(args.note, args.octave, other_note, other_octave)
                if is_harmonic:
                    other_freq = wm.get_frequency(other_note, other_octave)
                    print(f"  {other_note}{other_octave} ({format_freq(other_freq)}) - {relation}")
    
    except Exception as e:
        print(f"Error: {str(e)}")
        return 1
    
    return 0

def western_scale_info(args):
    """Display information about a Western scale"""
    wm = WesternMusic(reference_a4=args.reference)
    
    try:
        scale = wm.get_scale(args.root, args.octave, args.scale_type)
        
        print(f"\nScale: {args.root} {args.scale_type}, Octave: {args.octave}")
        print("-" * 40)
        print(f"{'Note':<10} {'Frequency':<15}")
        print("-" * 40)
        
        for note, freq in scale.items():
            print(f"{note:<10} {format_freq(freq)}")
    
    except Exception as e:
        print(f"Error: {str(e)}")
        return 1
    
    return 0

def indian_swara_info(args):
    """Display information about an Indian swara"""
    im = IndianMusic(reference_sa=args.reference)
    
    try:
        variant = args.variant if args.variant else "shuddha"
        freq = im.get_swara_frequency(args.swara, variant)
        
        print(f"\nSwara: {args.swara} {variant}")
        print(f"Frequency: {format_freq(freq)}")
        
        # Show ratio from Sa
        ratio = freq / im.reference_sa
        print(f"Ratio from Sa: {ratio:.4f}")
        
        # Show corresponding shruti
        if args.swara == "Sa" or args.swara == "Pa":
            shruti_num = im.swara_to_shruti[args.swara]
        else:
            shruti_num = im.swara_to_shruti[args.swara][variant]
        
        print(f"Corresponding Shruti: {shruti_num}")
    
    except Exception as e:
        print(f"Error: {str(e)}")
        return 1
    
    return 0

def indian_raga_info(args):
    """Display information about an Indian raga"""
    im = IndianMusic(reference_sa=args.reference)
    
    try:
        frequencies = im.calculate_raga_frequencies(args.raga)
        
        print(f"\nRaga: {args.raga}, Sa: {format_freq(args.reference)}")
        print("-" * 40)
        print(f"{'Swara':<15} {'Frequency':<15} {'Ratio to Sa':<15}")
        print("-" * 40)
        
        for swara, freq in frequencies.items():
            ratio = freq / im.reference_sa
            print(f"{swara:<15} {format_freq(freq):<15} {ratio:.4f}")
    
    except Exception as e:
        print(f"Error: {str(e)}")
        return 1
    
    return 0

def main():
    """Main entry point for the command line interface"""
    parser = argparse.ArgumentParser(description="SvaraScala - Musical frequency calculations")
    subparsers = parser.add_subparsers(dest="command", help="Command")
    
    # Western note parser
    western_note_parser = subparsers.add_parser("western-note", help="Get information about a Western note")
    western_note_parser.add_argument("note", help="Note name (e.g., C, F#)")
    western_note_parser.add_argument("octave", type=int, help="Octave number")
    western_note_parser.add_argument("--reference", type=float, default=440.0, help="Reference frequency for A4 (default: 440 Hz)")
    
    # Western scale parser
    western_scale_parser = subparsers.add_parser("western-scale", help="Get information about a Western scale")
    western_scale_parser.add_argument("root", help="Root note (e.g., C, F#)")
    western_scale_parser.add_argument("octave", type=int, help="Octave number")
    western_scale_parser.add_argument("--scale-type", default="major", help="Scale type (e.g., major, minor, blues)")
    western_scale_parser.add_argument("--reference", type=float, default=440.0, help="Reference frequency for A4 (default: 440 Hz)")
    
    # Indian swara parser
    indian_swara_parser = subparsers.add_parser("indian-swara", help="Get information about an Indian swara")
    indian_swara_parser.add_argument("swara", help="Swara name (e.g., Sa, Re, Ga)")
    indian_swara_parser.add_argument("--variant", help="Variant (e.g., komal, shuddha, tivra)")
    indian_swara_parser.add_argument("--reference", type=float, default=220.0, help="Reference frequency for Sa (default: 220 Hz)")
    
    # Indian raga parser
    indian_raga_parser = subparsers.add_parser("indian-raga", help="Get information about an Indian raga")
    indian_raga_parser.add_argument("raga", help="Raga name (e.g., Yaman, Bhairav)")
    indian_raga_parser.add_argument("--reference", type=float, default=220.0, help="Reference frequency for Sa (default: 220 Hz)")
    
    args = parser.parse_args()
    
    if args.command is None:
        parser.print_help()
        return 0
    
    # Dispatch to the appropriate handler
    if args.command == "western-note":
        return western_note_info(args)
    elif args.command == "western-scale":
        return western_scale_info(args)
    elif args.command == "indian-swara":
        return indian_swara_info(args)
    elif args.command == "indian-raga":
        return indian_raga_info(args)
    
    return 0

if __name__ == "__main__":
    sys.exit(main())