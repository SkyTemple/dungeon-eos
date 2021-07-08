from RandomGen import *
from DungeonAlgorithm import *

# This test uses PIL to show the final map
# Make sure PIL is installed to run this
# PIL is not required for the main algorithm
from PIL import Image

"""
# To use specific seeds
RandomGenerator.gen_type = 0
RandomGenerator.count = 1
RandomGenerator.seed_old_t0 = 0x0233A86C
RandomGenerator.seed_t0 = 0x059CFB28
RandomGenerator.use_seed_t1 = 4
RandomGenerator.seeds_t1 = [0x80CAA4C8, 0x0024ED91, 0x0024ED91, 0x0024ED91, 0x728E13F8]
"""

# A test with several parameters
Properties.layout = 10
Properties.mh_chance = 100
Properties.kecleon_chance = 100
Properties.middle_room_secondary = 10
Properties.nb_rooms = 5
Properties.bit_flags = 0x0
Properties.floor_connectivity = 3
Properties.maze_chance = 0
Properties.dead_end = 0
Properties.extra_hallways = 40
Properties.secondary_density = 0
Properties.enemy_density = 4
Properties.item_density = 1
Properties.buried_item_density = 0
Properties.trap_density = 3
StaticParam.PATCH_APPLIED = 0
StaticParam.FIX_DEAD_END_ERROR = 0
StaticParam.FIX_OUTER_ROOM_ERROR = 0
StaticParam.SHOW_ERROR = 0

NB_TRIES = 1

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
        elif DungeonData.list_tiles[x][y].terrain_flags&0x40 and DungeonData.list_tiles[x][y].terrain_flags&0x3==1:
            rooms.append(10) # Monster House
        elif DungeonData.list_tiles[x][y].terrain_flags&0x20 and DungeonData.list_tiles[x][y].terrain_flags&0x3==1:
            rooms.append(11) # Kecleon Shop
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
               255,255,255,
               255,128,0,
               0,96,0]+[0,0,0]*244)
im.save("layout.png")
