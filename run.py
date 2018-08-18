#!/usr/bin/env python

from staticjinja import Site
import common
from guitarTunning import get_guitar
from scalaGenerator import get_scale, get_all_scales

guitarContext = {
    "strings": get_guitar(),
    "notes": common.notes,
    "scale": get_scale('bluesMinor', common.get_note('A'))
}

scaleContext = {
    "notes": common.notes,
    "scales": [get_all_scales(common.get_note(note)) for note in common.notes]
}

site = Site.make_site(
    contexts=[
        ('guitar.html', guitarContext),
        ('pure_scale.html', scaleContext)
    ],
    outpath='./rendered'
)

site.render()
