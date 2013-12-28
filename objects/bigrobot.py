# -*- coding: utf-8 -*-

import math
import time
import random

from geometry import Vec,Segment

from .robot import Robot, BIG, Others, Visio
from ..define import *
from ..engine.engineobject import EngineObjectPoly
from .bougie import Bougie
from .cerise import Cerise
from .ping_pong import Ping_pong

class BigRobot(Robot):
	def __init__(self, *, engine, asserv, others, visio, posinit, team, match):
		self.bras_milieu = EngineObjectPoly(
			engine 		= engine,
			colltype	= COLLTYPE_BRAS,
			offset		= mm_to_px(4, -154),
			color		= "purple",
			poly_points = map(lambda p: mm_to_px(*p),[(0,0),(20,0),(20,-215),(0,-215)]), #taille du bras
			is_extension= True
		)

		self.bras_gauche = EngineObjectPoly(
			engine 		= engine,
			colltype	= COLLTYPE_BRAS,
			offset		= mm_to_px(-41, -154),
			color		= "purple",
			poly_points = map(lambda p: mm_to_px(*p),[(0,0),(20,0),(20,-100),(0,-100)]), #taille du bras
			is_extension= True
		)

		self.bras_droit = EngineObjectPoly(
			engine 		= engine,
			colltype	= COLLTYPE_BRAS,
			offset		= mm_to_px(54, -154),
			color		= "purple",
			poly_points = map(lambda p: mm_to_px(*p),[(0,0),(20,0),(20,-100),(0,-100)]), #taille du bras
			is_extension= True
		)

		Robot.__init__(self,
			engine		 		= engine,
			asserv		= asserv,
                        asserv_obj = None,
			others		= others,
                        others_obj = BigOthers(self),
			team				= team,
			posinit				= posinit,
			mass				= 10,
			typerobot			= BIG,
			colltype 			= COLLTYPE_GROS_ROBOT,
			poly_points			= mm_to_px((0,0),(HEIGHT_GROS,0),(HEIGHT_GROS,WIDTH_GROS),(0,WIDTH_GROS)),
			extension_objects	= [],
                        match = match
		)

class BigOthers(Others):
	pass
