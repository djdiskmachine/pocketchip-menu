import pygame

import sys
import os
import __main__

IS_LINUX = sys.platform[:3] == 'lin'
BASE_DIR = os.path.dirname(__main__.__file__) or '.'
APPS_DIR = os.path.normpath(os.path.join(BASE_DIR, 'apps'))
ASSETS_DIR = os.path.normpath(os.path.join(BASE_DIR, 'assets/ui'))
ICONS_DIR = os.path.normpath(os.path.join(BASE_DIR, 'icons'))
FONT_LATO = os.path.join(ASSETS_DIR, 'Lato-Regular.ttf')

EDGE_PADDING = 10
SPACE_PADDING = 5

class Pages:
    POWER = 1
    APPS = 2
    SETTINGS = 3


def within_bounds(mouse,pos,area):
    in_bounds = pos[0]+area[0]>mouse[0]>pos[0] and pos[1]+area[1]>mouse[1]>pos[1]
    return in_bounds

def assetpath(filename, path=ASSETS_DIR):
    return os.path.join(path, filename)

def iconpath(filename):
    return assetpath(filename, path=ICONS_DIR)
