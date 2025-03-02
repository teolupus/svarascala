"""
Western music frequency calculations for the SvaraScala library.

"Sunt autem haec: proslambanomenos, hypate hypaton, parhypate hypaton, lichanos
hypaton, hypate meson, parhypate meson, lichanos meson, mese, paramese, trite
diezeugmenon, paranete diezeugmenon, nete diezeugmenon, trite hyperbolaeon,
paranete hyperbolaeon, nete hyperbolaeon."
— Boethius, De institutione musica, Book IV

"These are as follows: the added note, the lowest of the lowest, the next to
lowest of the lowest, the index finger of the lowest, the lowest of the middle,
the next to lowest of the middle, the index finger of the middle, the middle,
the next to middle, the third of the separated, the next to last of the
separated, the last of the separated, the third of the highest, the next to
last of the highest, the last of the highest."

"Ut queant laxis
Resonare fibris,
Mira gestorum
Famuli tuorum,
Solve polluti
Labii reatum,
Sancte Ioannes."
- Guido d'Arezzo, Micrologus

"So that your servants
May sing with clear voices
The wonders of your deeds,
Remove the guilt
From our stained lips,
O Saint John."

"""

class WesternMusic:
    """
    Class to handle frequency calculations for Western music.
    """
    def __init__(self, reference_a4=440.0):
        """
        Initialize with a reference frequency for A4 (defaults to 440 Hz).
        
        Args:
            reference_a4 (float): Reference frequency for A4 in Hz. Default is 440.0 Hz.
        """
        self.reference_a4 = reference_a4
        self.notes = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
        
        # Mapping between sharp and flat notations
        self.enharmonic_map = {
            'C#': 'Db', 'Db': 'C#',
            'D#': 'Eb', 'Eb': 'D#',
            'F#': 'Gb', 'Gb': 'F#',
            'G#': 'Ab', 'Ab': 'G#',
            'A#': 'Bb', 'Bb': 'A#'
        }
        
        self.solfege = ['Do', 'Di', 'Re', 'Ri', 'Mi', 'Fa', 'Fi', 'Sol', 'Si', 'La', 'Li', 'Ti']
    
    def get_frequency(self, note, octave):
        """
        Calculate the frequency of a given note in a given octave.
        
        Args:
            note (str): Note name (e.g., 'C', 'D#', 'F', etc.)
            octave (int): Octave number (e.g., 4 for middle C)
            
        Returns:
            float: Frequency in Hz
        
        Examples:
            >>> wm = WesternMusic()
            >>> round(wm.get_frequency('A', 4), 1)
            440.0
            >>> round(wm.get_frequency('C', 4), 1)
            261.6
            >>> round(wm.get_frequency('Db', 4), 1)  # Flat notation
            277.2
        """
        # Convert flat notation to sharp if needed
        if note not in self.notes and note in self.enharmonic_map:
            note = self.enharmonic_map[note]
        
        # Calculate semitone distance from A4
        if note not in self.notes:
            raise ValueError(f"Unknown note: {note}. Available notes: {', '.join(self.notes + list(set(self.enharmonic_map.keys()) - set(self.notes)))}")
            
        note_index = self.notes.index(note)
        a_index = self.notes.index('A')
        
        # Calculate semitone distance
        distance = note_index - a_index + (octave - 4) * 12
        
        # Calculate frequency using the formula: f = reference_a4 * (2^(n/12))
        frequency = self.reference_a4 * (2 ** (distance / 12))
        
        return frequency
    
    def get_solfege_frequency(self, solfege_name, octave, key='C'):
        """
        Calculate the frequency of a solfege syllable in a given key.
        
        Args:
            solfege_name (str): Solfege name (e.g., 'Do', 'Re', 'Mi', etc.)
            octave (int): Octave number
            key (str): Key to use as 'Do' (default is 'C')
            
        Returns:
            float: Frequency in Hz
        
        Examples:
            >>> wm = WesternMusic()
            >>> round(wm.get_solfege_frequency('Do', 4, 'C'), 1)
            261.6
            >>> round(wm.get_solfege_frequency('Sol', 4, 'C'), 1)
            392.0
        """
        # Find the index of the solfege name
        solfege_index = self.solfege.index(solfege_name)
        
        # Find the index of the key
        key_index = self.notes.index(key)
        
        # Calculate the actual note
        note_index = (key_index + solfege_index) % 12
        actual_note = self.notes[note_index]
        
        # Adjust octave if solfege crosses octave boundary
        octave_adjustment = (key_index + solfege_index) // 12
        actual_octave = octave + octave_adjustment
        
        return self.get_frequency(actual_note, actual_octave)
    
    def get_scale(self, root_note, octave, scale_type='major'):
        """
        Get frequencies for notes in a given scale.
        
        Args:
            root_note (str): Root note of the scale (e.g., 'C', 'F#', etc.)
            octave (int): Octave number for the root note
            scale_type (str): Type of scale ('major', 'minor', 'minor_harmonic', etc.)
            
        Returns:
            dict: Dictionary mapping note names to frequencies
        
        Examples:
            >>> wm = WesternMusic()
            >>> c_major = wm.get_scale('C', 4, 'major')
            >>> len(c_major)
            7
            >>> 'C4' in c_major
            True
        """
        # Define scale patterns (semitone intervals)
        scale_patterns = {
            'major': [0, 2, 4, 5, 7, 9, 11],
            'minor': [0, 2, 3, 5, 7, 8, 10],
            'minor_harmonic': [0, 2, 3, 5, 7, 8, 11],
            'minor_melodic': [0, 2, 3, 5, 7, 9, 11],
            'chromatic': list(range(12)),
            'pentatonic_major': [0, 2, 4, 7, 9],
            'pentatonic_minor': [0, 3, 5, 7, 10],
            'blues': [0, 3, 5, 6, 7, 10]
        }
        
        if scale_type not in scale_patterns:
            raise ValueError(f"Unknown scale type: {scale_type}")
        
        # Get the pattern for the requested scale
        pattern = scale_patterns[scale_type]
        
        # Get the index of the root note
        root_index = self.notes.index(root_note)
        
        # Calculate all notes in the scale
        scale = {}
        for i, interval in enumerate(pattern):
            # Calculate the note index
            note_index = (root_index + interval) % 12
            actual_note = self.notes[note_index]
            
            # Calculate the octave adjustment
            octave_adjustment = (root_index + interval) // 12
            actual_octave = octave + octave_adjustment
            
            # Get the frequency
            frequency = self.get_frequency(actual_note, actual_octave)
            
            # Add to the scale dictionary
            scale[f"{actual_note}{actual_octave}"] = frequency
            
        return scale
    
    def are_harmonic(self, note1, octave1, note2, octave2, tolerance=0.01):
        """
        Determine if two notes have a harmonic relationship.
        
        Args:
            note1 (str): First note name
            octave1 (int): Octave of first note
            note2 (str): Second note name
            octave2 (int): Octave of second note
            tolerance (float): Tolerance for ratio comparison
            
        Returns:
            tuple: (bool, str) - Whether harmonic and description of relationship
        
        Examples:
            >>> wm = WesternMusic()
            >>> wm.are_harmonic('C', 4, 'G', 4)[0]  # Perfect fifth
            True
            >>> wm.are_harmonic('C', 4, 'F#', 4)[0]  # Tritone
            False
        """
        # Get frequencies of both notes
        freq1 = self.get_frequency(note1, octave1)
        freq2 = self.get_frequency(note2, octave2)
        
        # Make sure freq1 is the lower frequency
        if freq1 > freq2:
            freq1, freq2 = freq2, freq1
        
        # Calculate the frequency ratio
        ratio = freq2 / freq1
        
        # Common harmonic ratios
        harmonic_ratios = [
            (2, 1),  # octave
            (3, 2),  # perfect fifth
            (4, 3),  # perfect fourth
            (5, 4),  # major third
            (6, 5),  # minor third
            (5, 3),  # major sixth
            (8, 5),  # minor sixth
            (9, 8),  # major second
            (16, 15) # minor second
        ]
        
        for num, denom in harmonic_ratios:
            harmonic_ratio = num / denom
            if abs(ratio - harmonic_ratio) < tolerance:
                return True, f"{num}:{denom} ratio ({harmonic_ratio:.3f})"
        
        return False, "Not a harmonic relationship"
    
'''
"Sed haec quae de Musica breviter dicta sunt, tironibus interim satisfaciant,
quatenus huius artis prima vestibula ingredientes, hanc multiplicem variamque
notarum formam sine magistro penetrare valeant; quod hactenus neminem potuisse
vidimus. Vocum autem industria iuxta consimilem modificationem diligens lector
poterit inspicere. His itaque praelibatis, cum divina gratia, omnium opifice
bonorum, quae sine invidia communicat affluentissime, ea quae de Musica dicenda
sunt, quibuslibet cantoribus utilissima percipiant."
- Guido d'Arezzo, Micrologus

"But let these things, which have been briefly said about Music, satisfy
beginners for now, so that those entering the first doors of this art may be
able to penetrate this complex and varied form of notation without a teacher;
which we have seen no one able to do until now. The diligent reader will be
able to examine the industry of voices according to a similar modification. So,
having touched on these things, with divine grace, the maker of all good
things, which communicates most abundantly without envy, may they receive those
things which are to be said about Music, most useful to any singers."
'''