import pygame
import time
from random import randint
class cell:
	def __init__(self,x,y,width):
		self.color=[255,255,255]
		self.pos=(x,y)
		self.future=False

	def draw(self):
		pygame.draw.rect(fenetre, self.color, [self.pos[0]+0.25,self.pos[1]+0.25,width-0.25,width-0.25], 0)

	def draw_with_axis(self):
		pygame.draw.rect(fenetre, self.color, [self.pos[0]+2,self.pos[1]+2,width-2,width-2], 0)
		police=pygame.font.SysFont("rubikbold",7)
		image_texte=police.render(str(self.pos),1,(0,50,250))
		fenetre.blit(image_texte,(self.pos[0]+5,self.pos[1]+5))


	def invert_color(self):
		if self.color==[255,255,255]:
			self.color=[0,0,0]
		else:
			self.color=[255,255,255]

	def is_alive(self):
		return self.color==[0,0,0]

	def new_state(self,listOfCells):
		listOfNeighbours=[]
		for i in listOfCells:
			if self.pos[0]-width==i.pos[0] and self.pos[1]-width==i.pos[1]:
				listOfNeighbours.append(i)
			if self.pos[0]==i.pos[0] and self.pos[1]-width==i.pos[1]:
				listOfNeighbours.append(i)
			if self.pos[0]+width==i.pos[0] and self.pos[1]-width==i.pos[1]:
				listOfNeighbours.append(i)
			if self.pos[0]-width==i.pos[0] and self.pos[1]==i.pos[1]:
				listOfNeighbours.append(i)
			if self.pos[0]+width==i.pos[0] and self.pos[1]+width==i.pos[1]:
				listOfNeighbours.append(i)
			if self.pos[0]==i.pos[0] and self.pos[1]+width==i.pos[1]:
				listOfNeighbours.append(i)
			if self.pos[0]-width==i.pos[0] and self.pos[1]+width==i.pos[1]:
				listOfNeighbours.append(i)
			if self.pos[0]+width==i.pos[0] and self.pos[1]==i.pos[1]:
				listOfNeighbours.append(i)
		aliveNeighbours=0
		for k in listOfNeighbours:
			if k.is_alive():
				aliveNeighbours+=1
		if (not(self.is_alive()) and aliveNeighbours==3):
			return True
		if (self.is_alive() and (aliveNeighbours>=2 and aliveNeighbours<=3)):
			return True
		return False

def cell_generation(res,width):
	cell_list=[]
	for i in range(0,res[0]+1-width,width):
		for k in range(0,res[1]+1-width,width):
			s=cell(i,k,width)
			cell_list.append(s)
	return cell_list

def print_cells(listOfCells,gene_nbr):
	fenetre.fill([0,0,255])
	for i in listOfCells:
		i.draw()
	police=pygame.font.SysFont("rubikbold",30)
	image_texte=police.render(str(gene_nbr),1,(255,0,00))
	fenetre.blit(image_texte,(20,20))
	pygame.display.update()

def new_generation(listOfCells):
	for i in listOfCells:
		i.future=False
		if i.new_state(listOfCells):
			i.future=True
	for i in listOfCells:
		if i.future:
			i.color=[0,0,0]
		else:
			i.color=[255,255,255]

def stop_playing():
	for event in pygame.event.get():
		if event.type == pygame.QUIT or event.type==pygame.KEYDOWN:
			pygame.display.quit()
	pygame.event.pump()
	return

def configuration(listOfCells,width,res):
	start=False
	while start==False :
		for event in pygame.event.get():
			if event.type == 1025:
				(x,y)=pygame.mouse.get_pos()
				number=int(int((x/width))*(res[1]/width)+y/width)
				listOfCells[number].invert_color()
				print_cells(listOfCells,0)
			if event.type == pygame.QUIT or event.type == pygame.KEYDOWN:
				start=True

def game():
	list_cells=cell_generation(ecran,width)
	print_cells(list_cells,0)
	configuration(list_cells,width,ecran)
	for i in range(1,1500):
		new_generation(list_cells)
		print_cells(list_cells,i)
		stop_playing()
	pygame.display.quit()

#pygame init--------
ecran = (1200,700)
pygame.display.init()
pygame.font.init()
pygame.display.set_caption('Game of life')
fenetre = pygame.display.set_mode(ecran)
width=25

game()