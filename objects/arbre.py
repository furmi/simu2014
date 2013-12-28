# -*- coding: utf-8 -*-

import sys
import os
DIR_PATH = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(DIR_PATH, "..", "define"))
sys.path.append(os.path.join(DIR_PATH, "..", "engine"))

from define import *
from engine.engineobject import EngineObjectCircle



class Arbre(EngineObjectCircle):
	def __init__(self,engine,posinit):
		EngineObjectCircle.__init__(self,
			engine			= engine,
			colltype		= COLLTYPE_ARBRE,
			posinit			= posinit,
			color			= "green",
			mass 			= MASS_INF,
			radius			= mm_to_px(150)
		)

	def __repr__(self):
		return "Arbre %s " % (self.posinit,)
