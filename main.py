import  pygame
import  time
import  random

snake_speed = 15

#Set window size
window_x = 720
window_y = 480


#Define colors
black = pygame.Color(0,0,0)
white = pygame.Color(255,255,255)
red = pygame.Color(255,0,0)
green = pygame.Color(0,255,0)
blue = pygame.Color(0,0,255)

#Initialize pygame engine
pygame.init()

#Initialize game window
pygame.display.set_caption("SnakeGame")
game_window = pygame.display.set_mode((window_x, window_y))

#FPS
fps = pygame.time.Clock()

#Define snake default position
snake_pos = [100,50]

#Define first four blocks of snake
#Body
snake_body = [  [100, 50],
                [90, 50],
                [80, 50],
                [70,50]
            ]

#Fruit position
fruit_pos = [random.randrange(1, (window_x//10)) * 10,
             random.randrange(1, (window_y//10)) * 10]
fruit_spawn = True

#Set default snake direciton
#Towards right
direction = "RIGHT"
change_to = direction

#Initial score
score = 0

#Display score function
def show_score(choice, color, font, size):
    #Creating font object score_font
    score_font = pygame.font.SysFont(font, size)

    #Create the display surface object
    score_surface = score_font.render('Score : ' + str(score), True, color)

    #Create a rectangular object for the text surface object
    score_rect = score_surface.get_rect()

    #Displaying text
    game_window.blit(score_surface, score_rect)

#Game over function
def game_over():
    #Create font object
    my_font = pygame.font.SysFont('times new roman', 50)

    #Create a text surface on which text will be drawn
    game_over_surface = my_font.render('Your score is : ' + str(score), True, red)
     
    #Create a rectangular object for the text surface object
    game_over_rect = game_over_surface.get_rect()

    #Setting position of the text
    game_over_rect.midtop = (window_x/2, window_y/4)

    #Blit will draw the text on screen
    game_window.blit(game_over_surface, game_over_rect)
    pygame.display.flip()

    #After two seconds we will quit the program
    time.sleep(2)
    raise SystemExit

#Main Function
while True:

    #Handling game events
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP or event.key == pygame.K_w:
                change_to = 'UP'
            if event.key == pygame.K_DOWN or event.key == pygame.K_s:
                change_to = 'DOWN'
            if event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                change_to = 'RIGHT'
            if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                change_to = 'LEFT'
            if event.key == pygame.K_ESCAPE:
                raise SystemExit
        if event.type == pygame.QUIT:
            raise SystemExit
    
    # If two keys pressed simultaneously 
    # we don't want snake to move into two directions
    # simultaneously
    if change_to == 'UP' and direction != 'DOWN':
        direction = 'UP'
    if change_to == 'DOWN' and direction != 'UP':
        direction = 'DOWN'
    if change_to == 'LEFT' and direction != 'RIGHT':
        direction = 'LEFT'
    if change_to == 'RIGHT' and direction != 'LEFT':
        direction = 'RIGHT'

    #Moving the snake
    if direction == 'UP':
        snake_pos[1] -= 10
    if direction == 'DOWN':
        snake_pos[1] += 10
    if direction == 'RIGHT':
        snake_pos[0] += 10
    if direction == 'LEFT':
        snake_pos[0] -= 10
    
    #Snake body growing mechanism
    #if fruits and snakes collide then score increments by 10
    snake_body.insert(0, list(snake_pos))
    if snake_pos[0] == fruit_pos[0] and snake_pos[1] == fruit_pos[1]:
        score += 10
        fruit_spawn = False
    else:
        snake_body.pop()

    if not fruit_spawn:
        fruit_pos = [random.randrange(1, (window_x//10)) * 10,
                     random.randrange(1, (window_y//10)) * 10]
    
    fruit_spawn = True
    #Draw background
    game_window.fill(black)
    #Draw snake
    for pos in snake_body:
        pygame.draw.rect(game_window, green, pygame.Rect(pos[0], pos[1], 10, 10))
    #Draw apple
    pygame.draw.rect(game_window, red, pygame.Rect(fruit_pos[0], fruit_pos[1], 10, 10))

    #Game Over conditions and call
    if snake_pos[0] < 0 or snake_pos[0] > window_x-10:
        game_over()
    if snake_pos[1] < 0 or snake_pos[1] > window_y-10:
        game_over()
    
    #Touching the snake body
    for block in snake_body[1:]:
        if snake_pos[0] == block[0] and snake_pos[1] == block[1]:
            game_over()

    #Draw score
    show_score(1, white, 'times new roman', 20)
    
    #Refresh game screen
    pygame.display.update()

    #Frame Per Second/Refresh Rate
    fps.tick(snake_speed)