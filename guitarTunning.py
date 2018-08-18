#!/usr/bin/env python
import common
strings = [
    [
        common.get_note('E'),
        common.get_note('A'),
        common.get_note('D'),
        common.get_note('G'),
        common.get_note('B'),
        common.get_note('E')
    ]
]
for i in range(1, 18):
    nextString = []
    for note in strings[i-1]:
        nextString.append(common.add_note(note, common.semitom))
    strings.append(nextString)

# for string in strings:
#     for k in string:
#         print(common.notes[k], end=' -- ')
#     print()


def get_guitar():
    return strings
