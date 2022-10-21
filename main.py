# Simple pygame program

# Import and initialize the pygame library
from ast import Str
import pygame
import random
pygame.init()

# Set up the drawing window
screen = pygame.display.set_mode([500, 500])

#The size of a square
SQUARE_X = 25
SQUARE_Y = 25

#Return row and column coordinate given an x value.
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

def main():
    # Run until the game is over.
    running = True

    #Initilizing snake values
    SNAKE_X = 1
    SNAKE_Y = 1
    snake = [(SNAKE_X,SNAKE_Y)]
    snake_length = 1
    
    #Speed starts at 0
    update_value_x = 0
    update_value_y = 0

    #First food coordinate
    food_x = coordinate(random.randint(0,19))
    food_y = coordinate(random.randint(0,19)) 

    # Initialing Color
    snake_color = (255,0,0)
    food_color = (37, 209, 2)

    while running:

        # Did the user click the window close button?
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Fill the background with white
        screen.fill((255, 255, 255))
        
        #Draw the food.
        pygame.draw.rect(screen, food_color, pygame.Rect(food_x, food_y, SQUARE_X, SQUARE_Y))

        #Basic game logic, stepping through snake movement.
        pygame.time.wait(75)
        update_value_x, update_value_y = handle_movement(event, update_value_x,update_value_y) 
        SNAKE_X += update_value_x
        SNAKE_Y += update_value_y

        # Drawing Rectangle for each part of the snake.
        for part in snake:
            pygame.draw.rect(screen, snake_color, pygame.Rect(coordinate(part[0]), coordinate(part[1]), SQUARE_X, SQUARE_Y))

        #Handle losing case
        if(len(snake) > 1):
            for i in range(1,len(snake)):
                if(snake[i][0] == SNAKE_X and snake[i][1] == SNAKE_Y):
                    print("YOUR FINAL SCORE: " + str(snake_length))
                    running = False;

        #Snake loops when it goes out of bounds.
        if(coordinate(SNAKE_X) == coordinate(20)):
            SNAKE_X = 0
        if(coordinate(SNAKE_X) == coordinate(-1)):
            SNAKE_X = 20

        if(coordinate(SNAKE_Y) == coordinate(20)):
            SNAKE_Y = 0
        if(coordinate(SNAKE_Y) == coordinate(-1)):
            SNAKE_Y = 20
        
        #This is where we handle poping and appending to the snake list so that it moves.
        snake.append((SNAKE_X,SNAKE_Y))
        if len(snake) > snake_length:
            del snake[0]

        #Checking to see if the snake has touched the food.
        if coordinate(SNAKE_X) == food_x and coordinate(SNAKE_Y) == food_y:
            food_x = coordinate(random.randint(0,19))
            food_y = coordinate(random.randint(0,19)) 
            snake_length += 1
            print("Score is now: " + str(snake_length))

        #Drawing the little dots.
        for row in range(1, int(500/25)):
            for column in range(1,int(500/25)):
                pygame.draw.line(screen, (0,0,0), (SQUARE_X*row,SQUARE_Y*column),(SQUARE_X*row,SQUARE_Y*column))

        # Flip the display
        pygame.display.flip()

# Done! Time to quit.
main()
pygame.quit()