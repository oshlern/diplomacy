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


	def __init__(self, orderType, location, source, destination):
		self.orderType = orderType
		self.location = location
		self.source = source
		self.destination = destination

location
	location.troop ?= 0, 1, 2 #None, armyType, fleetType
	location.order ?= None
	location.isLand, location.isCoast, location.neighbors = [locations]
	location.isReachable(destination)

Map = [location1, location2]
moves = {}
convoyLocations = []

def addPower(destination, source, negative=False):
	if negative:
		modifier = -1
	else:
		modifier = 1
	if destination in moves:
		if source in moves[destination]:
			moves[destination][source][0] += modifier
		else:
			moves[destination][source] = (modifier, [])
	else:
		moves[destination] = {source: (modifier, [])}

def addConvoy(destination, source, location):
	if destination in moves:
		if source in moves[destination]:
			moves[destination][source][1].append(location)
		else:
			moves[destination][source] = (0, [location])
	else:
		moves[destination] = {source: (0, [location])}

def canSupport(order):
	assert order.orderType == supportType
	if order.source.troop:
		if order.source.order.orderType == moveType and order.source.order.destination == order.destination:
			if order.location.isReachable(order.destination):
				return True
	return False

def canConvoy(order):
	assert order.orderType == convoyType
	if order.source.troop == armyType:
		if order.source.order.orderType == moveType and order.source.order.destination == order.destination:
			if order.source.isCoast and order.destination.isCoast:
				return True
	return False

for order in orders:
	if order.orderType == supportType:
		if canSupport(order):
			addPower(order.destination, order.source)
	elif order.orderType == moveType:
		if order.destination != order.source:
			if order.destination.troop:
				s_order = order.destination.order
				if s_order.orderType == supportType and s_order.destination != order.location:
					if canSupport(s_order):
						addPower(s_order.destination, s_order.source, negative=True)
		addPower(order.destination, order.source)
	elif order.orderType == convoyType:
		if canConvoy(order):
			addConvoy(order.destination, order.source, order.location)
			convoyLocations.append(order.location)

loop over orders
	if support, add 1 power to move in list of moves (supported destination must be reachable by supporting unit)
	if move, if unto a supporting order, remove 1 power from (supported) move in list of moves unless the target of the support is the moving piece
		add 1 power to move in list of moves and set is_executed to True
	if convoy
		add self to dictionary of convoys indexed by move
loop over moves with destination that are convoying
	greatest power = 0
	greatest source = None
	loop over sources
		if move is executed
		and if move is not possible via land route, check if convoys allow it
			if greater than greatest power
				set greatest power and greatest source
	if source != destination
		remove convoy from list of convoys
loop over other moves
	greatest power = 0
	greatest source = None
	loop over sources
		if move is executed
		and if move is not possible via land route, check if convoys allow it
			if greater than greatest power
				set greatest power and greatest source 

	

moves = {destination: {source: (power, [convoy1, convoy2]), source2: (power2, [convoy3, convoy4])}}



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





