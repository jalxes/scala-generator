#!/usr/bin/env python

from common import add_note, tom, semitom


def major(note):
    return [
        note,
        add_note(note, tom),
        add_note(note, tom + tom),
        add_note(note, tom + tom + semitom),
        add_note(note, tom + tom + semitom + tom),
        add_note(note, tom + tom + semitom + tom + tom),
        add_note(note, tom + tom + semitom + tom + tom + tom),
        add_note(note, tom + tom + semitom + tom + tom + tom + semitom),
    ]


def pentaMajor(note):
    scale = major(note)
    return [
        scale[1 - 1],
        scale[2 - 1],
        scale[3 - 1],
        scale[5 - 1],
        scale[6 - 1],
        scale[8 - 1],
    ]


def bluesMajor(note):
    scale = major(note)
    return [

        scale[1 - 1],
        scale[2 - 1],
        add_note(scale[2 - 1], semitom),
        scale[3 - 1],
        scale[5 - 1],
        scale[6 - 1],
        scale[8 - 1],
    ]


def minor(note):
    return [
        note,
        add_note(note, tom),
        add_note(note, tom + semitom),
        add_note(note, tom + semitom + tom),
        add_note(note, tom + semitom + tom + tom),
        add_note(note, tom + semitom + tom + tom + semitom),
        add_note(note, tom + semitom + tom + tom + semitom + tom),
        add_note(note, tom + semitom + tom + tom + semitom + tom + tom),
    ]


def pentaMinor(note):
    scale = minor(note)
    return [
        scale[1 - 1],
        scale[3 - 1],
        scale[4 - 1],
        scale[5 - 1],
        scale[7 - 1],
        scale[8 - 1],
    ]


def bluesMinor(note):
    scale = minor(note)
    return [
        scale[1 - 1],
        scale[3 - 1],
        scale[4 - 1],
        add_note(scale[4 - 1], semitom),
        scale[5 - 1],
        scale[7 - 1],
        scale[8 - 1],
    ]


def get_scale(scale, note):
    if 'major' == scale:
        return major(note)
    if 'minor' == scale:
        return minor(note)
    if 'pentaMajor' == scale:
        return pentaMajor(note)
    if 'pentaMinor' == scale:
        return pentaMinor(note)
    if 'bluesMajor' == scale:
        return bluesMajor(note)
    if 'bluesMinor' == scale:
        return bluesMinor(note)


def get_all_scales(note):
    return {
        'major': major(note),
        'minor': minor(note),
        'pentaMajor': pentaMajor(note),
        'pentaMinor': pentaMinor(note),
        'bluesMajor': bluesMajor(note),
        'bluesMinor': bluesMinor(note),
    }
