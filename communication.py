__author__ = 'furmi'

import sys
import os
DIR_PATH = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(DIR_PATH, "..", "map"))

#pour importer les constantes des ordres et des robots
from define import *

from collections import deque
import time


class Communication():
	def __init__(self, bigrobot, minirobot, hokuyo):
		self.__bigrobot = bigrobot	#objet robot, afin d'envoyer les ordres
		self.__minirobot = minirobot	#objet robot, afin d'envoyer les ordres
		self.__orders_to_return = deque()	#structure de donnée contenant les ordres à renvoyer via readOrdersApi
		self.__hokuyo = hokuyo #objet de type Hokuyo

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
		#if address == 'all':
		if (len(self.__orders_to_return) != 0):
			order = self.__orders_to_return.popleft()
		else:
			order = None
		if order is not None:
			print(order)
			return order[0], order[1], order[2]
		else:
			return -1

	def __traitementFlussmittelOthers(self, order, args):
		"""
		Parse l'ordre envoyé à ADDR_FLUSSMITTEL_OTHER
		"""
		pass

	def __traitementFlussmittelAsserv(self, order, args):
		"""
		Parse l'ordre envoyé à ADDR_FLUSSMITTEL_ASSERV
		"""
		#on traite les ordres qui nécessitent de renvoyer des informations
		if (order == A_GET_POS):
			pos = self.__bigrobot.getPosition()
			self.__orders_to_return.append((ADDR_FLUSSMITTEL_ASSERV, order, pos))
		elif (order == A_GET_POS_ID):
			pos = self.__bigrobot.getPosition()
			pos_id = pos[0], pos[1], pos[2], args[0]
			self.__orders_to_return.append((ADDR_FLUSSMITTEL_ASSERV, order, pos_id))
		else:
			#on ajoute l'ordre reçu à la structure de renvoie
			self.__orders_to_return.append((ADDR_FLUSSMITTEL_OTHER, order, args))
			if (order == PINGPING):
				self.__bigrobot.ping()
			elif (order == A_GOTOA):
				self.__bigrobot.addGoalOrder(GOTOA, args[1], args[2], args[3])
			elif (order == A_GOTO):
				self.__bigrobot.addGoalOrder(GOTO, args[1], args[2])
			elif (order == A_GOTOAR):
				self.__bigrobot.addGoalOrder(GOTOAR, args[1], args[2], args[3])
			elif (order == A_GOTOR):
				self.__bigrobot.addGoalOrder(GOTOR, args[1], args[2])
			elif (order == A_ROT):
				self.__bigrobot.addGoalOrder(ROT, args[1])
			elif (order == A_ROTR):
				self.__bigrobot.addGoalOrder(ROTR, args[1])
			elif (order == A_CLEANG):
				self.__bigrobot.cleanGoals()
			elif (order == A_PWM):
				self.__bigrobot.addGoalOrder(PWM, args[1], args[2], args[3])
			else:
				print('Error : mauvais paramètre traitement Flussmittel asserv !')

	def __traitementFlussmittelCam(self, order, args):
		"""
		Parse l'ordre envoyé à ADDR_FLUSSMITTEL_CAM
		"""
		positions_bots = self.__hokuyo.getHokuyo()
		#if (order == GET_HOKUYO):



	def __traitementTibotOthers(self, order, args):
		"""
		Parse l'ordre envoyé à ADDR_TIBOT_OTHER
		"""
		pass

	def __traitementTibotAsserv(self, order, args):
		"""
		Parse l'ordre envoyé à ADDR_TIBOT_ASSERV
		"""
		#on traite les ordres qui nécessitent de renvoyer des informations
		if (order == A_GET_POS):
			pos = self.__minirobot.getPosition()
			self.__orders_to_return.append((ADDR_TIBOT_ASSERV, order, pos))
		elif (order == A_GET_POS_ID):
			pos = self.__minirobot.getPosition()
			pos_id = pos[0], pos[1], pos[2], args[0]
			self.__orders_to_return.append((ADDR_TIBOT_ASSERV, order, pos_id))
		else:
			if (order == PINGPING):
				self.__minirobot.ping()
			elif (order == A_GOTOA):
				self.__minirobot.addGoalOrder(GOTOA, args[1], args[2], args[3])
			elif (order == A_GOTO):
				self.__minirobot.addGoalOrder(GOTO, args[1], args[2])
			elif (order == A_GOTOAR):
				self.__minirobot.addGoalOrder(GOTOAR, args[1], args[2], args[3])
			elif (order == A_GOTOR):
				self.__minirobot.addGoalOrder(GOTOR, args[1], args[2])
			elif (order == A_ROT):
				self.__minirobot.addGoalOrder(ROT, args[1])
			elif (order == A_ROTR):
				self.__minirobot.addGoalOrder(ROTR, args[1])
			elif (order == A_CLEANG):
				self.__minirobot.cleanGoals()
			elif (order == A_PWM):
				self.__minirobot.addGoalOrder(PWM, args[1], args[2], args[3])
			else:
				print('Error : mauvais paramètre traitement Flussmittel asserv !')

	def __traitementHokuyo(self, order, args):
		"""
		Parse l'ordre envoyé à ADDR_HOKUYO
		"""
		if(order == GET_HOKUYO):
			data = tuple(self.__hokuyo.getHokuyo())
			data_to_ret = (args[0],)
			data_to_ret += data
			self.__orders_to_return.append((ADDR_HOKUYO, order, data_to_ret))

	def testCom(self):
		print('testCom')
		self.sendOrderAPI(ADDR_TIBOT_ASSERV,A_GOTO,49,2000,400)
		print('order 0', self.readOrdersAPI())
		time.sleep(1)
		self.sendOrderAPI(ADDR_FLUSSMITTEL_ASSERV,A_GOTO,50,180,500)
		print('order 1', self.readOrdersAPI())
		self.sendOrderAPI(ADDR_FLUSSMITTEL_ASSERV,A_GOTO,51,1200,1500)
		print('order 2', self.readOrdersAPI())
		self.sendOrderAPI(ADDR_FLUSSMITTEL_ASSERV,A_GOTO,52,2000,1500)
		print('order 3', self.readOrdersAPI())
		self.sendOrderAPI(ADDR_FLUSSMITTEL_ASSERV,A_GET_POS,35)
		print('order 4', self.readOrdersAPI())
		self.sendOrderAPI(ADDR_FLUSSMITTEL_ASSERV,A_GET_POS_ID,36)
		print('order 5', self.readOrdersAPI())
		#time.sleep(5)
		self.sendOrderAPI(ADDR_HOKUYO,GET_HOKUYO,123)
		print('order 6', self.readOrdersAPI())
