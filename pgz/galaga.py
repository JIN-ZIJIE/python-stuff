import pgzrun

WIDTH = 1200
HEIGHT = 1000

BLUE = (70, 130, 180)

def update():
    if keyboard.left:
        ship.x -= 10
    elif keyboard.right:
        ship.x += 10

ship = Actor('galaga')
ship.x = WIDTH//2
ship.y = HEIGHT-100



def draw():
    screen.clear()
    screen.fill(BLUE)
    ship.draw()

pgzrun.go()
