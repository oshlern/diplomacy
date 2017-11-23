from abc import ABCMeta
from enum import Enum

class City(Object):

	def __init__(self, name, isLand, isSC):
		self.name = name
		self.isLand = isLand
		self.isSC = isSC
		self.neighbors = []
		self.troop = None

class Troop(Object):

	__metaclass__ = ABCMeta

	def __init__(self):
		self.city = None
		self.order = None

	def move(self, destination):
		if self.canMove(destination):
			self.city.troop = None
			destination.troop = self
			self.city = destination


class Order(Object):

	hold = 1
	move = 2
	support = 3
	convoy = 4

	def __init__(self, orderType, source, destination, targetTroop=False):
		self.orderType = orderType
		self.source = source
		self.destination = destination
		self.targetTroop = targetTroop




class Game(Object):

	def __init__(self):
		self.cities = {}
		self.troops = []
		self.generateMap()

	def generateMap(self):
		addCity(City("London", True, True))

	def addCity(self, city, troop=False):
		self.cities[city.name] = city
		if troop:
			city.troop = troop
			troop.city = city
			self.troops.append(troop)

	def connectCities(self, city1, city2):
		self.cities[city1].neighbors.append(self.cities[city2])
		self.cities[city2].neighbors.append(self.cities[city1])





