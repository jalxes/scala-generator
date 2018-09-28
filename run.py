#!/usr/bin/env python

from staticjinja import Site
import common
from guitarTunning import get_guitar
from scalaGenerator import get_scale, get_all_scales

guitarContext = {
    "strings": get_guitar(),
    "notes": common.notes,
    "scale": get_scale('major', common.get_note('C'))
}

scaleContext = {
    "notes": common.notes,
    "allScales": {
        "major": [get_scale('major', common.get_note(note)) for note in common.notes],
        "minor": [get_scale('minor', common.get_note(note)) for note in common.notes]
    }
}

site = Site.make_site(
    contexts=[
        ('guitar.html', guitarContext),
        ('pure_scale.html', scaleContext)
    ],
    outpath='./rendered'
)

site.render()
