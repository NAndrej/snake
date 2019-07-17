import pygame
import random

WIDTH = 500
HEIGHT = 500
SNAKE_COLOR = [255, 0, 255]
WHITE = [255, 255, 255]
BLACK = [0, 0, 0]

class Game:

    def __init__(self):
        self.state = True
        self.obstacles = []
        self.draw_border()
        self.snake = None


    @staticmethod
    def generateApples():
        print('generateApples()')

    @staticmethod
    def makeObstacles(self):
        numObstacles = 5
        obstacles=[]
        for i in range(0, numObstacles):

            numBoxes = 5
            randAlign = random.randint(0, 1)
            xStartingPos = random.randint(100, 400)
            yStartingPos = random.randint(100, 400)

            if xStartingPos % 10 != 0:
                xStartingPos += (10 - (xStartingPos % 10))
            if yStartingPos % 10 != 0:
                yStartingPos += (10 - (yStartingPos % 10))

            if randAlign == 0:
                alignment = "V"
            else:
                alignment = "H"

            # construct
            for j in range(0, numBoxes):
                if alignment == "V":
                    obst = [xStartingPos, yStartingPos, 10, 10]
                    yStartingPos += 10
                    obstacles.append(obst)
                else:
                    obst = [xStartingPos, yStartingPos, 10, 10]
                    xStartingPos += 10
                    obstacles.append(obst)

        # find conflicts and clear one of the participants
        conflicts = []
        while True:
            for obst in range(0, len(obstacles)):
                for obst2 in range(0, len(obstacles)):
                    if obst != obst2 and obstacles[obst][0] == obstacles[obst2][0] and obstacles[obst][1] == obstacles[obst2][1]:
                        print('Obstacle', obst, 'at', obstacles[obst], 'conflicted with obstacle', obst2, 'at', obstacles[obst2], 'and was cleared along with the 2 surrounding obstacles at -1 and 1 indexes')
                        for o in range(-1, 1): #  the surrounding 2 obstacles also
                            obst =+ o
                            conflicts.append(obst)
            if len(conflicts) < 1:
                break
            for conf in conflicts:
                obstacles.pop(conf)
            conflicts.clear()

        print(obstacles)
        self.obstacles=obstacles

    @staticmethod
    def draw_obstacles(self):
        for obstacle in self.obstacles:
            pygame.draw.rect(window, [255, 255, 100], obstacle)

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
    def collisionCheck(self):
        for obstacle in self.obstacles:
            #preObstacle = [obstacle[0]-10,obstacle[1]-10,10,10]
            preObstacle = []
            head = self.snake.head
            if head[0] > obstacle[0]:
                preObstacle = [obstacle[0]+10,obstacle[1],10,10]
            if head[0] < obstacle[0]:
                preObstacle = [obstacle[0]-10,obstacle[1],10,10]
            if head[1] > obstacle[1]:
                preObstacle = [obstacle[0],obstacle[1]+10,10,10]
            if head[1] < obstacle[1]:
                preObstacle = [obstacle[0],obstacle[1]-10,10,10]

            if self.snake.head == preObstacle:
                self.snake.moving = False

class Snake:

    def __init__(self):

        self.boxes = [[WIDTH / 2, HEIGHT / 2, 10, 10], [(WIDTH / 2), HEIGHT / 2, 10, 10],
                      [(WIDTH / 2), HEIGHT / 2, 10, 10], [(WIDTH / 2), HEIGHT / 2, 10, 10]]
        self.distance = -10
        self.head = self.boxes[0]
        self.length = len(self.boxes)
        self.color = SNAKE_COLOR
        self.x_direction = 1
        self.y_direction = 0
        self.acceleration = 10
        self.score = 0
        self.sort_distance()
        self.moving = True;

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
        if self.moving:
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
    g.snake = s
    clock = pygame.time.Clock()
    g.makeObstacles(g)

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
        g.draw_obstacles(g)
        g.draw_border()
        s.move()
        g.collisionCheck(g)
        for box in s.boxes:
            pygame.draw.rect(window, s.color, box)


        pygame.display.flip()
        clock.tick(7.5)

pygame.quit()