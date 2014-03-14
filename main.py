#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Simulateur permettant de simuler un match d'eurobot.

Déplacer gros robot: clic gauche
Déplacer petit robot: clic droit

Déplacer adversaire: idem + ctrl

@author Thomas Recouvreux
@author Pierre-Henry Fricot
@author Cédric Bache

Pour la version 2013, nous avons utilisé le nouveau protocole de communication zérobot. Les objets et engines sont également réécrit pour adapter au nouveau reglement.
@author Siqi LIU <me@siqi.fr>
@author Florent Thévenet <florent@fthevenet.fr>
@author Thomas Fuhrmann <tomesman@gmail.com>

"""

#test de modif
#test modif fixe

import sys
import os
DIR_PATH = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(DIR_PATH, "..", "map"))


import optparse
import threading
import time

from engine import *
import match
from map import maploader
from objects import bigrobot, minirobot
import communication



if __name__ == "__main__":

		default = {}
		default["server_ip"]            = "localhost"
		default["port_frontend"]        = 5000
		default["port_backend"]         = 5001
		default["port_ev_push"]         = 5003
		default["port_ev_sub"]          = 5004

		usage = "usage: %prog [options]"
		parser = optparse.OptionParser(usage,version="%prog 0.0")
		parser.add_option("-S", "--server-ip",
						  action="store", dest="server_ip", default=default["server_ip"],
						  help="ip zerobot server")
		parser.add_option("-b", "--port-backend",
						  action="store", dest="port_backend", type="int", default=default["port_backend"],
						  help="port backend")
		parser.add_option("-f", "--port-frontend",
						  action="store", dest="port_frontend", type="int", default=default["port_frontend"],
						  help="port frontend")
		parser.add_option("-p", "--port-ev-push",
						  action="store", dest="port_ev_push", type="int", default=default["port_ev_push"],
						  help="port events publishing")
		parser.add_option("-s", "--port-ev-sub",
						  action="store", dest="port_ev_sub", type="int", default=default["port_ev_sub"],
						  help="port events subscribtion")
		(options, args) = parser.parse_args()


		engine = Engine()
		match = match.Match()

		# robots
		bigbot = bigrobot.BigRobot(engine = engine,
							posinit = mm_to_px(180, 400),
							team = RED)
		minibot = minirobot.MiniRobot(engine = engine,
							  posinit = mm_to_px(70, 570),
							  team = RED)
		bigbot2 = bigrobot.BigRobot(engine = engine,
							 posinit = mm_to_px(3000-180,170),
							 team = YELLOW)
		minibot2 = minirobot.MiniRobot(engine = engine,
							   posinit = mm_to_px(3000-100,690),
							   team = YELLOW)
		robots = (bigbot, minibot, bigbot2, minibot2)

		#instance de l'objet communication
		com = communication.Communication(bigbot, minibot)

		# hkuyo
		#hokuyo = services.create(utcoupe.HOKUYO, Hokuyo(robots))

		#bigrobot.init(engine)
		"""minirobot.init(engine)
		bigrobot2.init(engine)
		minirobot2.init(engine)"""

		maploader.load_map("map/map.xml",engine)

		engine.add(bigbot)
		#engine.add(minibot)
		engine.add(bigbot2)
		engine.add(minibot2)

		t=threading.Thread(target=engine.start)
		t.setDaemon(True)
		t.start()

		while not engine.e_stop.is_set():
				try:
						engine.e_stop.wait(3)
						print("dans la boucle")
				except KeyboardInterrupt:
						engine.stop()
						break



