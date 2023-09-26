import pygame
pygame.init()

#colour library
red = (255, 0 , 0)
green = (0, 255, 0)
blue = (0, 0, 255)
white = (255, 255, 255)
black = (0, 0, 0)
purple = (127, 0, 255)
orange = (255, 165, 0)
light_blue =  (0, 127, 255)
cyan =  (0, 255, 255)

screen = pygame.display.set_mode([600, 450])
pygame.display.set_caption('Idle Clicker')
background = black
framerate = 60
font = pygame.font.Font('FreeSansBold.ttf', 16)
timer = pygame.time.Clock()

#game variables
green_value = 1
red_value = 2
orange_value = 3
white_value = 4 
purple_value = 5
cyan_value = 5
lightblue_value = 6
draw_green = False
draw_red = False
draw_orange = False
draw_white = False
draw_purple = False
draw_cyan = False
draw_lightblue = False
red_length = 0
orange_length = 0
green_length = 0
white_length = 0
lightblue_length = 0
cyan_length = 0
purple_length = 0
lightblue_length = 0
red_speed = 1 
orange_speed = 3
green_speed = 5
cyan_speed = 7
lightblue_speed = 8
purple_speed = 11
white_speed = 13
score = 0
white_radius = 0

# drawo buttons function
green_cost = 1
green_owned = False
green_manager_cost = 100

lightblue_cost = 5
lightblue_owned = False
lightblue_manager_cost = 5000

red_cost = 2
red_owned = False
red_manager_cost = 500

orange_cost = 3
orange_owned = False
orange_manager_cost = 1000

white_cost = 4
white_owned = False
white_manager_cost = 2000

purple_cost = 6
purple_owned = False
purple_manager_cost = 60

def draw_task(colour, y_coord, value, draw, length, speed):
    global score
    if draw and length < 200:
        length += speed
    elif length >= 200:
        draw = False
        length = 0
        score += value
    task = pygame.draw.circle(screen, colour, (30, y_coord), 20, 5)
    pygame.draw.rect(screen, colour, [70, y_coord - 15, 200, 30])
    pygame.draw.rect(screen, black, [75, y_coord - 10, 190, 20])
    pygame.draw.rect(screen, colour, [70, y_coord - 15, length, 30])
    value_text = font.render(str(value), True, white)
    screen.blit(value_text, (16, y_coord - 10))
    return task, length, draw

def big_circle(colour, value, draw, radius, speed):
    global score
    if draw and radius < 128:
        radius += speed
    elif radius >= 128:
        draw = False
        radius = 0
        score += value
    
    tasks = pygame.draw.circle(screen, colour, (440, 180), 128, 5)
    pygame.draw.circle(screen, colour, (440, 180), radius, radius)
    return tasks, radius, draw

    
def draw_buttons(colour, x_coord, cost, owned, manager_cost):
    colour_button = pygame.draw.rect(screen, colour, [x_coord, 340, 50, 30])
 
    colour_cost = font.render(str(round(cost, 2)), True, black)
    screen.blit(colour_cost, (x_coord + 6, 350))

    manager_button = pygame.draw.rect(screen, colour, [x_coord, 405, 50, 30])
    manager_text = font.render(str(round(manager_cost,2)), True, black)
    screen.blit(manager_text, (x_coord + 6, 410))
    return colour_button, manager_button



running = True
while running:
    timer.tick(framerate)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if task1.collidepoint(event.pos):
                draw_green = True
            if task2.collidepoint(event.pos):
                draw_red = True
            if task3.collidepoint(event.pos):
                draw_lightblue = True
            if task4.collidepoint(event.pos):
                draw_orange = True
            if task5.collidepoint(event.pos):
                draw_purple = True
            if task_big.collidepoint(event.pos):
                draw_white = True
                                  


    screen.fill(background)
    task1, green_length, draw_green = draw_task(green, 50, green_value, draw_green, green_length, green_speed)
    task2, red_length, draw_red = draw_task(red, 110, red_value, draw_red, red_length, red_speed)
    task3, lightblue_length, draw_lightblue = draw_task(light_blue, 170, lightblue_value, draw_lightblue, lightblue_length, lightblue_speed)
    task4, orange_length, draw_orange = draw_task(orange, 230, orange_value, draw_orange, orange_length, orange_speed)
    task5, purple_length, draw_purple = draw_task(purple, 290, purple_value, draw_purple, purple_length, purple_speed)
    task_big, white_radius, draw_white = big_circle(white, 1, draw_white, white_radius ,white_speed)

    green_buy, green_manager_buy = draw_buttons(green, 10,  green_cost, green_owned, green_manager_cost)
    red_buy, red_manager_buy = draw_buttons(red, 70,  red_cost, red_owned, red_manager_cost)
    orange_buy, orange_manager_buy = draw_buttons(orange, 130,  orange_cost, orange_owned, orange_manager_cost)
    lightblue_buy, lightblue_manager_buy = draw_buttons(light_blue, 190,  lightblue_cost, lightblue_owned, lightblue_manager_cost)
    purple_buy, purple_manager_buy = draw_buttons(purple, 250,  purple_cost, purple_owned, purple_manager_cost)


    display_score = font.render('Money: $' +str(round(score,2)), True, white, black)
    screen.blit(display_score, (10,5))
    pygame.display.flip()

pygame.quit()

