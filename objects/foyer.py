# -*- coding: utf-8 -*-

import sys
import os
DIR_PATH = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(DIR_PATH, "..", "define"))
sys.path.append(os.path.join(DIR_PATH, "..", "engine"))

from define import *
from engine.engineobject import EngineObjectCircle



class Foyer(EngineObjectCircle):
	def __init__(self,engine,posinit,type):
		if (type == "centre"):
			self.rad = 150
		else:
			self.rad = 250
		EngineObjectCircle.__init__(self,
			engine			= engine,
			colltype		= COLLTYPE_FOYER,
			posinit			= posinit,
			color			= "brown",
			mass 			= MASS_INF,
			radius			= mm_to_px(self.rad)
		)
		self.nbFeu = 0

	def __repr__(self):
		return "Foyer %s " % (self.posinit,)
