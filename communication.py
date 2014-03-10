__author__ = 'furmi'

import sys
import os
DIR_PATH = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(DIR_PATH, "..", "map"))

import objects.clients as client

class Communication():
	def __init__(self):
		print('todo')

	def sendOrderAPI(self, address, order, *arguments):
		"""
		Méthode appelée par l'IA pour envoyer un ordre à travers le protocole
		@param enum de la partie du robot qui est appelée
		@param enum de l'ordre envoyé sur la partie
		@param args suivent l'ordre
		"""
		if (address == 1):
			self.__traitementFlussmittelOthers(order, arguments)
		elif (address == 2):
			self.__traitementFlussmittelAsserv(order, arguments)
		elif (address == 3):
			self.__traitementFlussmittelCam(order, arguments)
		elif (address == 4):
			self.__traitementTibotOthers(order, arguments)
		elif (address == 5):
			self.__traitementTibotAsserv(order, arguments)
		elif (address == 6):
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
		pass

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
		pass

	def __traitementHokuyo(self, order, args):
		"""
		Parse l'ordre envoyé à ADDR_HOKUYO
		"""
		pass