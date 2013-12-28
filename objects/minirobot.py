# -*- coding: utf-8 -*-

from pymunk import RotaryLimitJoint, PinJoint
import pymunk
from math import *

from geometry import Vec


from ..define import *
from .robot import Robot, MINI, Others
from ..engine.engineobject import EngineObjectPoly,EngineObjectSegment
from .verre import Verre


class MiniRobot(Robot):
	def __init__(self, *, engine, asserv, others, posinit, team, match):
		Robot.__init__(self,
			engine 				= engine,
			asserv				= asserv,
			asserv_obj 			= None,
			others				= others,
            visio 				= None,
            visio_obj 			= None,
			team				= team,
			posinit				= posinit,
			mass				= 10,
			typerobot			= MINI,
			colltype 			= COLLTYPE_PETIT_ROBOT,
			poly_points			= mm_to_px((0,0),(HEIGHT_MINI,0),(HEIGHT_MINI,WIDTH_MINI),(0,WIDTH_MINI)),
            match 				= match
		)