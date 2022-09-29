from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from numpy import floor
import random

app = Ursina()

window.fullscreen = False

block_layer = random.randint(-1,2)

tnt_texture = load_texture('Assets/TNT.png')
grass_texture = load_texture('Assets/grass_texture.png')
stone_texture = load_texture('Assets/stone_texture.png')
brick_texture = load_texture('Assets/brick_texture.png')
gold_texture = load_texture('Assets/gold_texture.png')
diamond_texture = load_texture('Assets/diamond_texture.png')
wood_plank_texture = load_texture('Assets/wooden_plank_texture.png')
wood_texture = load_texture('Assets/wood_texture.png')
iron_ore_texture = load_texture('Assets/iron_texture.png')
crafting = load_texture('Assets/crafting_table.png')
leaf = load_texture('Assets/leave_tex.png')
sky_texture = load_texture('Assets/skybox.png')
arm_texture = load_texture('Assets/arm_texture.png')
punch_sound = Audio('Assets/assets_punch_sound', loop = False, autoplay = False)

block_pick = 1

window.fps_counter.enabled = True
window.exit_button.visible = False

def update():
    global block_pick

    if held_keys['1']:
        block_pick = 1
    if held_keys['2']:
        block_pick = 2
    if held_keys['3']:
        block_pick = 3
    if held_keys['4']:
        block_pick = 4
    if held_keys['5']:
        block_pick = 5
    if held_keys['6']:
        block_pick = 6
    if held_keys['7']:
        block_pick = 7
    if held_keys['8']:
        block_pick = 8
    if held_keys['9']:
        block_pick = 9
    
class Voxel(Button):
    def __init__(self, position = (0,0,0), texture = grass_texture):
        super().__init__(
            parent = scene,
            position = position,
            model = 'Assets/block',
            origin_y = 0.5,
            texture = texture,
            color = color.white,
            scale = 1)

    def input(self,key):
        if self.hovered:
            if key == 'left mouse down':
                punch_sound.play()
                if block_pick == 1: voxel = Voxel(position = self.position + mouse.normal, texture = grass_texture)
                if block_pick == 2: voxel = Voxel(position = self.position + mouse.normal, texture = stone_texture)
                if block_pick == 3: voxel = Voxel(position = self.position + mouse.normal, texture = brick_texture)
                if block_pick == 4: voxel = Voxel(position = self.position + mouse.normal, texture = gold_texture)
                if block_pick == 5: voxel = Voxel(position = self.position + mouse.normal, texture = diamond_texture)
                if block_pick == 6: voxel = Voxel(position = self.position + mouse.normal, texture = wood_plank_texture)
                if block_pick == 7: voxel = Voxel(position = self.position + mouse.normal, texture = wood_texture)
                if block_pick == 8: voxel = Voxel(position = self.position + mouse.normal, texture = tnt_texture)
                if block_pick == 9: voxel = Voxel(position = self.position + mouse.normal, texture = crafting)                

            if key == 'right mouse down':
                punch_sound.play()
                destroy(self)

class hand(Entity):
    def __init__(self):
        super().__init__(
            parent = camera.ui,
            model = 'Assets/arm',
            texture = arm_texture,
            scale = 0.2,
            rotation = Vec3(150,-10,0),
            position = Vec2(0.4,-0.6))

class Sky(Entity):
   def __init__(self):
        super().__init__(
            parent = scene,
            model = 'sky_dome',
            texture = sky_texture,
            scale = 1000,
            double_sided = True)

for z in range(20):
    for x in range(20):
        voxel = Voxel(position = (x,-2,z))
    for x in range(20):
        voxel = Voxel(position = (x,-1,z))
    for x in range(20):
        voxel = Voxel(position = (x,0,z))
    for x in range(20):
        voxel = Voxel(position = (x,1,z))
    for x in range(20):
        voxel = Voxel(position = (x,2,z))

player = FirstPersonController(collider = 'mesh')
sky = Sky()
Hand = hand()

app.run()
