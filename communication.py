__author__ = 'furmi'

import sys
import os
DIR_PATH = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(DIR_PATH, "..", "map"))

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
		print('todo')

	def readOrdersAPI(self, address = 'all'):
		print('todo')

