
tom = 2
semitom = 1

notes = (
    'C',
    'C#/Db',
    'D',
    'D#/Eb',
    'E',
    'F',
    'F#/Gb',
    'G',
    'G#/Ab',
    'A',
    'A#/Bb',
    'B',
)


def add_note(note, distance):
    if (note + distance) > 11:
        return (note + distance) - 12
    return note + distance


def get_note(note):
    return notes.index(note)
