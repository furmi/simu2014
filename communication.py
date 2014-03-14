__author__ = 'furmi'

import sys
import os
DIR_PATH = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(DIR_PATH, "..", "map"))

#pour importer les constantes des ordres et des robots
from define import *


class Communication():
	def __init__(self, bigrobot, minirobot):
		self.__bigrobot = bigrobot	#objet robot, afin d'envoyer les ordres
		self.__minirobot = minirobot	#objet robot, afin d'envoyer les ordres

	def sendOrderAPI(self, address, order, *arguments):
		"""
		Méthode appelée par l'IA pour envoyer un ordre à travers le protocole
		@param enum de la partie du robot qui est appelée
		@param enum de l'ordre envoyé sur la partie
		@param args suivent l'ordre
		"""
		if (address == ADDR_FLUSSMITTEL_OTHER):
			self.__traitementFlussmittelOthers(order, arguments)
		elif (address == ADDR_FLUSSMITTEL_ASSERV):
			self.__traitementFlussmittelAsserv(order, arguments)
		elif (address == ADDR_FLUSSMITTEL_CAM):
			self.__traitementFlussmittelCam(order, arguments)
		elif (address == ADDR_TIBOT_OTHER):
			self.__traitementTibotOthers(order, arguments)
		elif (address == ADDR_TIBOT_ASSERV):
			self.__traitementTibotAsserv(order, arguments)
		elif (address == ADDR_HOKUYO):
			self.__traitementHokuyo(order, arguments)
		else:
			print('ordre non valide')

	def readOrdersAPI(self, address = 'all'):
		"""
		Méthode appelée par l'IA pour vérifier les ordres en attente
		"""
		pass

	def __traitementFlussmittelOthers(self, order, args):
		"""
		Parse l'ordre envoyé à ADDR_FLUSSMITTEL_OTHER
		"""
		pass

	def __traitementFlussmittelAsserv(self, order, args):
		"""
		Parse l'ordre envoyé à ADDR_FLUSSMITTEL_ASSERV
		"""
		print(args)
		if (order == PINGPING):
			self.__bigrobot.ping()
		elif (order == A_GOTOA):
			self.__bigrobot.addGoalOrder(GOTOA, args(1), args(2), args(3))
		elif (order == A_GOTO):
			self.__bigrobot.addGoalOrder(GOTO, args[1], args[2])
		elif (order == A_GOTOAR):
			self.__bigrobot.addGoalOrder(GOTOAR, args(1), args(2), args(3))
		elif (order == A_GOTOR):
			self.__bigrobot.addGoalOrder(GOTOR, args(1), args(2))
		elif (order == A_ROT):
			self.__bigrobot.addGoalOrder(ROT, args(1))
		elif (order == A_ROTR):
			self.__bigrobot.addGoalOrder(ROTR, args(1))
		elif (order == A_CLEANG):
			self.__bigrobot.cleanGoals()
		elif (order == A_PWM):
			self.__bigrobot.addGoalOrder(PWM, args(1), args(2), args(3))

	def __traitementFlussmittelCam(self, order, args):
		"""
		Parse l'ordre envoyé à ADDR_FLUSSMITTEL_CAM
		"""
		pass

	def __traitementTibotOthers(self, order, args):
		"""
		Parse l'ordre envoyé à ADDR_TIBOT_OTHER
		"""
		pass

	def __traitementTibotAsserv(self, order, args):
		"""
		Parse l'ordre envoyé à ADDR_TIBOT_ASSERV
		"""
		if (order == PINGPING):
			self.__minirobot.ping()
		elif (order == A_GOTOA):
			self.__minirobot.addGoalOrder(GOTOA, args(1), args(2), args(3))
		elif (order == A_GOTO):
			self.__minirobot.addGoalOrder(GOTO, args[1], args[2])
		elif (order == A_GOTOAR):
			self.__minirobot.addGoalOrder(GOTOAR, args(1), args(2), args(3))
		elif (order == A_GOTOR):
			self.__minirobot.addGoalOrder(GOTOR, args(1), args(2))
		elif (order == A_ROT):
			self.__minirobot.addGoalOrder(ROT, args(1))
		elif (order == A_ROTR):
			self.__minirobot.addGoalOrder(ROTR, args(1))
		elif (order == A_CLEANG):
			self.__minirobot.cleanGoals()
		elif (order == A_PWM):
			self.__minirobot.addGoalOrder(PWM, args(1), args(2), args(3))

	def __traitementHokuyo(self, order, args):
		"""
		Parse l'ordre envoyé à ADDR_HOKUYO
		"""
		pass

	def testCom(self):
		print('testCom')
		self.sendOrderAPI(ADDR_FLUSSMITTEL_ASSERV,A_GOTO,50,1500,1000)