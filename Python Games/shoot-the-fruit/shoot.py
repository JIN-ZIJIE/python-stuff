from random import randint
apple = Actor('apple')
orange = Actor('orange')
pineapple = Actor('pineapple')

def draw():
    screen.clear()
    apple.draw()
    orange.draw()
    pineapple.draw()

def place_apple():
    apple.x = randint(10, 800)
    apple.y = randint(10, 600)

#def place_orange():
#    orange.x = randint(10, 800)
#    orange.y = randint(10, 600)
    
#def place_pineapple():
#    pineapple.x = randint(10, 800)
#    pineapple.y = randint(10, 600)

def on_mouse_down(pos):
    if apple.collidepoint(pos):
        print('Good Shot!')
        place_apple()
    else:
        print('You missed!')
        quit()
    
place_apple()
place_orange()
place_pineapple()
