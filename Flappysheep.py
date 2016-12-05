import pygame
import time

from pygame.locals import *

pygame.init()

import random

fenetre = pygame.display.set_mode((1300,700),FULLSCREEN)

icone = pygame.image.load("Docs/Flappyicone.ico").convert_alpha()
pygame.display.set_icon(icone)
pygame.display.set_caption("Flappy sheep")

fond = pygame.image.load("Docs/Fond.png").convert()
obstaclebas = pygame.image.load("Docs/Obstaclebas.png").convert()
obstaclehaut = pygame.image.load("Docs/Obstaclehaut.png").convert()
mouton = pygame.image.load("Docs/mouton.png").convert_alpha()
Traine = pygame.image.load("Docs/Traine.png").convert()
fenetre.blit(fond,(0,0))
pygame.display.flip()

font = pygame.font.SysFont('Arial', 40)

def afficher():
	time.sleep(0.002)
	fenetre.blit(fond,(0,0))
	for i in range(0,4):
		fenetre.blit(obstaclebas,(L[i][0],L[i][1]))
		fenetre.blit(obstaclehaut,(L[i][0],L[i][1]-900))
	for i in range(0,257):
		fenetre.blit(Traine,(i,T[i]))
	fenetre.blit(mouton,(250,M[0]))
	score1 = (str(score[0]))
	Score = font.render(score1,1,(255,255,255))
	positionscore = Score.get_rect(center = (100,600))
	fenetre.blit(Score,positionscore)
	pygame.display.flip()

def defilement():
	for i in range(0,4):
		L[i][0] += -1

def gravite():
	M[2] += M[1]
	M[1] += 0.06
	M[0] = int(round(M[2],0))
	for event in pygame.event.get():
		if event.type == QUIT:
			en_cours[0] = 0
			r[0] = 0
		if event.type == KEYDOWN:
			if event.key == pygame.K_UP:
				M[1] = -3.5
			if event.key == pygame.K_ESCAPE:
				en_cours[0] = 0
				r[0] = 0

def traine():
	for i in range(0,256):
		T[i] = T[i+1]
	T[256] = M[0] + 25

def chute():
	while M[0]<700:
		M[0] += int(M[1])
		M[1] += 0.01
		afficher()
	M[0] = 700
	while en_cours[0] == 1:
		afficher()
		for event in pygame.event.get():
			if event.type == QUIT:
				en_cours[0] = 0
				r[0] = 0
			if event.type == KEYDOWN:
				if event.key == pygame.K_ESCAPE:
					en_cours[0] = 0
					r[0] = 0
				if event.key == pygame.K_r:
					en_cours[0] = 0

r = [1]

while r[0] == 1:
	en_cours = [1]

	score = [0]

	L = [[4500,0],[4500,0],[4500,0],[4500,0]]
	M = [150,-3.5,150]
	T = []
	for k in range(0,257):
		T.append(1000)
	afficher()
	for event in pygame.event.get():
		if event.type == KEYDOWN:
			if event.key == pygame.K_ESCAPE:
				en_cours[0] = 0
				r[0] = 0
			if event.key == K_UP:
				for t in range(0,1000):
					if en_cours[0] == 0:
						break
					if M[0]>632:
						M = [632,0,632]
						chute()
					else:
						traine()
						gravite()
						afficher()

				hauteur = random.randint(250,650)
				L[0] = [1300,hauteur]
				for t in range (0,400):
					if en_cours[0] == 0:
						break
					if M[0]>632:
						M = [632,0,632]
						chute()
					else:
						traine()
						gravite()
						defilement()
						afficher()
				hauteur = random.randint(250,650)
				L[1] = L[0]
				L[0] = [1300,hauteur]
				for t in range (0,400):
					if en_cours[0] == 0:
						break
					if M[0]>632:
						M = [632,0,632]
						chute()
					else:
						traine()
						gravite()
						defilement()
						afficher()

				while en_cours[0] == 1:
					hauteur = random.randint(250,650)
					L[3] = L[2]
					L[2] = L[1]
					L[1] = L[0]
					L[0] = [1300,hauteur]
					for t in range (0,175):
						if en_cours[0] == 0:
							break
						if M[0]>632:
							M = [632,0]
							chute()
						else:
							traine()
							gravite()
							defilement()
							afficher()
					for t in range (175,176):
						if en_cours[0] == 0:
							break
						if M[0]>L[2][1]-43:
							M[1] = 0
							chute()
						if M[0]<L[2][1]-216:
							M[1] = 0
							chute()
						else:
							traine()
							gravite()
							defilement()
							afficher()
					for t in range (176,202):
						if en_cours[0] == 0:
							break
						if M[0]>L[2][1]-43:
							M = [L[2][1]-43,0,L[2][1]-43]
							chute()
						if M[0]<L[2][1]-216:
							M = [L[2][1]-216,0,L[2][1]-216]
							chute()
						else:
							traine()
							gravite()
							defilement()
							afficher()
					for t in range (202,275):
						if en_cours[0] == 0:
							break
						if M[0]>L[2][1]-68:
							M = [L[2][1]-68,0,L[2][1]-68]
							chute()
						if M[0]<L[2][1]-216:
							M = [L[2][1]-216,0,L[2][1]-216]
							chute()
						else:
							traine()
							gravite()
							defilement()
							afficher()
					for t in range (275,323):
						if en_cours[0] == 0:
							break
						if M[0]>L[2][1]-68:
							M = [L[2][1]-68,0,L[2][1]-68]
							chute()
						if M[0]<L[2][1]-223:
							M = [L[2][1]-223,0,L[2][1]-223]
							chute()
						else:
							traine()
							gravite()
							defilement()
							afficher()
					score[0] += 1
					for t in range (323,400):
						if en_cours[0] == 0:
							break
						if M[0]>632:
							M = [632,0,632]
							chute()
						else:
							traine()
							gravite()
							defilement()
							afficher()