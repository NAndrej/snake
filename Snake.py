import pygame, math, random

WIDTH = 500
HEIGHT = 500
WHITE = [255, 255, 255]
BLACK = [0, 0, 0]

def sort_distance(snake):
    for sBox in snake.boxes:
        sBox[0] += snake.distance * (snake.boxes.index(sBox) + 1)

class Game:
    def __init__(self):
        self.state = True
        self.obstacles = False
        self.draw_border()

    def makeObstacles(self):

        #  TODO:  Check if it collides with initial snake and apples? position

        obstacles = []
        numObstacles = random.randint(3, 6)
        print("Number of Obstacles: ", numObstacles)
        for i in range(1, numObstacles + 1):
            numBoxes = random.randint(2, 5)
            randAlign = random.randint(0, 1)
            if randAlign == 0:
                alignment = "V"
            else:
                alignment = "H"
            print("Number of boxes for the ", i, " obstacle is : ", numBoxes, ", with ", alignment, " alignment")

            xStartingPos = random.randint(1, 489)
            yStartingPos = random.randint(1, 489)
            startBox = [xStartingPos, yStartingPos, 10, 10]
            obstacles.append(startBox)

            if alignment == "V":
                for j in range(1, numBoxes):
                    yStartingPos += 10
                    box = [xStartingPos, yStartingPos, 10, 10]
                    obstacles.append(box)

            if alignment == "H":
                for j in range(1, numBoxes):
                    xStartingPos += 10
                    box = [xStartingPos, yStartingPos, 10, 10]
                    obstacles.append(box)

        return obstacles

    def draw_obstacles(self, obst):
        for obstacle in obst:
            pygame.draw.rect(window, WHITE, obstacle)
        print(obst)
        self.obstacles = True

    def draw_border(self):
        border = []
        for i in range(1, 499):
            border.append([i, 0, 10, 10])
            border.append([490, i, 10, 10])
            border.append([0, i, 10, 10])
            border.append([i, 490, 10, 10])
        for borderBox in border:
            pygame.draw.rect(window, WHITE, borderBox)

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
        self.previous_x_dir = self.x_direction
        self.previous_y_dir = self.y_direction
        self.previous_x = 0
        self.previous_y = 0
        self.flip = False
        self.acceleration = 15
        self.score = 0
        sort_distance(self)

    def update_direction(self, p_direction):
        self.previous_x_dir = self.x_direction
        self.previous_y_dir = self.y_direction
        self.previous_x = self.boxes[0][0]
        self.previous_y = self.boxes[0][1]
        self.flip = True
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

if __name__ == "__main__":
    pygame.init()
    window = pygame.display.set_mode((WIDTH, HEIGHT))
    g = Game()
    s = Snake()
    clock = pygame.time.Clock()

    while g.state:
        pygame.Surface.fill(window, BLACK)
        if not g.obstacles:
            g.draw_obstacles(g.makeObstacles())

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                g.state = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    if s.y_direction != 1:
                        s.update_direction("UP")
                        #s.move()
                if event.key == pygame.K_DOWN:
                    if s.y_direction != -1:
                        s.update_direction("DOWN")
                        #s.move()
                if event.key == pygame.K_LEFT:
                    if s.x_direction != 1:
                        s.update_direction("LEFT")
                        #s.move()
                if event.key == pygame.K_RIGHT:
                    if s.x_direction != -1:
                        s.update_direction("RIGHT")
                        #s.move()
        s.move()
        for box in s.boxes:
            pygame.draw.rect(window, s.color, box)
        pygame.display.update()
        clock.tick(5)


pygame.quit()
