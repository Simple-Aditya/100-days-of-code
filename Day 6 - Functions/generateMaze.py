import random
def generateMap(i = 10):
    maze = [['_'] * i for _ in range(i)]
    return maze

def initializeTwoPoints(maze):
    start = random.randint(0, len(maze) - 1), random.randint(0, len(maze) - 1)
    end = random.randint(0, len(maze) - 1), random.randint(0, len(maze) - 1)
    while start == end:
        end = random.randint(0, len(maze) - 1), random.randint(0, len(maze) - 1)
    
    maze[start[0]][start[1]] = 'S'
    maze[end[0]][end[1]] = 'E'
    
    return maze

def generateBarriers(maze):
    num_barriers = random.randint(1, len(maze) * len(maze) // 4)
    for i in range(num_barriers):
        x, y = random.randint(0, len(maze) - 1), random.randint(0, len(maze) - 1)
        while maze[x][y] != '_':
            x, y = random.randint(0, len(maze) - 1), random.randint(0, len(maze) - 1)
        maze[x][y] = '#'
    return maze

def printMaze(maze):
    for row in maze:
        print(row)
