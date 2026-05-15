import generateMaze

maze = generateMaze.generateMap(10)
maze = generateMaze.initializeTwoPoints(maze)
maze = generateMaze.generateBarriers(maze)
generateMaze.printMaze(maze)

def escapeMaze(maze):
    
    escape = []
    
    start, end = None, None
    for i in range(len(maze)):
        for j in range(len(maze[i])):
            if maze[i][j] == 'S':
                start = (i, j)
            elif maze[i][j] == 'E':
                end = (i, j)
    
    mouse = start
    while mouse != end:
        x, y = mouse
        if x < end[0] and maze[x + 1][y] != '#':
            mouse = (x + 1, y)
        elif x > end[0] and maze[x - 1][y] != '#':
            mouse = (x - 1, y)
        elif y < end[1] and maze[x][y + 1] != '#':
            mouse = (x, y + 1)
        elif y > end[1] and maze[x][y - 1] != '#':
            mouse = (x, y - 1)
        else:
            return "No escape possible"
        
        escape.append(mouse)
        
    return escape

print(escapeMaze(maze))