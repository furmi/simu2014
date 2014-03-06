# -*- coding: utf-8 -*-

__author__ = 'furmi'

import time
import sys
import os
DIR_PATH = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(DIR_PATH, "..", "define"))
sys.path.append(os.path.join(DIR_PATH, "..", "engine"))

class Hokuyo:
	"""
	Emule le comportement de l'hokuyo.
	Permet de répondre aux ordres envoyés à travers le protocole.
	"""
	def __init__(self, robots):
		self.robots = robots
		self.__last_time_stamp = 0
		#return le nombre de millisecondes depuis le temps d'origine
		self.__get_milli = lambda: int(round(time.time() * 1000))

	def ping(self):
		return 'pong'

	def adresse (self):
		#todo adresse via l'enum
		return 6

	def start(self):
		"""
		Set du premier timestamp quand le match a démarré
		"""
		self.__last_time_stamp = self.__get_milli()

	def getHokuyo(self):
		"""
		Renvoie la position de tous les robots
		@return int temps entre 2 envoie de données
		@return int position x de notre gros robot
		@return int position y de notre gros robot
		@return int position x de notre petit robot
		@return int position y de notre petit robot
		@return int position x du gros robot ennemi
		@return int position y du gros robot ennemi
		@return int position x du petit robot ennemi
		@return int position y du petit robot ennemi
		"""
		return self.__getTimeStamp(), \
			   self.robots[0].x(), self.robots[0].y(), \
			   self.robots[1].x(), self.robots[1].y(), \
			   self.robots[2].x(), self.robots[2].y(), \
			   self.robots[3].x(), self.robots[3].y()

	def __getTimeStamp(self):
		current_time = self.__get_milli()
		diff_time = current_time - self.__last_time_stamp
		self.__last_time_stamp = current_time
		return diff_time


