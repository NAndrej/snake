
import pygame
import random

WIDTH = 500
HEIGHT = 500
WHITE = [255, 255, 255]
BLACK = [0, 0, 0]


class Game:
    def __init__(self):
        self.state = True
        self.draw_border()

    @staticmethod
    def generateApples():
        print('generateApples()')

    @staticmethod
    def makeObstacles():
        obstacles = []
        numObstacles = random.randint(5, 10)
        for i in range(0, numObstacles):
            numBoxes = random.randint(3, 6)
            randAlign = random.randint(0, 1)
            xStartingPos = random.randint(25, 476)
            yStartingPos = random.randint(25, 476)

            if xStartingPos % 10 != 0:
                xStartingPos += (10 - (xStartingPos % 10))
            if yStartingPos % 10 != 0:
                yStartingPos += (10 - (yStartingPos % 10))

            print ('xStartingPos[', i ,']: ', xStartingPos)
            print ('yStartingPos[', i ,']: ', yStartingPos)

            if randAlign == 0:
                alignment = "V"
            else:
                alignment = "H"

            for j in range(0, numBoxes):
                if alignment == "V":
                    obst = [xStartingPos, yStartingPos, 10, 10]
                    yStartingPos += 10
                    obstacles.append(obst)
                else:
                    obst = [xStartingPos, yStartingPos, 10, 10]
                    xStartingPos += 10
                    obstacles.append(obst)
        return obstacles

    @staticmethod
    def draw_obstacles(obst):
        for obstacle in obst:
            pygame.draw.rect(window, WHITE, obstacle)

    @staticmethod
    def draw_border():
        border = []
        for i in range(0, 491):
            border.append([i, 0, 10, 10])
            border.append([490, i, 10, 10])
            border.append([0, i, 10, 10])
            border.append([i, 490, 10, 10])
        for borderBox in border:
            pygame.draw.rect(window, WHITE, borderBox)

    @staticmethod
    def collisionCheck():
        print('collisionCheck()')

class Snake:
    def __init__(self):
        self.boxes = [[WIDTH / 2, HEIGHT / 2, 10, 10], [(WIDTH / 2), HEIGHT / 2, 10, 10],
                      [(WIDTH / 2), HEIGHT / 2, 10, 10], [(WIDTH / 2), HEIGHT / 2, 10, 10]]
        self.distance = -15
        self.head = self.boxes[0]
        self.length = len(self.boxes)
        self.color = WHITE
        self.x_direction = 1
        self.y_direction = 0
        self.acceleration = 10
        self.score = 0
        self.sort_distance()

    def update_direction(self, p_direction):
        if p_direction == "RIGHT":
            self.x_direction = 1
            self.y_direction = 0
        if p_direction == "LEFT":
            self.x_direction = -1
            self.y_direction = 0
        if p_direction == "UP":
            self.y_direction = -1
            self.x_direction = 0
        if p_direction == "DOWN":
            self.y_direction = 1
            self.x_direction = 0

    def move(self):
        previousX = self.boxes[0][0]
        previousY = self.boxes[0][1]

        self.boxes[0][0] += self.x_direction * self.acceleration
        self.boxes[0][1] += self.y_direction * self.acceleration

        for sBox in self.boxes:
            if sBox == self.boxes[0]: continue
            newPreviousX = sBox[0]
            newPreviousY = sBox[1]
            sBox[0] = previousX
            sBox[1] = previousY
            previousX = newPreviousX
            previousY = newPreviousY

    def sort_distance(self):
        for sBox in self.boxes:
            sBox[0] += self.distance * (self.boxes.index(sBox) + 1)


if __name__ == "__main__":
    pygame.init()
    window = pygame.display.set_mode((WIDTH, HEIGHT))
    g = Game()
    s = Snake()
    clock = pygame.time.Clock()
    obstacles = g.makeObstacles()

    while g.state:
        pygame.Surface.fill(window, BLACK)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                g.state = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    if s.y_direction != 1:
                        s.update_direction("UP")
                        break
                if event.key == pygame.K_DOWN:
                    if s.y_direction != -1:
                        s.update_direction("DOWN")
                        break
                if event.key == pygame.K_LEFT:
                    if s.x_direction != 1:
                        s.update_direction("LEFT")
                        break
                if event.key == pygame.K_RIGHT:
                    if s.x_direction != -1:
                        s.update_direction("RIGHT")
                        break
        s.move()
        for box in s.boxes:
            pygame.draw.rect(window, s.color, box)
        g.draw_obstacles(obstacles)
        g.draw_border()
        pygame.display.flip()
        clock.tick(5)

pygame.quit()
