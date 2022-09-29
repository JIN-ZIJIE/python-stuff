from ursina import *

def update():
    firstEntity.rotation_y += 50 * time.dt

    firstEntity.position += firstEntity.forward * time.dt

application.development_mode = False

app = Ursina()

window.fullscreen = False
window.borderless = False

firstEntity = Entity(model = 'cube',
                     color = color.rgb(215, 255, 0),
                     texture = 'brick',

                     position = (0,0,0),
                     rotation = (0,0,0),
                     scale = 2,
                     )

secondEntity = Entity(parent = firstEntity,
                     model = 'sphere',
                     color = color.rgb(215, 255, 0),
                     texture = 'brick',

                     position = (1,1,1),
                     )

EditorCamera()

app.run()
