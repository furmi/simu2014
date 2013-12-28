# -*- coding: utf-8 -*-

import sys
import os
DIR_PATH = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(DIR_PATH, "..", "define"))
sys.path.append(os.path.join(DIR_PATH, "..", "engine"))

from define import *
from engine.engineobject import EngineObjectCircle



class Bougie(EngineObjectCircle):
	def __init__(self,engine,posinit,color):
		EngineObjectCircle.__init__(self,
			engine			= engine,
			colltype		= COLLTYPE_BOUGIE,
			posinit			= posinit,
			color			= color,
			mass 			= MASS_INF,
			radius			= mm_to_px(40)
		)

	def __repr__(self):
		return "Bougies %s " % (self.posinit,)

	def eteindre(self):
		self.color = "gray"
