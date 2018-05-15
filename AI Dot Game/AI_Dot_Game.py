import sys, 
import pygame
import operator  #add TUPLES
import random



pygame.init()
clockobject = pygame.time.Clock()
clockobject.tick(1)

size = WIDTH, HEIGHT = 800,800

BLACK = 0, 0, 0
GREEN = 0,255,0
RED = 255,0,0
WHITE = 255,255,255

TARGET_XY = (int(WIDTH/2),5)
START_XY = (int(WIDTH/2),int(WIDTH/2)) #(int(WIDTH/2),HEIGHT-5)  # start at the bottom centre
VECTOR_LEN = 20
POPULATION_SIZE = 500

def generate_instructions(num = 1000):
    inst = []
    for i in range(0, num-1):
        X = random.randint(VECTOR_LEN*(-1),VECTOR_LEN)
        Y = random.randint(VECTOR_LEN*(-1),VECTOR_LEN)
        XY = [X,Y]
        inst.append(XY)
    return inst

def distance(posA=(0,0), posB=(0,0)):
    dx = abs(posA[0] - posB[0])
    dy = abs(posA[1] - posB[1])
    return (dx**2 + dy**2)**0.5
            

def draw_target():
    pygame.draw.circle(screen,GREEN,TARGET_XY,8)
    
    
    
class Dot:
    def __init__(self):
        self.instructions = generate_instructions(1000)
        self.posXY = START_XY
        self.dead = False
        self.reached_goal = False
        self.step= 0
        self.fitness =0.00
        
    def show(self):
        if self.reached_goal:
            pygame.draw.circle(screen, RED, self.posXY,3)
        else:
            pygame.draw.circle(screen, WHITE, self.posXY,3)
        
    def move(self):
        if len(self.instructions) > self.step:
            #still instructions left to do
            self.posXY = tuple(map(operator.add, self.posXY, self.instructions[self.step]))
            self.step += 1
        else:
            self.dead = True
            

    def update(self):
        # move the dot if it is still alive
        if not ( self.dead or self.reached_goal) :
            self.move()
        # check if that move killed the dot
        if (self.posXY[0]<3 or 
           self.posXY[1]<3 or 
           self.posXY[0]>WIDTH-3 or 
           self.posXY[1]>HEIGHT-3):
            self.dead = True
        elif distance(self.posXY,TARGET_XY) < 10 :
            self.reached_goal = True
            # has the dot reached the target?
            
    def calculate_fitness(self):
        # fitness is a function of distance to target
        dist = distance(self.posXY, TARGET_XY)
        self.fitness = 1 / (dist**2)
        
        
class Population:
    def __init__(self,pop_size=10):
        self.generation = 1
        self.dots = []
        for i in range(1, pop_size):
            self.dots.append(Dot())
            
    def show(self):
        for dot in self.dots:
            dot.show()

    def update(self):
        for dot in self.dots:
            dot.update()

    def calculate_fitness(self):
        for dot in self.dots:
            dot.calculate_fitness()     

# ---------------------
screen = pygame.display.set_mode(size)
pygame.display.update()


#dot = Dot()
pop = Population(POPULATION_SIZE)

for j in range(0, 1000):
    # draw the playing field
    
    draw_target()
    
    pop.show()
    
    pop.update()
    
    # clean up for next move
    pygame.display.flip()
    screen.fill(BLACK)
    
pop.calculate_fitness()


pygame.quit()
sys.exit()
