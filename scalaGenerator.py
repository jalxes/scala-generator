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

major = {
    0: 'major',
    1: tom,
    2: tom,
    3: semitom,
    4: tom,
    5: tom,
    6: tom,
    7: semitom
}
minor = {
    0: 'minor',
    1: tom,
    2: semitom,
    3: tom,
    4: tom,
    5: semitom,
    6: tom,
    7: tom
}


def printScale(scale, note):
    x = note
    for i in scale:
        # print(x, end=' ')
        if i == 0:
            print('%s %s' % (notes[x], scale[i]), end='|')
            print(notes[x], end='|')
            continue
        if (x + scale[i]) > 11:
            x = (x + scale[i]) - 12
        else:
            x += scale[i]
        # print(scale[i], end=' ')
        # print(x, end=' ')
        print(notes[x], end='|')
    print()


for note in notes:
    printScale(major, note)
    printScale(minor, note)
