from DungeonAlgorithm import *

# This test uses PIL to show the final map
# Make sure PIL is installed to run this
# PIL is not required for the main algorithm
from PIL import Image

# A test with several parameters
Properties.layout = 0
Properties.mh_chance = 0
Properties.kecleon_chance = 0
Properties.middle_room_secondary = 0
Properties.nb_rooms = 0
Properties.bit_flags = 0x0
Properties.floor_connectivity = 1
Properties.maze_chance = 0
Properties.dead_end = 0
Properties.extra_hallways = 0
Properties.secondary_density = 0
Properties.enemy_density = 0
Properties.item_density = 0
Properties.buried_item_density = 0
Properties.trap_density = 0
StaticParam.PATCH_APPLIED = 0
StaticParam.FIX_OUTER_ROOM_ERROR = 0
StaticParam.SHOW_ERROR = 0

NB_TRIES = 5

for x in range(NB_TRIES):
    generate_floor()
    if ReturnData.invalid_generation:
        print("Unsafe generation parameters")
        break

rooms = []
for y in range(32):
    for x in range(56):
        if DungeonData.player_spawn_x==x and DungeonData.player_spawn_y==y:
            rooms.append(8) # Player Spawn
        elif DungeonData.stairs_spawn_x==x and DungeonData.stairs_spawn_y==y:
            rooms.append(9) # Stairs Spawn
        elif DungeonData.list_tiles[x][y].spawn_flags&0x8:
            rooms.append(4) # Enemy
        elif DungeonData.list_tiles[x][y].spawn_flags&0x4:
            rooms.append(5) # Trap
        elif DungeonData.list_tiles[x][y].spawn_flags&0x2:
            if DungeonData.list_tiles[x][y].terrain_flags&0x3==0:
                rooms.append(6) # Buried Item
            else:
                rooms.append(7) # Item
        else:
            rooms.append(DungeonData.list_tiles[x][y].terrain_flags&0x3) # Terrain

im = Image.frombytes(data = bytes(rooms), size=(56,32), mode='P')
im.putpalette([255,0,0,
               0,192,0,
               0,0,255,
               0,0,0,
               192,0,0,
               192,0,192,
               0,128,128,
               0,255,255,
               255,255,0,
               255,255,255]+[0,0,0]*246)
im.save("layout.png")
