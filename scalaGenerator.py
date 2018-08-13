#!/usr/bin/env python

tom = 2
semitom = 1
print('|scale|I|II|III|IV|V|VI|VII|VIII')
print('|---|---|---|---|---|---|---|---|---|')

notes = {
    0: 'C',
    1: 'C#',
    2: 'D',
    3: 'D#',
    4: 'E',
    5: 'F',
    6: 'F#',
    7: 'G',
    8: 'G#',
    9: 'A',
    10: 'A#',
    11: 'B',
    12: 'C',
}

def sumNote(note, period):
    if (period + note) > 11:
        return (period + note) - 12
    return period + note

def major(note):
    return {
        1: note,
        2: sumNote(note, tom),
        3: sumNote(note, tom + tom),
        4: sumNote(note, tom + tom + semitom),
        5: sumNote(note, tom + tom + semitom + tom),
        6: sumNote(note, tom + tom + semitom + tom + tom),
        7: sumNote(note, tom + tom + semitom + tom + tom + tom),
        8: sumNote(note, tom + tom + semitom + tom + tom + tom + semitom),
    }

def minor(note):
    return {
        1: note,
        2: sumNote(note, tom),
        3: sumNote(note, tom + semitom),
        4: sumNote(note, tom + semitom + tom),
        5: sumNote(note, tom + semitom + tom + tom),
        6: sumNote(note, tom + semitom + tom + tom + semitom),
        7: sumNote(note, tom + semitom + tom + tom + semitom + tom),
        8: sumNote(note, tom + semitom + tom + tom + semitom + tom + tom),
    }

def penta_major(note):
    scale =  major(note)
    scale[4] = 'skip'
    scale[7] = 'skip'
    return scale

def penta_minor(note):
    scale =  minor(note)
    scale[2] = 'skip'
    scale[6] = 'skip'
    return scale

def printScale(type):
    for note in notes:
        scale = {}
        if type == 'major':
            scale = major(note)
        if type == 'minor':
            scale = minor(note)
        if type == 'penta_major':
            scale = penta_major(note)
        if type == 'penta_minor':
            scale = penta_minor(note)

        print('%s %s' % (notes[note], type), end='|')
        for i in scale:
            if scale[i] == 'skip':
                print(' --- ', end='|')
                continue
            print(notes[scale[i]], end='|')
        print()


printScale('major')
printScale('minor')
printScale('penta_major')
printScale('penta_minor')
