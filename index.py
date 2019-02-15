#!/usr/bin/env python3

#########################################################
## Desarrollado en el Area de Control de Procesos del	#
## Dpto de Electronica de la UAM Azcapotzalco			#
## 														#
#########################################################

import pygame,sys,os #importamos los modulos necesarios
from pygame.locals import *



FPS = 30
ANCHO_PANTALLA = 800	#Resolucion establecida para la pantalla touch 7' de la Raspberry
ALTO_PANTALLA = 450
FPSCLOCK = pygame.time.Clock()

#ROJO=(155,0,0)
red = (255,51,51)
blue = (51,51,255)
green = (51,255,51)

ROJORECT = pygame.Rect(40,120,150,150)
AZULRECT = pygame.Rect(250,120,150,150)
VERDERECT = pygame.Rect(460,120,150,150)


if __name__=='__main__':
	pygame.init()
	fpsClock = pygame.time.Clock()
	VENTANA = pygame.display.set_mode((ANCHO_PANTALLA,ALTO_PANTALLA))
	pygame.display.set_caption("FINGERPRINT SENSOR")
	
	fontObj=pygame.font.Font('freesansbold.ttf',25)
	newfp = fontObj.render('Nueva Huella',True,red)
	newfpRect = newfp.get_rect()
	newfpRect.center = (115,70)
	
	searchfp = fontObj.render('Cotejar Huella',True,blue)
	searchfpRect = searchfp.get_rect()
	searchfpRect.center = (325,70)
	
	delfp = fontObj.render('Eliminar Huella',True,green)
	delfpRect = delfp.get_rect()
	delfpRect.center = (540,70)
	
	def colliderect(x,y):
		if ROJORECT.collidepoint((x,y)):
			
			mssgfp = fontObj.render('En proceso...',True,red)
			mssgfpRect = mssgfp.get_rect()
			mssgfpRect.center = (340,330)
			VENTANA.blit(mssgfp,mssgfpRect)
			pygame.display.update()
			os.system("./leer_huella.py")
			pygame.time.wait(2500)
			print ("Terminado...")
			os.system("clear")

		if AZULRECT.collidepoint((x,y)):
			
			mssgfp = fontObj.render('En proceso...',True,red)
			mssgfpRect = mssgfp.get_rect()
			mssgfpRect.center = (340,330)
			VENTANA.blit(mssgfp,mssgfpRect)
			pygame.display.update()
			os.system("./buscar_huella.py")
			pygame.time.wait(2500)
			print ("Terminado...")
			
		if VERDERECT.collidepoint((x,y)):
			
			mssgfp = fontObj.render('En proceso...',True,red)
			mssgfpRect = mssgfp.get_rect()
			mssgfpRect.center = (340,330)
			VENTANA.blit(mssgfp,mssgfpRect)
			pygame.display.update()
			os.system("./eliminar_huella.py")
			pygame.time.wait(2500)
			print ("Terminado...")
	
	
	while True:
		VENTANA.fill((100,100,100))
		pygame.draw.rect(VENTANA, red, ROJORECT)
		pygame.draw.rect(VENTANA, blue, AZULRECT)
		pygame.draw.rect(VENTANA, green, VERDERECT)
		VENTANA.blit(newfp,newfpRect)
		VENTANA.blit(searchfp,searchfpRect)
		VENTANA.blit(delfp,delfpRect)
		pygame.display.update()
	
		for event in pygame.event.get():
			if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
				#os.system("./leer_huella.py")
				pygame.quit()
				sys.exit()
			else:
				if event.type == MOUSEBUTTONUP:
					mousex,mousey = event.pos
					colliderect(mousex,mousey)


		pygame.display.update()
		FPSCLOCK.tick(FPS)
