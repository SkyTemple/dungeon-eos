from DungeonAlgorithm import *

# This test uses PIL to show the final map
# Make sure PIL is installed to run this
# PIL is not required for the main algorithm
from PIL import Image

# A test with several parameters
Properties.layout = 10
Properties.mh_chance = 0
Properties.kecleon_chance = 0
Properties.middle_room_secondary = 50
Properties.nb_rooms = 4
Properties.bit_flags = 0x5
Properties.floor_connectivity = 250
Properties.maze_chance = 0
Properties.dead_end = 1
Properties.extra_hallways = 0
Properties.secondary_density = 255
StaticParam.PATCH_APPLIED = 0
StaticParam.FIX_OUTER_ROOM_ERROR = 1

NB_TRIES = 1

for x in range(NB_TRIES):
    generate_floor()
    if ReturnData.invalid_generation:
        print("Unsafe generation parameters")

rooms = []
for y in range(32):
    for x in range(56):
        rooms.append(DungeonData.list_tiles[x][y].terrain_flags)

im = Image.frombytes(data = bytes(rooms), size=(56,32), mode='P')
im.putpalette([255,0,0,
               0,255,0,
               0,0,255,
               255,255,0,
               255,0,255,
               0,255,255,
               255,128,0,
               0,128,255]+[0,0,0]*248)
im.save("Test.png")
