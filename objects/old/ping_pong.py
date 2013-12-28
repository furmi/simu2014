# -*- coding: utf-8 -*-

import sys
import os
DIR_PATH = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(DIR_PATH, "..", "define"))
sys.path.append(os.path.join(DIR_PATH, "..", "engine"))

from define import *
from engine.engineobject import EngineObjectCircle


class Ping_pong(EngineObjectCircle):
	def __init__(self,engine,posinit, team):
		EngineObjectCircle.__init__(self,
			engine			= engine,
			colltype		= COLLTYPE_DEFAULT,
			posinit			= posinit,
			color 			= "orange" if team == RED else "green",
			mass 			= 800,
			radius			= mm_to_px(11)
		)

	def __repr__(self):
		return "pingpong %s" % (self.posinit)
