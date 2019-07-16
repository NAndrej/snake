import pygame, math, random

WIDTH = 500
HEIGHT = 500
WHITE=[255,255,255]
BLACK=[0,0,0]

def makeObstacles():

    #TODO:  Check if it collides with initial snake and apples? position

    obstacles=[]
    numObstacles = random.randint(3, 6)
    print("Number of Obstacles: ", numObstacles)
    for i in range(1, numObstacles + 1):
        numBoxes = random.randint(2, 5)
        randAlign = random.randint(0, 1)
        if randAlign == 0:
            alignment = "V"
        else:
            alignment = "H"
        print("Number of boxes for the ", i," obstacle is : ", numBoxes,", with ", alignment," alignment")

        xStartingPos = random.randint(1, 499)
        yStartingPos = random.randint(1, 499)
        startBox = [xStartingPos, yStartingPos, 10, 10]
        obstacles.append(startBox)

        if alignment == "V":
            for j in range(1,numBoxes):
                yStartingPos += 10
                box=[xStartingPos,yStartingPos,10,10]
                obstacles.append(box)

        if alignment == "H":
            for j in range(1,numBoxes):
                xStartingPos += 10
                box=[xStartingPos,yStartingPos,10,10]
                obstacles.append(box)

    return obstacles


if __name__ == "__main__":
    pygame.init()
    window = pygame.display.set_mode((WIDTH, HEIGHT))
    running = True
    obstaclesMade = False
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        if not obstaclesMade:
            obstacles = makeObstacles()
            for obstacle in obstacles:
                pygame.draw.rect(window,WHITE,obstacle)
            obstaclesMade = True
            print(obstacles)

        pygame.display.flip()

    pygame.quit()
