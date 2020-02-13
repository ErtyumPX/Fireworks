import pygame
from random import randint, choice, uniform
from math import floor

pygame.init()

gravity = 0.02

class Firework():
	def __init__(self, x, y, typ, color = (255,255,255)):
		self.x = x
		self.y = y
		self.color = color
		self.velY = uniform(-4.5, -2)
		self.acc = 0
		self.typ = typ

	def Move(self):
		self.acc += gravity
		self.velY += gravity
		if(self.velY > 0):
			self.Pop()
		else:
			self.y += self.velY

	def Pop(self):
		fireworks.remove(self)
		for i in range(randint(40,50)):
			flame = Flame(self.x, self.y, self.typ, self.color)
			flames.append(flame)

	def Show(self):
		pygame.draw.line(surface, self.color, (self.x,self.y), (self.x, self.y-5*self.velY), 3)

class Flame():
	def __init__(self, x, y, typ, color):
		self.x = x
		self.y = y
		#self.thickness = randint(6,12)
		self.thickness = randint(4,8)
		self.acc = 0
		#self.velX = uniform(-3, 3) 
		#self.velY = uniform(-2, 4)
		self.velX = choice([-3,-2,-1,1,2,3])
		self.velY = randint(-3, 6)
		self.color = color
		self.length = randint(10,20)  # 10-20
		self.line = [(x, y)]

		self.decreaseRate = randint(4,10)
		self.frame = 0

		self.typ = typ

	def Move(self):
		self.acc += (gravity * self.typ)
		self.velY += self.acc
		if(len(self.line) < self.length):
			self.line.insert(0, (self.line[0][0] + floor(self.velX), self.line[0][1] + floor(self.velY)))
		else:
			for i in range(len(self.line)-1, 0, -1):
				self.line[i] = self.line[i - 1]
			self.line[0] = (self.line[0][0] + floor(self.velX), self.line[0][1] + floor(self.velY))
		if(self.line[-1][1] > windowY):
			flames.remove(self)
		self.frame += 1
		if(self.frame % self. decreaseRate == 0):
			self.thickness -= 1
		if(self.thickness < 1 and self in flames):
			flames.remove(self)

	def Show(self):
		for pixel in self.line:
			#pygame.draw.line(surface, self.color, pixel, pixel, self.thickness)
			pygame.draw.rect(surface, self.color, (pixel[0], pixel[1], self.thickness, self.thickness))

fireworks = []
flames = []

clock = pygame.time.Clock()
windowX = 400
windowY = 500
surface = pygame.display.set_mode((windowX, windowY))
pygame.display.set_caption('Firework')
pygame.time.set_timer(pygame.USEREVENT, 750)

main = True
while(main):
	clock.tick(120)
	surface.fill(0)
	EVENTS = pygame.event.get()
	for event in EVENTS:
		if(event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE):
			fireWork = Firework(randint(25,windowX-25), randint(windowY-25,windowY-10), choice([0,0.5]),  (randint(0,255),randint(0,255),randint(0,255)))
			fireworks.append(fireWork)
		elif(event.type == pygame.USEREVENT):
			fireWork = Firework( randint(25, windowX-25), randint(windowY-25, windowY-10), choice([0,0.5]), (randint(0,255),randint(0,255),randint(0,255)))
			#fireWork = Firework(randint(25,windowX-25), randint(windowY-25,windowY-10), (255,255,0))
			fireworks.append(fireWork)
		elif(event.type == pygame.QUIT):
			main = False

	for flame in flames:
		flame.Move()
		flame.Show()
	for fire in fireworks:
		fire.Move()
		fire.Show()

	pygame.display.update()

pygame.quit()