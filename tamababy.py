import pygame
import random
import math
import time
pygame.init()
d_width = 960
d_height = 960
displayResolution = (d_width,d_height)
wn = pygame.display.set_mode(displayResolution)
gameRunning = True

WHITE= (255,255,255)
BLUE= (0,0,255)
RED = (255,0,0)
start_time = time.time()
baddySpeed = 1


class Player:
	def __init__(self, x,y, speed = 10):
		self.x = x
		self.y = y
		self.speed = speed
		self.width = 64
		self.height = 64
		self.sprite = pygame.Surface((self.width,self.height))
		
		
	
	def move(self):
		if pygame.key.get_pressed()[pygame.K_RIGHT] and self.x < d_width-32:
			self.x += self.speed
		if pygame.key.get_pressed()[pygame.K_LEFT] and self.x > 0:
			self.x -= self.speed
		if pygame.key.get_pressed()[pygame.K_UP] and self.y > 0:
			self.y -= self.speed
		if pygame.key.get_pressed()[pygame.K_DOWN] and self.y < d_height -32:
			self.y += self.speed
	def draw(self):
		pygame.draw.rect(self.sprite, BLUE, (0,0,self.width,self.height))
		wn.blit(self.sprite, (self.x, self.y))
	def check_collision(self, obj):
		global gameRunning
		if (self.x + self.width > obj.x and self.x < obj.x + obj.width) and (self.y + self.height > obj.y and self.y < obj.y + obj.height):
			score  =str(time.time() - start_time)
			print("You lasted " + str(score))
			if score < 10:
				print("Sorry, but you are extremely bad at this game. You need to practise for at least a year to get better.")
			elif score < 15:
				print("Meh, that is an okay score. I guess you are decent at this game, but still not that good.")
			elif score < 20:
				print("You are pretty good at this game, I'll give you that. Just practise a bit more for the top scores, alright?")
			else:
				print("Oh my dear goodness! You rock at this game. You should go pro.")
			gameRunning = False
	def stuff(self):
		self.move()
		self.draw()
		

baddyList =[]
class Baddy:
	def __init__(self, speed):
		self.x = 0
		self.y = 0
		
		self.width = 32
		self.height = 32
		self.speed = speed
		self.dir = random.randrange(0,360)
		baddyList.append(self)
		self.sprite = pygame.Surface((32,32))
	def draw(self):
		pygame.draw.rect(self.sprite, RED, (0,0,32,32))
		wn.blit(self.sprite, (self.x, self.y))
	def move(self):
		if self.x < 0 or self.x> d_height:
			self.dir  = (180-self.dir)
		if self.y < 0 or self.y> d_width:
			self.dir  = (360-self.dir)
		self.x += math.cos(self.dir*(math.pi/180))*self.speed
		self.y += math.sin(self.dir*(math.pi/180))*self.speed
	def stuff(self):
		self.move()
		self.draw()
		
if __name__ == "__main__":
	clock = pygame.time.Clock()
	player = Player(d_width/2, d_height/2)
	timer = 60
	while gameRunning:
		clock.tick(60)
		if timer>0:
			timer-=1
		if timer ==0:
			baddy = Baddy(baddySpeed)

			timer = 60
		
		
		wn.fill(WHITE)
		player.stuff()
		baddySpeed += 0.01
		for baddy in baddyList:
			
			if timer == 1:
				baddy.speed = baddySpeed
			player.check_collision(baddy)
			baddy.stuff()
		pygame.display.update()

	


		for event in pygame.event.get():
			if event == pygame.QUIT:
				gameRunning = False
		
	





	pygame.quit()
	exit()

