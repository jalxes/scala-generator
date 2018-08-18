
tom = 2
semitom = 1

notes = (
    'C',
    'Db',
    'D',
    'Eb',
    'E',
    'F',
    'Gb',
    'G',
    'Ab',
    'A',
    'Bb',
    'B',
)


def add_note(note, distance):
    if (note + distance) > 11:
        return (note + distance) - 12
    return note + distance


def get_note(note):
    return notes.index(note)
