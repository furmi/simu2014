# -*- coding: utf-8 -*-

import sys
import os
DIR_PATH = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(DIR_PATH, "..", "define"))
sys.path.append(os.path.join(DIR_PATH, "..", "engine"))

from define import *
from engine.engineobject import EngineObjectCircle



class Gateau(EngineObjectCircle):
	def __init__(self,engine,posinit):
		EngineObjectCircle.__init__(self,
			engine			= engine,
			colltype		= COLLTYPE_WALL,
			posinit			= posinit,
			mass			= MASS_INF,
			color			=  "white",
			radius			= mm_to_px(200)
		)

	def __repr__(self):
		return "wall gateau"