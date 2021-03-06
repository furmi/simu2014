# -*- coding: utf-8 -*-


import random
import math
import time
import sys
import os
DIR_PATH = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(DIR_PATH, "..", "define"))
sys.path.append(os.path.join(DIR_PATH, "..", "engine"))

from define import *
from engine.engineobject import EngineObjectPoly
from .clients import *

class Robot(EngineObjectPoly):
	def __init__(self, *, engine, team, posinit, mass, poly_points,
				 typerobot, extension_objects=[], colltype):
		color = 'yellow' if team == YELLOW else 'red'
		EngineObjectPoly.__init__(self,
			engine		 	= engine,
			mass			= mass,
			posinit			= posinit,
			color			= color,
			colltype		= colltype, 
			poly_points		= poly_points,
			extension_objects	= extension_objects
		)

	#données d'état du robot
		self.__typerobot = typerobot
		self.__team = team
		self.__goals = []
		self.__asserv = Asserv(self)
		self.__others = Others(self)

	#données du robot utiles au simulateur
		self.__mod_teleport = False # quand on clique ça téléporte au lieu d'envoyer un ordre à l'asservissement
		self.__mod_recul = False # marche arrière ou marche avant ?
		self.__max_speed = 1000 # vitesse maximale (quand pwm=255)
		self.__stop = False

		#utilité ?
		self.__current_team = RED
		self.__current_robot = BIG

		self.body._set_velocity_func(self._my_velocity_func())

	def init(self, engine):
		self.__engine = engine

	def x(self):
		return px_to_mm(self.body.position[0])
	
	def y(self):
		return px_to_mm(self.body.position[1])
	
	def a(self):
		return int(math.degrees(self.body.angle))

	def getPosition(self):
		return self.x(), self.y(), self.a()

	def getTyperobot(self):
		return self.__typerobot

	def getTeam(self):
		return self.__team

	def addGoal(self, newGoal):
		self.__goals.append(newGoal)
		print (self.__goals)

	def cleanGoals(self):
		self.__goals = []

	def setStop(self, value):
		self.__stop = value

	def addGoalOrder(self, numOrdre, x = None, y = None, angle = None):
		"""
		Méthode appelée depuis communication pour ajouter un goal au robot
		@param numOrdre int définit dans define
		"""
		if (numOrdre == GOTO):
			self.__asserv.goto(x,y)
		elif (numOrdre == GOTOA):
			self.__asserv.gotoa(x,y,angle)
		elif (numOrdre == GOTOAR):
			self.__asserv.gotoar(x,y,angle)
		elif (numOrdre == GOTOR):
			self.__asserv.gotor(x,y)
		elif (numOrdre == ROT):
			self.__asserv.rot(angle)
		elif (numOrdre == ROTR):
			self.__asserv.rotr(angle)
		elif (numOrdre == PWM):
			self.__asserv.pwm(x,y,angle)	#!! x=pwm_l, y=pwm_r, angle=delay !!


	def _my_velocity_func(self):
		def f(body, gravity, damping, dt):
			self.body._set_torque(0)
			self.body._set_angular_velocity(0)
			if not self.__stop and self.__goals:
				current_goal = self.__goals[0]
				if isinstance(current_goal, GoalPOSR):
					x,y = self.body.position
					a = self.body.angle
					cx, cy = current_goal.pos
					dx = cx * math.cos(a) - cy * math.sin(a)
					dy = cx * math.sin(a) + cy * math.cos(a)
					self.__goals[0] = GoalPOS(x+dx, y+dy)
				elif isinstance(current_goal, GoalANGLER):
					a = current_goal.a
					ca = self.body.angle
					self.__goals[0] = GoalANGLE(ca+a)
				elif isinstance(current_goal, GoalPOS):
					gx,gy = current_goal.pos
					v = self.__max_speed / 4
					x,y = self.body.position
					dx = gx - x
					dy = gy - y
					d = math.sqrt(dx**2+dy**2)
					if d < abs(v * dt):
						self.body._set_position((gx,gy))
						self.__goals.pop(0)
						self.body._set_velocity((0,0))
					else:
						a = math.atan2(dy, dx)
						vx = abs(v) * math.cos(a)
						vy = abs(v) * math.sin(a)
						self.body._set_velocity((vx,vy))
						if v < 0:
							a += math.pi
						self.body._set_angle(a)
				elif isinstance(current_goal, GoalPWM):
					if current_goal.start == -1:
						current_goal.start = time.time()
					elif (time.time() - current_goal.start) > current_goal.delay:
						self.__goals.pop(0)
					else:
						a = self.body.angle
						v = self.__max_speed * current_goal.pwm / 255
						vx = v * math.cos(a)
						vy = v * math.sin(a)
						self.body._set_velocity((vx,vy))
				elif isinstance(current_goal, GoalANGLE):
					self.body._set_angle(current_goal.a)
					self.__goals.pop(0)
				else:
					raise Exception("type_goal inconnu")
			else:
				self.body._set_velocity((0,0))
		return f

	def onEvent(self, event):
		# selection des teams et des robots
		if KEYDOWN == event.type:
			if KEY_CHANGE_TEAM == event.key:
				self.__current_team = YELLOW
				print("équipe rouge")
				return True
			elif KEY_CHANGE_ROBOT == event.key:
				self.__current_robot = MINI
				print("control du mini robot")
				return True
			elif KEY_TELEPORTATION == event.key:
				self.__mod_teleport = not self.__mod_teleport
				return True
			elif KEY_RECUL == event.key:
				self.__mod_recul = not self.__mod_recul
			elif KEY_JACK == event.key:
				#todo avertir jack unplugged
				pass
		elif KEYUP == event.type:
			if KEY_CHANGE_TEAM == event.key:
				print("équipe jaune")
				self.__current_team = YELLOW
				return True
			elif KEY_CHANGE_ROBOT == event.key:
				self.__current_robot = BIG
				print("control gros robot")
				return True

		# actions
		if self._event_concerns_me(event):
			# keydown
			if KEYDOWN == event.type:
				if KEY_STOP_RESUME == event.key:
					self.__asserv.stop()
					return True
				elif KEY_CANCEL == event.key:
					self.__asserv.cleang()
					return True
			# keyup
			elif KEYUP == event.type:
				if KEY_STOP_RESUME == event.key:
					self.__asserv.resume()
			# mouse
			elif MOUSEBUTTONDOWN == event.type:
				p = event.pos
				p_mm = px_to_mm(p)
				if self.__mod_teleport:
					#self.extras.teleport(p_mm[0], p_mm[1], 0)
					print ('pass dans le mod teleport')
				else:
					v = mm_to_px(1000) * (-1 if self.__mod_recul else 1)
					#on clean les goals avant d'en envoyer un nouveau afin d'éviter les blocages
					self.cleanGoals()
					self.__asserv.goto(*px_to_mm(p[0],p[1]))
				return True
		return False

	def _event_concerns_me(self, event):
		return self.__current_team == self.__team and self.__typerobot == self.__current_robot
	
	def __repr__(self):
		return "Robot"