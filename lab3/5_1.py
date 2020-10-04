import pygame
from pygame.draw import *
import numpy as np

pygame.init()

FPS = 30
size = [1000, 550]
size_x, size_y = size[0], size[1]
screen = pygame.display.set_mode(size)
screen.fill((255, 255, 255))

#Матрица перехода от относительных координат к абсолютным
S = np.array([[size_x, 0], [0, size_y]], ndmin=2)

#Факториал
def fact(n):
    if n == 0:
        return 1
    else:
        return n*fact(n-1)

#Кривая Безье
def beziercurve(pointlist, stepcount=100):
    n = len(pointlist)-1
    pl = np.array(pointlist)
    result = np.zeros((stepcount, 2))
    for step in range(stepcount):
        t = step / (stepcount-1)
        vec = np.zeros(2)
        for j in range(0,n+1):
            vec += pl[j]*fact(n)/(fact(j)*fact(n-j)) * t**j * (1-t)**(n-j)
        result[step] = vec
    return result

#1 полоса
color1 = [254, 213, 162]
x1, y1 = [0.000, 0.000] @ S
x2, y2 = [1.000, 0.215] @ S
rect(screen, color1, [x1, y1, x2-x1, y2-y1+1])

#2 полоса
color2 = [254, 213, 196]
x1, y1 = [0.000, 0.215] @ S
x2, y2 = [1.000, 0.431] @ S
rect(screen, color2, [x1, y1, x2-x1, y2-y1+1])

#3 полоса
color3 = [254, 213, 148]
x1, y1 = [0.000, 0.431] @ S
x2, y2 = [1.000, 0.640] @ S
rect(screen, color3, [x1, y1, x2-x1, y2-y1+1])

#4 полоса
color4 = [179, 134, 148]
x1, y1 = [0.000, 0.640] @ S
x2, y2 = [1.000, 1.000] @ S
rect(screen, color4, [x1, y1, x2-x1, y2-y1+1])

#Солнце
sun_color = [252, 238, 33]
sun_x, sun_y = [0.500, 0.200] @ S
sun_r = int(0.060 * size_x)
circle(screen, sun_color, [int(sun_x), int(sun_y)], sun_r)

#Верхние горы
color11 = [252,152,49]
poly = np.vstack((
	[0.006, 0.470],
	[0.013, 0.406], 
    beziercurve([
		[0.013, 0.406],
		[0.097, 0.401],
		[0.207, 0.198],
		]), 
	[0.207, 0.198],
	[0.245, 0.215],
	[0.263, 0.255],
	[0.385, 0.378],
	[0.452, 0.363],
	[0.486, 0.390],
	[0.535, 0.319],
	[0.577, 0.333],
	[0.602, 0.301], 
    beziercurve([
		[0.602, 0.301],
		[0.671, 0.307],
		[0.717, 0.106],
		[0.750, 0.185],
		]), 
	[0.750, 0.185],
	[0.795, 0.250],
	[0.831, 0.236], 
    beziercurve([
		[0.831, 0.236],
		[0.850, 0.236],
		[0.897, 0.286],
		]), 
	[0.897, 0.286],
	[0.932, 0.259],
	[1.000, 0.311],
	[1.000, 0.314]
	)) @ S
polygon(screen, color11, poly)

#Нижние горы
color12 = [172,67,52]
poly = np.vstack((
	[0.000, 0.570],
	[0.025, 0.520],
	beziercurve([
		[0.025, 0.520],
		[0.087, 0.321],
		[0.136, 0.355],
		[0.175, 0.640],
		]),
	[0.175, 0.640],
	[0.220, 0.530],
	[0.290, 0.585],
	[0.320, 0.450],
	[0.410, 0.480],
	[0.480, 0.560],
	[0.575, 0.530],
	beziercurve([
		[0.575, 0.530],
		[0.673, 0.365],
		[0.726, 0.445],
		]),
	beziercurve([
		[0.726, 0.445],
		[0.777, 0.512],
		[0.820, 0.530],
		]),
	[0.820, 0.530],
	[0.860, 0.450],
	[0.900, 0.500],
	[0.920, 0.445],
	[0.960, 0.450],
	[1.000, 0.360],
	[1.000, 0.645],
	[0.000, 0.680]	
	)) @ S
polygon(screen, color12, poly)

#Темные нижние горы
color13 = [48,16,38]
poly = np.vstack((
	[0.000, 1.000],
	[0.000, 0.518],
	[0.120, 0.565],
	[0.215, 0.742],
	[0.300, 0.920],
	beziercurve([
		[0.300, 0.920],
		[0.350, 0.996],
		[0.470, 0.985],
		]),
	[0.470, 0.985],
	[0.633, 0.850],
	[0.680, 0.880],
	beziercurve([
		[0.680, 0.880],
		[0.800, 1.100],
		[0.956, 0.620],
		[1.000, 0.605],
		]),
	[1.000, 0.605],
	[1.000, 1.000]
	)) @ S
polygon(screen, color13, poly)

#Рисование птиц
bird_color = [66,33,11]
bird_original_relative_size = 0.05
bird = np.vstack((beziercurve([
		[+0.00, +0.00],
		[+0.26, -0.38],
		[+0.90, -0.42],
		]),
	beziercurve([
		[+0.90, -0.42],
		[-0.06, +0.36],
		]),
	beziercurve([
		[-0.06, +0.36],
		[-0.96, -0.32],
		[-0.88, -0.42],
		]),
	beziercurve([
		[-0.88, -0.42],
		[-0.64, -0.46],
		[+0.00, +0.00],
		])))

def bird_relative(relative_pos, relative_size=1.00):
	return [relative_pos + pt * relative_size*bird_original_relative_size for pt in bird] @ S

birds = np.array([[0.387, 0.352, 0.70],
	     [0.477, 0.364, 0.70],
	     [0.477, 0.415, 0.70],
	     [0.400, 0.457, 0.70],
	     [0.630, 0.666, 0.80],
	     [0.685, 0.741, 0.70],
	     [0.797, 0.715, 0.60],
	     [0.782, 0.785, 1.00]])

for elem in birds:
	polygon(screen, bird_color, bird_relative(elem[:2], elem[2]))


pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
	clock.tick(FPS)
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			finished = True

pygame.quit()
