__author__ = 'furmi'

import sys
import os
DIR_PATH = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(DIR_PATH, "..", "map"))

from .communication import Communication
from .hokuyo import Hokuyo
import threading
from multiprocessing import Process, Pipe
from define import *

class ProcessIA():
	"""
	Classe qui va lancer une IA en subprocess.
	"""
	def __init__(self, liste_robots):
		self.__bigrobot = liste_robots[0]
		self.__minirobot = liste_robots[1]
		self.__robots = liste_robots
		self.__hokuyo = Hokuyo(self.__robots)
		self.__communication = Communication(self.__bigrobot, self.__minirobot, self.__hokuyo)
		#communication de data entre l'IA et le simu
		self.__parent_conn, self.__child_conn = Pipe()
		#TODO lancer l'IA
		self.__process = Process(target=self.__testIa(self.__child_conn), args=(self.__child_conn))
		self.__process.start()
		#on démarre le thread de lecture des données IA renvoyées à travers le pipe
		self.__read_thread = threading.Thread(target=self.__readPipe)
		self.__read_thread.start()
		#on démarre le thread d'écriture des données IA à envoyer à travers le pipe
		self.__write_thread = threading.Thread(target=self.__writePipe)
		self.__write_thread.start()

	def __testIa(self, conn):
		self.__color = self.__bigrobot.getTeam()
		if self.__color == RED:
			conn.send(ADDR_TIBOT_ASSERV,A_GOTO,49,2000,400)
		elif self.__color == YELLOW:
			conn.send(ADDR_TIBOT_ASSERV,A_GOTO,36,1000,800)

	def __writePipe(self):
		"""
		Envoie des données à l'IA à travers le Pipe
		Tourne dans un thread
		"""
		while True:
			data = self.__communication.readOrdersAPI()
			if data != -1:
				self.__parent_conn(data)

	def __readPipe(self):
		"""
		Méthode de lecture des données envoyées par l'IA via le pipe.
		recv est bloquant, donc lancé dans un thread
		"""
		while True:
			self.__parseDataIa(self.__parent_conn.recv())

	def __parseDataIa(self, data):
		"""
		Formate les données IA reçues pour les adapter à la méthode
		sendOrderAPI de Communication
		"""
		self.__communication.sendOrderAPI(data[0],data[1],data[2])