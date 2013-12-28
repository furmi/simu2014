# -*- coding: utf-8 -*-

import sys
import os
DIR_PATH = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(DIR_PATH, "..", "define"))
sys.path.append(os.path.join(DIR_PATH, "..", "engine"))

from define import *
from engine.engineobject import EngineObjectPoly



class Cadeau(EngineObjectPoly):
	def __init__(self,engine,posinit,color):
		EngineObjectPoly.__init__(self,
			engine			= engine,
			colltype		= COLLTYPE_CADEAU,
			posinit			= posinit,
			mass			= MASS_INF,
			color			= color,
			poly_points		= map(lambda p: mm_to_px(*p),[(0,0),(150,0),(150,22),(0,22)])
		)

	def __repr__(self):
		return "Cadeaux %s " % (self.posinit,)
