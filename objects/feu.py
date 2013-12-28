__author__ = 'furmi'

# -*- coding: utf-8 -*-

import sys
import os
DIR_PATH = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(DIR_PATH, "..", "define"))
sys.path.append(os.path.join(DIR_PATH, "..", "engine"))

from define import *
from engine.engineobject import EngineObjectPoly

class Feu(EngineObjectPoly):
	def __init__(self,engine,posinit, orientation):
		if (orientation == "vert"):
			points = map(lambda p: mm_to_px(*p),[(0,0),(30,0),(30,140),(0,140)])
		else:
			points = map(lambda p: mm_to_px(*p),[(0,0),(140,0),(140,30),(0,30)])
		EngineObjectPoly.__init__(self,
			engine			= engine,
			colltype		= COLLTYPE_FEU,
			posinit			= posinit,
			mass			= MASS_INF,
			poly_points		= points
		)

	def eteindre(self):
		#à modifier, ça ne modifie pas l'objet graphique...
		self.poly_points = map(lambda p: mm_to_px(*p),[(0,0),(140,0),(140,85)])
		self.color = "red"

	def __repr__(self):
		return "Feu %s " % (self.posinit,)

