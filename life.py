import random
import pygame

pygame.init()

cells_along_X = 60
cells_along_Y = 40

cell_side = 20

display_X = cells_along_X * cell_side
display_Y = cells_along_Y * cell_side

display = pygame.display.set_mode((display_X, display_Y))
pygame.display.set_caption("Game of life")

def init_state(x, y):
    init_state_list = []

    for row in range(y):
        init_state_list.append([])

    for row in range(y):
        for col in range(x):
            init_state_list[row].append(0)
    return init_state_list

dead_state = init_state(cells_along_X, cells_along_Y)

def rand_state(x, y):
    init_state_list = []

    for row in range(y):
        init_state_list.append([])

    for row in range(y):
        for col in range(x):
            init_state_list[row].append(random.randint(0, 1))
    return init_state_list

random_state = rand_state(cells_along_X, cells_along_Y)


def wrapper(state):
    wrpp = []
    for n in range(len(state) + 2):
        wrpp.append([])

    for row in range(len(state) + 2):
        for col in range(len(state[1]) + 2):
            wrpp[row].append(0)

  # for _list
    lastcol = len(state[1]) - 1
    lastrow = len(state) - 1

  # upper border
    wrpp[0][0] = state[lastrow][lastcol]  # Principle diagonal corners
    wrpp[0][len(wrpp) - 1] = state[lastrow][0]  # Secondary diagonal corners

    (wrpp[0])[1:len(wrpp[1]) - 1] = (state[len(state) - 1])[:]

  # lower border
    wrpp[len(wrpp) - 1][len(wrpp[1]) - 1] = state[0][0]  # Principle diagonal corners
    wrpp[len(wrpp) - 1][0] = state[0][len(state[1]) - 1]  # Secondary diagonal corners

    (wrpp[len(wrpp) - 1])[1:len(wrpp[1]) - 1] = (state[0])[:]

    for n in range(len(state)):
        wrpp[n + 1][0] = state[n][len(state[n]) - 1]  # last item to position 0
        wrpp[n + 1][len(wrpp[n]) - 1] = state[n][0]  # first item to psition last

        (wrpp[n + 1])[1:len(wrpp[n]) - 1] = (state[n])[:]

    return wrpp


def count_neighbours(state):
    neighbours = []

    wrapped_state = wrapper(state)

    for row in range(len(state)):
        neighbours.append([])

    #print(neighbours)    
    for row in range(len(state)):
        #print(len(state[row]))
        for col in range(len(state[row])):
            #print(neighbours, end=" ")
            #neighbours[row][col].append(1)
            neighbours[row].append(0)

            wrow = row + 1
            wcol = col + 1

            if wrapped_state[wrow-1][wcol-1] == 1:      
                neighbours[row][col] += 1
            if wrapped_state[wrow-1][wcol] == 1:      
                neighbours[row][col] += 1 
            if wrapped_state[wrow-1][wcol+1] == 1:      
                neighbours[row][col] += 1

            if wrapped_state[wrow][wcol-1] == 1:      
                neighbours[row][col] += 1
            if wrapped_state[wrow][wcol+1] == 1:      
                neighbours[row][col] += 1    

            if wrapped_state[wrow+1][wcol-1] == 1:      
                neighbours[row][col] += 1
            if wrapped_state[wrow+1][wcol] == 1:      
                neighbours[row][col] += 1 
            if wrapped_state[wrow+1][wcol+1] == 1:      
                neighbours[row][col] += 1    

                    
    return neighbours


def new_state(state):

    neighbour_count = count_neighbours(state)
    
    next_state = init_state(len(state[1]), len(state))

    for row in range(len(state)):
        for col in range(len(state[row])):
            
            if state[row][col] == 1: # live cell
                if neighbour_count[row][col] < 2:
                    next_state[row][col] = 0
                elif neighbour_count[row][col] == 2 or neighbour_count[row][col] == 3:
                    next_state[row][col] = 1
                elif neighbour_count[row][col] > 3:
                    next_state[row][col] = 0
                else:
                    next_state[row][col] = 0

            elif state[row][col] == 0: # dead cell
                if neighbour_count[row][col] == 3:
                    next_state[row][col] = 1                    
                else:
                    next_state[row][col] = 0
    return next_state


def draw_board(state):
    for row in range(len(state)):
        for col in range(len(state[row])):
            if state[row][col] == 1:
                pygame.draw.rect(display, (100, 70, 100), [col * 20, row * 20, cell_side-1, cell_side-1])


def run_forever(state):
    n = 0
    while n < 200:
        if n % 2 == 0:
            draw_board(state)
            print(n)
            n+=1
        else:
            display.fill((150, 150, 150))    
            state = draw_board(new_state(state))
            print(n)
            n+=1
        pygame.display.update()

clock = pygame.time.Clock()

running = True
while running:
    clock.tick(60)

    display.fill((150, 150, 150))
 
    #run_forever(random_state)
    n = 0
    while n < 200:
        if n % 2 == 0:
            draw_board(random_state)
            print(n)
            n+=1
        else:
            display.fill((150, 150, 150))    
            state = draw_board(new_state(random_state))
            print(n)
            n+=1
        pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    

    pygame.display.update()
