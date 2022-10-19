# Simple pygame program

# Import and initialize the pygame library
import pygame
import random
pygame.init()

# Set up the drawing window
screen = pygame.display.set_mode([500, 500])

#The size of a square
SQUARE_X = 25
SQUARE_Y = 25

def coordinate(x):
    return x*25

def handle_movement(event, update_value_x, update_value_y):
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_RIGHT:
            #If we arent already moving left
            if update_value_x != -1:
                update_value_x = 1
                update_value_y = 0
        if event.key == pygame.K_LEFT:
            #If we arent already moving right
            if update_value_x != 1:
                update_value_x = -1
                update_value_y = 0
        if event.key == pygame.K_UP:
            #If we arent already moving down
            if update_value_y != 1:
                update_value_y = -1
                update_value_x = 0
        if event.key == pygame.K_DOWN:
            #If we arent already moving up
            if update_value_y != -1:
                update_value_y = 1
                update_value_x = 0
    return update_value_x, update_value_y
    
def is_same_position(position_1, position_2):
    if position_1 == position_2:
        return True
    else:
        return False


def main():
    # Run until the user asks to quit
    running = True

    SNAKE_X = 1
    SNAKE_Y = 1
    
    snake = [(SNAKE_X,SNAKE_Y)]

    snake_length = 1
    
    update_value_x = 0
    update_value_y = 0

    food_x = coordinate(random.randint(0,19))
    food_y = coordinate(random.randint(0,19)) 

    while running:

        # Did the user click the window close button?
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Fill the background with white
        screen.fill((255, 255, 255))

            # Initialing Color
        snake_color = (255,0,0)
        food_color = (37, 209, 2)
        
        pygame.draw.rect(screen, food_color, pygame.Rect(food_x, food_y, SQUARE_X, SQUARE_Y))

        # Drawing Rectangle
        for part in snake:
            pygame.draw.rect(screen, snake_color, pygame.Rect(coordinate(part[0]), coordinate(part[1]), SQUARE_X, SQUARE_Y))

        pygame.time.wait(75)
    
        update_value_x, update_value_y = handle_movement(event, update_value_x,update_value_y) 
        SNAKE_X += update_value_x
        SNAKE_Y += update_value_y

        if(coordinate(SNAKE_X) == coordinate(20)):
            SNAKE_X = 0
        if(coordinate(SNAKE_X) == coordinate(-1)):
            SNAKE_X = 20

        if(coordinate(SNAKE_Y) == coordinate(20)):
            SNAKE_Y = 0
        if(coordinate(SNAKE_Y) == coordinate(-1)):
            SNAKE_Y = 20

        snake.append((SNAKE_X,SNAKE_Y))

        if len(snake) > snake_length:
            del snake[0]

        if coordinate(SNAKE_X) == food_x and coordinate(SNAKE_Y) == food_y:
            food_x = coordinate(random.randint(0,19))
            food_y = coordinate(random.randint(0,19)) 
            snake_length += 1

        for row in range(1, int(500/25)):
            for column in range(1,int(500/25)):
                pygame.draw.line(screen, (0,0,0), (SQUARE_X*row,SQUARE_Y*column),(SQUARE_X*row,SQUARE_Y*column))

        # Flip the display
        pygame.display.flip()

# Done! Time to quit.
main()
pygame.quit()