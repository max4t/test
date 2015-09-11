from reader import get as accidents


class Row:

	def __init__(self, accident, place, car, user):
		self.lights = accident.lum
		self.city_size = accident.agg
		self.intersec = accident.int
		self.weather = accident.atm
		self.road = place.catr
		self.way = place.circ
		self.profile = place.prof
		self.curve = place.plan
		self.condition = place.surf
		self.infras = place.infra
		self.car = car.catv
		self.maneuver = car.manv
		if user.an_nais == -1:
			raise ValueError("wrong year")
		self.age = 2014 - user.an_nais
		self.gender = user.sexe
		self.pos = user.place
		self.loc = user.locp

		self.result = user.grav

	def X(self):
		return [
			self.lights, \
			self.city_size, \
			self.intersec, \
			self.weather, \
			self.road, \
			self.way, \
			self.profile, \
			self.curve, \
			self.condition, \
			self.infras, \
			self.car, \
			self.maneuver, \
			self.age, \
			self.gender, \
			self.pos, \
			self.loc
		]

	def y(self):
		return self.result


entries = []
for key in accidents():
	if len(accidents()[key].places) != 1:
		continue
	acc = accidents()[key]
	place = acc.places[next(iter(acc.places))]
	for car_key in place.cars:
		car = place.cars[car_key]
		for user in car.users:
			try:
				entries.append(Row(acc, place, car, user))
			except ValueError:
				pass

X = [([1] + row.X()) for row in entries]
y = [[row.y()] for row in entries]




