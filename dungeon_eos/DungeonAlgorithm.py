from dungeon_eos.RandomGen import *


class Properties:  # Floor Properties
    layout = 1
    mh_chance = 0
    kecleon_chance = 0
    middle_room_secondary = 0
    nb_rooms = 4
    bit_flags = 0x1
    floor_connectivity = 15
    maze_chance = 0
    dead_end = 0
    extra_hallways = 0
    secondary_density = 10
    empty_mh_chance = 0
    enemy_density = 0
    item_density = 0
    buried_item_density = 0
    trap_density = 0
    fixed_floor_number = 0
    hidden_stairs_type = 0


class TileData:
    TRANS_TABLE = {
        0x0: "terrain_flags",
        0x2: "spawn_flags",
        0x4: "tex_index",
        0x6: "unk1",
        0x7: "room_index",
        0x8: "normal_movement",
        0x9: "secondary_movement",
        0xA: "void_movement",
        0xB: "wall_movement",
        0xC: "monster_ptr",
        0x10: "non_monster_ptr",
    }

    def __init__(self):
        self[0x0] = 0
        self[0x2] = 0
        self[0x4] = 0
        self[0x6] = 0
        self[0x7] = 0xFF
        self[0x8] = 0
        self[0x9] = 0
        self[0xA] = 0
        self[0xB] = 0
        self[0xC] = 0
        self[0x10] = 0

    def __getitem__(self, index):
        return getattr(self, TileData.TRANS_TABLE[index])

    def __setitem__(self, index, value):
        setattr(self, TileData.TRANS_TABLE[index], value)


class StaticParam:
    MERGE_CHANCE = 5  # Originally 5%
    IMPERFECT_CHANCE = 60  # Originally 60%
    SECONDARY_CHANCE = 80  # Originally 80%
    MH_NORMAL_SPAWN_ENM = 30  # Originally 30
    MH_NORMAL_SPAWN_ITEM = 7  # Originally 7
    MH_MIN_TRAP_DUNGEON = 28  # Originally 28
    PATCH_APPLIED = 0
    FIX_DEAD_END_ERROR = 0
    FIX_OUTER_ROOM_ERROR = 0
    SHOW_ERROR = 0

    DEFAULT_TILE = TileData()

    # US: 0235171C
    LIST_DIRECTIONS = {
        0: 0,
        2: 1,
        4: 1,
        6: 1,
        8: 1,
        10: 0,
        12: 1,
        14: -1,
        16: 0,
        18: -1,
        20: -1,
        22: -1,
        24: -1,
        26: 0,
        28: -1,
        30: 1,
    }
    # US: 02353010
    LIST_CHECKS = [
        1,
        0,
        1,
        0,
        0,
        0,
        0,
        0,
        1,
        0,
        0,
        0,
        0,
        0,
        1,
        0,
        0,
        0,
        0,
        0,
        1,
        0,
        1,
        0,
        0,
        0,
        1,
        0,
        1,
        0,
        0,
        0,
    ]


# US: 0x02353538
class DungeonData:  # Dungeon structure
    maze_value = 0
    dungeon_number = 1  # 0x748
    floor_dungeon_number = 1  # 0x749
    unknown_751 = 1  # 0x751
    free_mode = 1  # 0x75C
    unknown_798 = 0  # 0x798
    create_mh = 0  # 0x40C4
    mh_room = -1  # 0x40C9
    hidden_stairs_type = 0  # 0x40CC
    fixed_floor_number = 0  # 0x40DA
    attempts = 0  # 0x40DE
    mission_flag = 0  # 0x760
    mission_type_1 = 0  # 0x761
    mission_type_2 = 0  # 0x762
    player_spawn_x = -1  # 0xCCE0
    player_spawn_y = -1  # 0xCCE2
    stairs_spawn_x = -1  # 0xCCE4
    stairs_spawn_y = -1  # 0xCCE6
    hidden_stairs_spawn_x = -1  # 0xCCE8
    hidden_stairs_spawn_y = -1  # 0xCCEA
    kecleon_shop_min_x = 0  # 0xCD14
    kecleon_shop_min_y = 0  # 0xCD18
    kecleon_shop_max_x = 0  # 0xCD1C
    kecleon_shop_max_y = 0  # 0xCD20
    nb_items = 0  # 0x12AFA
    guaranteed_item_id = 0  # 0x2C9E8
    floor_dungeon_max = 4  # 0x2CAF4

    def clear_tiles():
        DungeonData.list_tiles = [
            [TileData() for y in range(32)] for x in range(56)
        ]  # 0x40E0

    def clear_fixed_room():
        DungeonData.tiles_fr = [
            [TileData() for y in range(8)] for x in range(8)
        ]  # 0xCD60

    def clear_active_traps():
        DungeonData.active_traps = [0 for i in range(64)]


class StatusData:  # Status structure 0237CFBC
    second_spawn = 0  # 0x0
    has_monster_house = 0  # 0x1
    stairs_room = 0  # 0x2
    has_kecleon_shop = 0  # 0x3
    is_not_valid = 0  # 0x5
    floor_size = 0  # 0x6
    has_maze = 0  # 0x7
    no_enemy_spawn = 0  # 0x8
    kecleon_chance = 100  # 0xC
    mh_chance = 0  # 0x10
    nb_rooms = 0  # 0x14
    middle_room_secondary = 0  # 0x18
    hidden_stairs_spawn_x = 0  # 0x1C
    hidden_stairs_spawn_y = 0  # 0x1E
    kecleon_shop_middle_x = 0  # 0x20
    kecleon_shop_middle_y = 0  # 0x22
    unk_val_24 = 0  # 0x24
    hidden_stairs_type = 0  # 0x2C
    kecleon_shop_min_x = 0  # 0x30
    kecleon_shop_min_y = 0  # 0x34
    kecleon_shop_max_x = 0  # 0x38
    kecleon_shop_max_y = 0  # 0x3C


class ReturnData:  # Special Return Data
    invalid_generation = False


class GridCell:
    TRANS_TABLE = {
        0x0: "start_x",
        0x2: "start_y",
        0x4: "end_x",
        0x6: "end_y",
        0x8: "invalid_cell",
        0x9: "unk1",
        0xA: "is_room",
        0xB: "is_connected",
        0xC: "unk2",
        0xD: "unk3",
        0xE: "is_mh",
        0xF: "unk4",
        0x10: "is_maze",
        0x11: "has_been_merged",
        0x12: "is_merged",
        0x13: "connected_to_top",
        0x14: "connected_to_bottom",
        0x15: "connected_to_left",
        0x16: "connected_to_right",
        0x17: "connected_to_top_2",
        0x18: "connected_to_bottom_2",
        0x19: "connected_to_left_2",
        0x1A: "connected_to_right_2",
        0x1B: "unk5",
        0x1C: "flag_imperfect",
        0x1D: "flag_secondary",
    }

    def __init__(self):
        self[0x0] = 0
        self[0x2] = 0
        self[0x4] = 0
        self[0x6] = 0
        self[0x8] = 0
        self[0x9] = 0
        self[0xA] = 0
        self[0xB] = 0
        self[0xC] = 0
        self[0xD] = 0
        self[0xE] = 0
        self[0xF] = 0
        self[0x10] = 0
        self[0x11] = 0
        self[0x12] = 0
        self[0x13] = 0
        self[0x14] = 0
        self[0x15] = 0
        self[0x16] = 0
        self[0x17] = 0
        self[0x18] = 0
        self[0x19] = 0
        self[0x1A] = 0
        self[0x1B] = 0
        self[0x1C] = 0
        self[0x1D] = 0

    def __getitem__(self, index):
        return getattr(self, GridCell.TRANS_TABLE[index])

    def __setitem__(self, index, value):
        setattr(self, GridCell.TRANS_TABLE[index], value)


# US: 0233CF84
def generate_grid_positions(max_nb_room_x, max_nb_room_y):
    sum_x = 0
    list_x = []
    for x in range(max_nb_room_x + 1):
        list_x.append(sum_x)
        sum_x += 0x38 // max_nb_room_x
    sum_y = 0
    list_y = []
    for y in range(max_nb_room_y + 1):
        list_y.append(sum_y)
        sum_y += 0x20 // max_nb_room_y
    return list_x, list_y


# US: 0233D004
def init_grid(max_nb_room_x, max_nb_room_y):
    grid = [[GridCell() for y in range(15)] for z in range(15)]
    for x in range(max_nb_room_x):
        for y in range(max_nb_room_y):
            if StatusData.floor_size == 1 and x >= max_nb_room_x // 2:
                grid[x][y][8] = 1
            elif StatusData.floor_size == 2 and x >= max_nb_room_x * 3 // 4:
                grid[x][y][8] = 1
            else:
                grid[x][y][8] = 0
            grid[x][y][10] = 1  # Create room
    return grid


# US: 0233D104
def place_rooms(grid, max_nb_room_x, max_nb_room_y, nb_rooms):
    rnd = randrange(3)
    if nb_rooms < 0:
        nb_rooms = -nb_rooms
    else:
        nb_rooms += rnd
    # nb_rooms True, rest False
    rooms_ok = [(x < nb_rooms) for x in range(256)]
    max_rooms = max_nb_room_x * max_nb_room_y
    # Shuffle rooms_ok
    for x in range(0x40):
        a = randrange(max_rooms)
        b = randrange(max_rooms)
        tmp = rooms_ok[a]
        rooms_ok[a] = rooms_ok[b]
        rooms_ok[b] = tmp
    StatusData.nb_rooms = 0
    odd_x = max_nb_room_x % 2
    counter = 0
    for x in range(max_nb_room_x):
        for y in range(max_nb_room_y):
            if grid[x][y][8] == 0:  # valid cell
                if StatusData.nb_rooms >= 0x20:
                    # Too many rooms; always remove
                    grid[x][y][10] = 0
                # random 1 or 0 from the shuffled array; randomly
                # create/remove the room
                if rooms_ok[counter]:
                    grid[x][y][10] = 1  # create room
                    StatusData.nb_rooms += 1
                    if odd_x and y == 1 and x == (max_nb_room_x - 1) // 2:
                        # never make a room at (x_mid, 1)?
                        grid[x][y][10] = 0
                else:
                    grid[x][y][10] = 0  # remove room
                counter += 1
    if StatusData.nb_rooms >= 2:
        # Enough rooms
        return

    # Need at least 2 rooms;
    # randomly try grid cells until a room can be created
    attempts = 0
    ok = False
    while attempts < 200 and not ok:
        for x in range(max_nb_room_x):
            for y in range(max_nb_room_y):
                if grid[x][y][8] == 0:
                    if randrange(100) < 60:
                        grid[x][y][10] = 1
                        ok = True
                        break
            if ok:
                break
        attempts += 1
    StatusData.second_spawn = 0


# US: 0233D318
def create_rooms(grid, max_nb_room_x, max_nb_room_y, list_x, list_y, flags):
    imperfect = flags & 0x4
    room_number = 0
    for y in range(max_nb_room_y):
        cur_val_y = list_y[y]
        next_val_y = list_y[y + 1]
        for x in range(max_nb_room_x):
            cur_val_x = list_x[x]
            next_val_x = list_x[x + 1]
            range_x = next_val_x - cur_val_x - 4
            range_y = next_val_y - cur_val_y - 3
            if grid[x][y][8] == 0:
                if grid[x][y][10] == 0:
                    # This grid cell does not have a room;
                    # create a hallway anchor
                    unk_x1 = 2
                    unk_x2 = 4
                    if x == 0:
                        unk_x1 = 1
                    if x == max_nb_room_x - 1:
                        unk_x2 = 2
                    unk_y1 = 2
                    unk_y2 = 4
                    if y == 0:
                        unk_y1 = 1
                    if y == max_nb_room_y - 1:
                        unk_y2 = 2
                    # Pick some random point on the interior of the cell
                    pt_x = randrangeswap(
                        cur_val_x + 2 + unk_x1, cur_val_x + 2 + range_x - unk_x2
                    )
                    pt_y = randrangeswap(
                        cur_val_y + 2 + unk_y1, cur_val_y + 2 + range_y - unk_y2
                    )
                    grid[x][y][0] = pt_x
                    grid[x][y][2] = pt_y
                    grid[x][y][4] = pt_x + 1
                    grid[x][y][6] = pt_y + 1
                    # Open a single tile to serve as a hallway anchor
                    DungeonData.list_tiles[pt_x][pt_y][0] &= ~0x3
                    DungeonData.list_tiles[pt_x][pt_y][0] |= 0x1
                    # room index; set to 0xFE for anchor
                    DungeonData.list_tiles[pt_x][pt_y][7] = 0xFE
                else:
                    # This grid cell has a room
                    size_x = randrangeswap(5, range_x)
                    size_y = randrangeswap(4, range_y)
                    # Force small rooms to have an odd-numbered dimension?
                    if size_x | 1 < range_x:
                        size_x |= 1
                    if size_y | 1 < range_y:
                        size_y |= 1
                    # Constrain the aspect ratio to 2/3 < x/y < 3/2
                    if size_x > size_y * 3 // 2:
                        size_x = size_y * 3 // 2
                    if size_y > size_x * 3 // 2:
                        size_y = size_x * 3 // 2
                    start_x = randrangeforce(range_x - size_x) + cur_val_x + 2
                    end_x = start_x + size_x
                    start_y = randrangeforce(range_y - size_y) + cur_val_y + 2
                    end_y = start_y + size_y
                    # Create the room over the specified coordinates
                    grid[x][y][0] = start_x
                    grid[x][y][2] = start_y
                    grid[x][y][4] = end_x
                    grid[x][y][6] = end_y
                    for room_x in range(start_x, end_x):
                        for room_y in range(start_y, end_y):
                            DungeonData.list_tiles[room_x][room_y][0] &= ~0x3
                            DungeonData.list_tiles[room_x][room_y][0] |= 0x1
                            DungeonData.list_tiles[room_x][room_y][7] = room_number
                    # Randomly flag the room to have a secondary structure
                    flag_secondary = randrange(100) < StaticParam.SECONDARY_CHANCE
                    if StatusData.middle_room_secondary == 0:
                        flag_secondary = 0
                    # Flag the room to have imperfections if specified
                    flag_imp = imperfect
                    if flag_secondary and flag_imp:
                        # If a room is flagged for both a secondary structure
                        # and imperfections, pick one or the other at random
                        if randrange(100) < 50:
                            flag_imp = 0
                        else:
                            flag_secondary = 0
                    if flag_imp:
                        grid[x][y][0x1C] = 1
                    if flag_secondary:
                        grid[x][y][0x1D] = 1
                    room_number += 1


# US: 0233E05C
def create_connections(grid, max_nb_room_x, max_nb_room_y, pt_x, pt_y, prop):
    # Draw a random connection direction.
    # Connect the current cell with the cell to the:
    #   0: east
    #   1: north
    #   2: west
    #   3: south
    direction = randrange(4)
    # Try to connect the current cell to another grid cell, and repeat
    # floor_connectivity times
    for i in range(prop.floor_connectivity):
        # Keep the same connection direction as last iteration with
        # probability 1/2. This "stickiness" or "momentum" encourages multiple
        # rooms to be connected in a straight line, and in a continuous path
        # without too many forks caused by "doubling back"
        test = randrange(8)
        new_direction = randrange(4)
        if test < 4:
            # Shuffle the direction to a new one
            direction = new_direction
        ok = False
        while not ok:
            if direction & 0x3 == 0 and pt_x < max_nb_room_x - 1:
                ok = True
            elif direction & 0x3 == 1 and pt_y > 0:
                ok = True
            elif direction & 0x3 == 2 and pt_x > 0:
                ok = True
            elif direction & 0x3 == 3 and pt_y < max_nb_room_y - 1:
                ok = True
            else:
                # If the selected connection doesn't work, rotate
                # counterclockwise and try again. Since we're masking with 0x3
                # we don't have to worry about overflowing the direction enum
                direction += 1
        direction &= 3
        # Draw the actual connection
        if direction == 0 and grid[pt_x + 1][pt_y][8] == 0:
            # Connect to the east and move to that grid cell
            grid[pt_x][pt_y][0x16] = 1
            grid[pt_x + 1][pt_y][0x15] = 1
            pt_x += 1
        elif direction == 1 and grid[pt_x][pt_y - 1][8] == 0:
            # Connect to the north and move to that grid cell
            grid[pt_x][pt_y][0x13] = 1
            grid[pt_x][pt_y - 1][0x14] = 1
            pt_y -= 1
        elif direction == 2 and grid[pt_x - 1][pt_y][8] == 0:
            # Connect to the west and move to that grid cell
            grid[pt_x][pt_y][0x15] = 1
            grid[pt_x - 1][pt_y][0x16] = 1
            pt_x -= 1
        elif direction == 3 and grid[pt_x][pt_y + 1][8] == 0:
            # Connect to the south and move to that grid cell
            grid[pt_x][pt_y][0x14] = 1
            grid[pt_x][pt_y + 1][0x13] = 1
            pt_y += 1
    if prop.dead_end == 0:
        # Draw extra connections to remove dead end hallways
        more = True
        while more:
            more = False
            # Check all hallway anchors for dead ends
            for y in range(max_nb_room_y):
                for x in range(max_nb_room_x):
                    if grid[x][y][8] == 0 and grid[x][y][10] == 0:
                        count_connect = 0
                        for v in range(0x13, 0x17):
                            if grid[x][y][v] != 0:
                                count_connect += 1
                        if count_connect == 1:
                            # Dead end found. Connect this anchor to a random
                            # other cell to eliminate the dead end
                            direction = randrange(4)
                            ok = False
                            for v in range(8):
                                if (
                                    direction & 0x3 == 0
                                    and pt_x < max_nb_room_x - 1
                                    and grid[x][y][0x16] == 0
                                ):
                                    ok = True
                                elif (
                                    direction & 0x3 == 1
                                    and pt_y > 0
                                    and grid[x][y][0x13] == 0
                                ):
                                    ok = True
                                elif (
                                    direction & 0x3 == 2
                                    and pt_x > 0
                                    and grid[x][y][0x15] == 0
                                ):
                                    ok = True
                                elif (
                                    direction & 0x3 == 3
                                    and pt_y < max_nb_room_y - 1
                                    and grid[x][y][0x14] == 0
                                ):
                                    ok = True
                                else:
                                    direction += 1
                                if ok:
                                    break
                            direction &= 3
                            ### WARNING! Not consistent with the original code!
                            ### That part is bugged in the actual version
                            if StaticParam.FIX_DEAD_END_ERROR:
                                # Draw the connection in the selected direction
                                if direction == 0 and grid[x + 1][y][8] == 0:
                                    grid[x][y][0x16] = 1
                                    grid[x + 1][y][0x15] = 1
                                    # Since we drew another connection, we need
                                    # to iterate over all the cells again since
                                    # the new connection could've created a new
                                    # dead end
                                    more = True
                                    x += 1
                                elif direction == 1 and grid[x][y - 1][8] == 0:
                                    grid[x][y][0x13] = 1
                                    grid[x][y - 1][0x14] = 1
                                    more = True
                                    y -= 1
                                elif direction == 2 and grid[x - 1][y][8] == 0:
                                    grid[x][y][0x15] = 1
                                    grid[x - 1][y][0x16] = 1
                                    more = True
                                    x -= 1
                                elif direction == 3 and grid[x][y + 1][8] == 0:
                                    grid[x][y][0x14] = 1
                                    grid[x][y + 1][0x13] = 1
                                    more = True
                                    y += 1
                            else:
                                if direction == 0 and grid[x + 1][y][8] == 0:
                                    grid[x][y][0x16] = 1
                                    grid[x + 1][y][0x15] = 1
                                    more = True
                                    x += 1
                                # Note: wrong grid index in the validity check
                                elif direction == 1 and grid[x + 1][y][8] == 0:
                                    grid[x][y][0x13] = 1
                                    grid[x][y - 1][0x14] = 1
                                    more = True
                                    y -= 1
                                # Note: wrong grid index in the validity check
                                elif direction == 2 and grid[x + 1][y][8] == 0:
                                    grid[x][y][0x15] = 1
                                    grid[x - 1][y][0x16] = 1
                                    more = True
                                    x -= 1
                                # Note: wrong grid index in the validity check
                                elif direction == 3 and grid[x + 1][y][8] == 0:
                                    grid[x][y][0x14] = 1
                                    grid[x][y + 1][0x13] = 1
                                    more = True
                                    y += 1


# US: 0233F120
# Create a hallway between two points
def process_hallway(pt_x, pt_y, pt2_x, pt2_y, vertical, list_val_x, list_val_y):
    dep_pt_x = pt_x
    dep_pt_y = pt_y
    if vertical == 0:
        # Horizontal hallway
        counter = 0
        # Create the horizonatal line between the starting point and the grid
        # cell boundary
        while pt_x != list_val_x:
            if counter >= 56:  # Sanity check
                return
            counter += 1
            if DungeonData.list_tiles[pt_x][pt_y][0] & 0x3 == 1:
                # If open floor is hit during hall creation, stop prematurely;
                # This hall has connected up with an existing hall
                if dep_pt_x != pt_x:
                    return
            else:
                DungeonData.list_tiles[pt_x][pt_y][0] &= ~0x3
                DungeonData.list_tiles[pt_x][pt_y][0] |= 0x1
            if pt_x >= list_val_x:
                pt_x -= 1
            else:
                pt_x += 1
        counter = 0
        # Create the vertical line to connect the horizontal lines at two
        # different y values
        while pt_y != pt2_y:
            if counter >= 56:
                return
            counter += 1
            if DungeonData.list_tiles[pt_x][pt_y][0] & 0x3 == 1:
                if dep_pt_x != pt_x or dep_pt_y != pt_y:
                    return
            else:
                DungeonData.list_tiles[pt_x][pt_y][0] &= ~0x3
                DungeonData.list_tiles[pt_x][pt_y][0] |= 0x1
            if pt_y >= pt2_y:
                pt_y -= 1
            else:
                pt_y += 1
        counter = 0
        # Create the horizontal line between the end point and the grid cell
        # boundary
        while pt_x != pt2_x:
            if counter >= 56:
                return
            counter += 1
            if DungeonData.list_tiles[pt_x][pt_y][0] & 0x3 == 1:
                if dep_pt_x != pt_x or dep_pt_y != pt_y:
                    return
            else:
                DungeonData.list_tiles[pt_x][pt_y][0] &= ~0x3
                DungeonData.list_tiles[pt_x][pt_y][0] |= 0x1
            if pt_x >= pt2_x:
                pt_x -= 1
            else:
                pt_x += 1
    else:
        # Vertical hallway
        counter = 0
        # Create the vertical line between the starting point and the grid
        # cell boundary
        while pt_y != list_val_y:
            if counter >= 56:
                return
            counter += 1
            if DungeonData.list_tiles[pt_x][pt_y][0] & 0x3 == 1:
                # If open floor is hit during hall creation, stop prematurely;
                # This hall has connected up with an existing hall
                if dep_pt_y != pt_y:
                    return
            else:
                DungeonData.list_tiles[pt_x][pt_y][0] &= ~0x3
                DungeonData.list_tiles[pt_x][pt_y][0] |= 0x1
            if pt_y >= list_val_y:
                pt_y -= 1
            else:
                pt_y += 1
        counter = 0
        # Create the horizontal line to connect the horizontal lines at two
        # different x values
        while pt_x != pt2_x:
            if counter >= 56:
                return
            counter += 1
            if DungeonData.list_tiles[pt_x][pt_y][0] & 0x3 == 1:
                if dep_pt_x != pt_x or dep_pt_y != pt_y:
                    return
            else:
                DungeonData.list_tiles[pt_x][pt_y][0] &= ~0x3
                DungeonData.list_tiles[pt_x][pt_y][0] |= 0x1
            if pt_x >= pt2_x:
                pt_x -= 1
            else:
                pt_x += 1
        counter = 0
        # Create the vertical line between the end point and the grid cell
        # boundary
        while pt_y != pt2_y:
            if counter >= 56:
                return
            counter += 1
            if DungeonData.list_tiles[pt_x][pt_y][0] & 0x3 == 1:
                if dep_pt_x != pt_x or dep_pt_y != pt_y:
                    return
            else:
                DungeonData.list_tiles[pt_x][pt_y][0] &= ~0x3
                DungeonData.list_tiles[pt_x][pt_y][0] |= 0x1
            if pt_y >= pt2_y:
                pt_y -= 1
            else:
                pt_y += 1


# US: 0233E43C
# Connect grid cells together with hallways
def create_hallways(grid, max_nb_room_x, max_nb_room_y, list_x, list_y, no_merge_rooms):
    # Validate and copy grid connections over to a work array
    for y in range(max_nb_room_y):
        for x in range(max_nb_room_x):
            if grid[x][y][8] != 0:
                # Invalid cell, omit any connections in the work array
                grid[x][y][0x17] = 0
                grid[x][y][0x18] = 0
                grid[x][y][0x19] = 0
                grid[x][y][0x1A] = 0
            else:
                # Valid cell. Prune any cell connections that extend past the
                # grid boundaries
                if x == 0:
                    grid[x][y][0x15] = 0
                if y == 0:
                    grid[x][y][0x13] = 0
                if x == max_nb_room_x - 1:
                    grid[x][y][0x16] = 0
                if y == max_nb_room_y - 1:
                    grid[x][y][0x14] = 0
                # Copy the original grid connections to a work array
                for v in range(0x13, 0x17):
                    grid[x][y][v + 4] = grid[x][y][v]
    for x in range(max_nb_room_x):
        for y in range(max_nb_room_y):
            if grid[x][y][8] == 0:
                if grid[x][y][10] == 0:
                    # Anchor; take the central point
                    pt_x = grid[x][y][0]
                    pt_y = grid[x][y][2]
                else:
                    # Room; take a random point on the interior of the room
                    pt_x = randrange(grid[x][y][0] + 1, grid[x][y][4] - 1)
                    pt_y = randrange(grid[x][y][2] + 1, grid[x][y][6] - 1)
                if grid[x][y][0x17]:
                    # Connect to the cell above
                    if grid[x][y - 1][8] == 0:
                        if grid[x][y - 1][10] == 0:
                            # Anchor; take the central x coordinate
                            pt2_x = grid[x][y - 1][0]
                        else:
                            # Room; take a random x coordinate on the interior
                            pt2_x = randrange(
                                grid[x][y - 1][0] + 1, grid[x][y - 1][4] - 1
                            )
                        # Create the hallway
                        process_hallway(
                            pt_x,
                            grid[x][y][2],
                            pt2_x,
                            grid[x][y - 1][6] - 1,
                            1,
                            list_x[x],
                            list_y[y],
                        )
                    # Mark the connection and remove it from the work array so
                    # we don't try to draw a second connection from the other
                    # direction
                    grid[x][y][0x17] = 0
                    grid[x][y - 1][0x18] = 0
                    grid[x][y][0xB] = 1
                    grid[x][y - 1][0xB] = 1
                if grid[x][y][0x18]:
                    # Connect to the cell below
                    if grid[x][y + 1][8] == 0:
                        if grid[x][y + 1][10] == 0:
                            # Anchor; take the central x coordinate
                            pt2_x = grid[x][y + 1][0]
                        else:
                            # Room; take a random x coordinate on the interior
                            pt2_x = randrange(
                                grid[x][y + 1][0] + 1, grid[x][y + 1][4] - 1
                            )
                        # Create the hallway
                        process_hallway(
                            pt_x,
                            grid[x][y][6] - 1,
                            pt2_x,
                            grid[x][y + 1][2],
                            1,
                            list_x[x],
                            list_y[y + 1] - 1,
                        )
                    # Mark the connection and remove it from the work array so
                    # we don't try to draw a second connection from the other
                    # direction
                    grid[x][y][0x18] = 0
                    grid[x][y + 1][0x17] = 0
                    grid[x][y][0xB] = 1
                    grid[x][y + 1][0xB] = 1
                if grid[x][y][0x19]:
                    # Connect to the cell on the left
                    if grid[x - 1][y][8] == 0:
                        if grid[x - 1][y][10] == 0:
                            # Anchor; take the central y coordinate
                            pt2_y = grid[x - 1][y][2]
                        else:
                            # Room; take a random y coordinate on the interior
                            pt2_y = randrange(
                                grid[x - 1][y][2] + 1, grid[x - 1][y][6] - 1
                            )
                        # Create the hallway.
                        # Using grid[x-1][y][0]-1 is a bug; it should be
                        # grid[x-1][y][4]-1. However, it doesn't matter
                        # because process_hallway has safety checks that make
                        # the end result the same regardless.
                        process_hallway(
                            grid[x][y][0],
                            pt_y,
                            grid[x - 1][y][0] - 1,
                            pt2_y,
                            0,
                            list_x[x],
                            list_y[y],
                        )
                    # Mark the connection and remove it from the work array so
                    # we don't try to draw a second connection from the other
                    # direction
                    grid[x][y][0x19] = 0
                    grid[x - 1][y][0x1A] = 0
                    grid[x][y][0xB] = 1
                    grid[x - 1][y][0xB] = 1
                if grid[x][y][0x1A]:
                    # Connect to the cell on the right
                    if grid[x + 1][y][8] == 0:
                        if grid[x + 1][y][10] == 0:
                            # Anchor; take the central y coordinate
                            pt2_y = grid[x + 1][y][2]
                        else:
                            # Room; take a random y coordinate on the interior
                            pt2_y = randrange(
                                grid[x + 1][y][2] + 1, grid[x + 1][y][6] - 1
                            )
                        # Create the hallway
                        process_hallway(
                            grid[x][y][4] - 1,
                            pt_y,
                            grid[x + 1][y][0],
                            pt2_y,
                            0,
                            list_x[x + 1] - 1,
                            list_y[y],
                        )
                    # Mark the connection and remove it from the work array so
                    # we don't try to draw a second connection from the other
                    # direction
                    grid[x][y][0x1A] = 0
                    grid[x + 1][y][0x19] = 0
                    grid[x][y][0xB] = 1
                    grid[x + 1][y][0xB] = 1
    if no_merge_rooms == 0:
        # Try to merge some connected rooms together
        for x in range(max_nb_room_x):
            for y in range(max_nb_room_y):
                chance = randrange(100)
                # A room can only be merged if it's:
                #   - valid
                #   - connected to another room
                #   - not already merged
                #   - unk1?
                # Only rooms can be merged, not hallway anchors
                if (
                    chance < StaticParam.MERGE_CHANCE
                    and grid[x][y][8] == 0
                    and grid[x][y][0xB] != 0
                    and grid[x][y][0x12] == 0
                    and grid[x][y][0x9] == 0
                    and grid[x][y][10] != 0
                ):
                    rnd_num = randrange(4)
                    # Check the target room under the same merge conditions
                    if (
                        rnd_num == 0
                        and x >= 1
                        and grid[x - 1][y][8] == 0
                        and grid[x - 1][y][0xB] != 0
                        and grid[x - 1][y][0x12] == 0
                        and grid[x - 1][y][0x9] == 0
                        and grid[x - 1][y][10] != 0
                    ):
                        # Merge with the room to the left
                        src_y = min(grid[x - 1][y][2], grid[x][y][2])
                        dst_y = max(grid[x - 1][y][6], grid[x][y][6])
                        src_x = grid[x - 1][y][0]
                        dst_x = grid[x][y][4]
                        # Use original room's index
                        room = DungeonData.list_tiles[grid[x][y][0]][grid[x][y][2]][7]
                        # Carve out the merged room tile by tile
                        for cur_x in range(src_x, dst_x):
                            for cur_y in range(src_y, dst_y):
                                DungeonData.list_tiles[cur_x][cur_y][0] &= ~0x3
                                DungeonData.list_tiles[cur_x][cur_y][0] |= 0x1
                                DungeonData.list_tiles[cur_x][cur_y][7] = room
                        # Update room boundaries
                        grid[x - 1][y][0] = src_x
                        grid[x - 1][y][2] = src_y
                        grid[x - 1][y][4] = dst_x
                        grid[x - 1][y][6] = dst_y
                        # Mark the appropriate merge flags on both rooms
                        grid[x - 1][y][0x12] = 1
                        grid[x][y][0x12] = 1
                        grid[x][y][0xB] = 0
                        grid[x][y][0x11] = 1
                    elif (
                        rnd_num == 1
                        and y >= 1
                        and grid[x][y - 1][8] == 0
                        and grid[x][y - 1][0xB] != 0
                        and grid[x][y - 1][0x12] == 0
                        and grid[x][y - 1][0x9] == 0
                        and grid[x][y - 1][10] != 0
                    ):
                        # Merge with the room above
                        src_x = min(grid[x][y - 1][0], grid[x][y][0])
                        dst_x = max(grid[x][y - 1][4], grid[x][y][4])
                        src_y = grid[x][y - 1][2]
                        dst_y = grid[x][y][6]
                        # Use original room's index
                        room = DungeonData.list_tiles[grid[x][y][0]][grid[x][y][2]][7]
                        # Carve out the merged room tile by tile
                        for cur_x in range(src_x, dst_x):
                            for cur_y in range(src_y, dst_y):
                                DungeonData.list_tiles[cur_x][cur_y][0] &= ~0x3
                                DungeonData.list_tiles[cur_x][cur_y][0] |= 0x1
                                DungeonData.list_tiles[cur_x][cur_y][7] = room
                        # Update room boundaries
                        grid[x][y - 1][0] = src_x
                        grid[x][y - 1][2] = src_y
                        grid[x][y - 1][4] = dst_x
                        grid[x][y - 1][6] = dst_y
                        # Mark the appropriate merge flags on both rooms
                        grid[x][y - 1][0x12] = 1
                        grid[x][y][0x12] = 1
                        grid[x][y][0xB] = 0
                        grid[x][y][0x11] = 1
                    elif (
                        rnd_num == 2
                        and x <= max_nb_room_x - 2
                        and grid[x + 1][y][8] == 0
                        and grid[x + 1][y][0xB] != 0
                        and grid[x + 1][y][0x12] == 0
                        and grid[x + 1][y][0x9] == 0
                        and grid[x + 1][y][10] != 0
                    ):
                        # Merge with the room to the right
                        src_y = min(grid[x + 1][y][2], grid[x][y][2])
                        dst_y = max(grid[x + 1][y][6], grid[x][y][6])
                        src_x = grid[x][y][0]
                        dst_x = grid[x + 1][y][4]
                        # Use original room's index
                        room = DungeonData.list_tiles[grid[x][y][0]][grid[x][y][2]][7]
                        # Carve out the merged room tile by tile
                        for cur_x in range(src_x, dst_x):
                            for cur_y in range(src_y, dst_y):
                                DungeonData.list_tiles[cur_x][cur_y][0] &= ~0x3
                                DungeonData.list_tiles[cur_x][cur_y][0] |= 0x1
                                DungeonData.list_tiles[cur_x][cur_y][7] = room
                        # Update room boundaries
                        grid[x + 1][y][0] = src_x
                        grid[x + 1][y][2] = src_y
                        grid[x + 1][y][4] = dst_x
                        grid[x + 1][y][6] = dst_y
                        # Mark the appropriate merge flags on both rooms
                        grid[x + 1][y][0x12] = 1
                        grid[x][y][0x12] = 1
                        grid[x][y][0xB] = 0
                        grid[x][y][0x11] = 1
                    elif (
                        rnd_num == 3
                        and y <= max_nb_room_y - 2
                        and grid[x][y + 1][8] == 0
                        and grid[x][y + 1][0xB] != 0
                        and grid[x][y + 1][0x12] == 0
                        and grid[x][y + 1][0x9] == 0
                        and grid[x][y + 1][10] != 0
                    ):
                        # Merge with the room below
                        src_x = min(grid[x][y + 1][0], grid[x][y][0])
                        dst_x = max(grid[x][y + 1][4], grid[x][y][4])
                        src_y = grid[x][y][2]
                        dst_y = grid[x][y + 1][6]
                        # Use original room's index
                        room = DungeonData.list_tiles[grid[x][y][0]][grid[x][y][2]][7]
                        # Carve out the merged room tile by tile
                        for cur_x in range(src_x, dst_x):
                            for cur_y in range(src_y, dst_y):
                                DungeonData.list_tiles[cur_x][cur_y][0] &= ~0x3
                                DungeonData.list_tiles[cur_x][cur_y][0] |= 0x1
                                DungeonData.list_tiles[cur_x][cur_y][7] = room
                        # Update room boundaries
                        grid[x][y + 1][0] = src_x
                        grid[x][y + 1][2] = src_y
                        grid[x][y + 1][4] = dst_x
                        grid[x][y + 1][6] = dst_y
                        # Mark the appropriate merge flags on both rooms
                        grid[x][y + 1][0x12] = 1
                        grid[x][y][0x12] = 1
                        grid[x][y][0xB] = 0
                        grid[x][y][0x11] = 1


# US: 0233F424
# Try to force a connection on any unconnected rooms so the grid forms a
# connected graph
def add_hallways(grid, max_nb_room_x, max_nb_room_y, list_x, list_y):
    for x in range(max_nb_room_x):
        for y in range(max_nb_room_y):
            if grid[x][y][8] == 0 and grid[x][y][0xB] == 0 and grid[x][y][0x11] == 0:
                if grid[x][y][10] != 0 and grid[x][y][9] == 0:
                    # Unconnected room
                    rnd_x = randrange(grid[x][y][0] + 1, grid[x][y][4] - 1)
                    rnd_y = randrange(grid[x][y][2] + 1, grid[x][y][6] - 1)
                    if (
                        y > 0
                        and grid[x][y - 1][8] == 0
                        and grid[x][y - 1][0x12] == 0
                        and grid[x][y - 1][0xB] != 0
                    ):
                        # Try to connect with the grid cell above if it's
                        # connected
                        if grid[x][y - 1][10] == 0:
                            # Anchor; take the center x coordinate
                            pt_x = grid[x][y - 1][0]
                        else:
                            # Room; take a random x coordinate on the interior
                            pt_x = randrange(
                                grid[x][y - 1][0] + 1, grid[x][y - 1][4] - 1
                            )
                            pt_y = randrange(
                                grid[x][y - 1][2] + 1, grid[x][y - 1][6] - 1
                            )  # unused variable
                        process_hallway(
                            rnd_x,
                            grid[x][y][2],
                            pt_x,
                            grid[x][y - 1][6] - 1,
                            1,
                            list_x[x],
                            list_y[y],
                        )
                        grid[x][y][0xB] = 1
                        grid[x][y][0x13] = 1
                        grid[x][y - 1][0x14] = 1
                    elif (
                        y < max_nb_room_y - 1
                        and grid[x][y + 1][8] == 0
                        and grid[x][y + 1][0x12] == 0
                        and grid[x][y + 1][0xB] != 0
                    ):
                        # Try to connect with the grid cell below if it's
                        # connected
                        if grid[x][y + 1][10] == 0:
                            # Anchor; take the center x coordinate
                            pt_x = grid[x][y + 1][0]
                        else:
                            # Room; take a random x coordinate on the interior
                            pt_x = randrange(
                                grid[x][y + 1][0] + 1, grid[x][y + 1][4] - 1
                            )
                            pt_y = randrange(
                                grid[x][y + 1][2] + 1, grid[x][y + 1][6] - 1
                            )  # unused variable
                        process_hallway(
                            rnd_x,
                            grid[x][y][6] - 1,
                            pt_x,
                            grid[x][y + 1][2],
                            1,
                            list_x[x],
                            list_y[y + 1] - 1,
                        )
                        grid[x][y][0xB] = 1
                        grid[x][y][0x14] = 1
                        grid[x][y + 1][0x13] = 1
                    elif (
                        x > 0
                        and grid[x - 1][y][8] == 0
                        and grid[x - 1][y][0x12] == 0
                        and grid[x - 1][y][0xB] != 0
                    ):
                        # Try to connect with the grid cell to the left if
                        # it's connected
                        if grid[x - 1][y][10] == 0:
                            # Anchor; take the center y coordinate
                            pt_y = grid[x - 1][y][2]
                        else:
                            # Room; take a random y coordinate on the interior
                            pt_x = randrange(
                                grid[x - 1][y][0] + 1, grid[x - 1][y][4] - 1
                            )  # unused variable
                            pt_y = randrange(
                                grid[x - 1][y][2] + 1, grid[x - 1][y][6] - 1
                            )
                        # This is weird, it should be grid[x][y-1][4]-1
                        process_hallway(
                            grid[x][y][0],
                            rnd_y,
                            grid[x - 1][y][0] - 1,
                            pt_y,
                            0,
                            list_x[x],
                            list_y[y],
                        )
                        grid[x][y][0xB] = 1
                        grid[x][y][0x15] = 1
                        grid[x - 1][y][0x16] = 1
                    elif (
                        x < max_nb_room_x - 1
                        and grid[x + 1][y][8] == 0
                        and grid[x + 1][y][0x12] == 0
                        and grid[x + 1][y][0xB] != 0
                    ):
                        # Try to connect with the grid cell to the right if
                        # it's connected
                        if grid[x + 1][y][10] == 0:
                            # Anchor; take the center y coordinate
                            pt_y = grid[x + 1][y][2]
                        else:
                            # Room; take a random y coordinate on the interior
                            pt_x = randrange(
                                grid[x + 1][y][0] + 1, grid[x + 1][y][4] - 1
                            )  # unused variable
                            pt_y = randrange(
                                grid[x + 1][y][2] + 1, grid[x + 1][y][6] - 1
                            )
                        process_hallway(
                            grid[x][y][4] - 1,
                            rnd_y,
                            grid[x + 1][y][0],
                            pt_y,
                            0,
                            list_x[x + 1] - 1,
                            list_y[y],
                        )
                        grid[x][y][0xB] = 1
                        grid[x][y][0x16] = 1
                        grid[x - 1][y][0x15] = 1
                else:
                    # Unconnected anchor; fill it in with wall tiles and
                    # remove any spawn flags
                    DungeonData.list_tiles[grid[x][y][0]][grid[x][y][2]][0] &= ~0x3
                    DungeonData.list_tiles[grid[x][y][0]][grid[x][y][2]][2] &= ~0x7
    # If there are any rooms that are still unconnected (meaning attempts to
    # connect them failed), fill them in
    for y in range(max_nb_room_y):
        for x in range(max_nb_room_x):
            if (
                grid[x][y][8] == 0
                and grid[x][y][0x11] == 0
                and grid[x][y][0xB] == 0
                and grid[x][y][0xF] == 0
            ):
                for cur_x in range(grid[x][y][0], grid[x][y][4]):
                    for cur_y in range(grid[x][y][2], grid[x][y][6]):
                        # Set to wall terrain
                        DungeonData.list_tiles[cur_x][cur_y][0] &= ~0x3
                        # Remove spawn flags
                        DungeonData.list_tiles[cur_x][cur_y][2] &= ~0x7
                        # Set room index to 0xFF (not a room)
                        DungeonData.list_tiles[cur_x][cur_y][7] = 0xFF


# US: 0233F900
def store_check_tile(tile_dat, secondary, room):
    tile_dat[0] &= ~0x3
    if secondary != 0 and tile_dat[7] == room:
        tile_dat[0] |= 0x2


# US: 023406D4
# Random walk with a 2-tile stride, placing obstacles along the way,
# starting from some point and ending when the random walk becomes trapped
# with no more open terrain to walk into
def line_maze(pt_x, pt_y, pt2_x, pt2_y, pt3_x, pt3_y, secondary, room):
    ok = True
    while ok:
        direction = randrange(4)
        store_check_tile(DungeonData.list_tiles[pt_x][pt_y], secondary, room)
        ok = False
        for i in range(4):
            direction &= 0x3
            if direction == 0:
                # Right
                val_x = 2
                val_y = 0
            elif direction == 1:
                # Up
                val_x = 0
                val_y = -2
            elif direction == 2:
                # Left
                val_x = -2
                val_y = 0
            elif direction == 3:
                # Down
                val_x = 0
                val_y = 2
            # Check for open terrain two spaces forward
            if pt2_x <= pt_x + val_x < pt3_x and pt2_y <= pt_y + val_y < pt3_y:
                if DungeonData.list_tiles[pt_x + val_x][pt_y + val_y][0] & 0x3 == 1:
                    ok = True
                    break
            # This direction didn't work so try the next one
            direction += 1
        if ok:
            if direction == 0:
                # Right
                store_check_tile(
                    DungeonData.list_tiles[pt_x + 1][pt_y], secondary, room
                )
                pt_x += 2
            elif direction == 1:
                # Up
                store_check_tile(
                    DungeonData.list_tiles[pt_x][pt_y - 1], secondary, room
                )
                pt_y -= 2
            elif direction == 2:
                # Left
                store_check_tile(
                    DungeonData.list_tiles[pt_x - 1][pt_y], secondary, room
                )
                pt_x -= 2
            elif direction == 3:
                # Down
                store_check_tile(
                    DungeonData.list_tiles[pt_x][pt_y + 1], secondary, room
                )
                pt_y += 2


# US: 02340458
# Generate a maze through a series of random walks
def create_maze(grid_cell, secondary):
    grid_cell[0x10] = 1
    StatusData.has_maze = 1
    room = DungeonData.list_tiles[grid_cell[0]][grid_cell[2]][7]
    # Random walks from upper border
    for cur_x in range(grid_cell[0] + 1, grid_cell[4] - 1, 2):
        if DungeonData.list_tiles[cur_x][grid_cell[2] - 1][0] & 0x3 != 1:
            line_maze(
                cur_x,
                grid_cell[2] - 1,
                grid_cell[0],
                grid_cell[2],
                grid_cell[4],
                grid_cell[6],
                secondary,
                room,
            )

    # Right border
    for cur_y in range(grid_cell[2] + 1, grid_cell[6] - 1, 2):
        if DungeonData.list_tiles[grid_cell[4]][cur_y][0] & 0x3 != 1:
            line_maze(
                grid_cell[4],
                cur_y,
                grid_cell[0],
                grid_cell[2],
                grid_cell[4],
                grid_cell[6],
                secondary,
                room,
            )

    # Lower border
    for cur_x in range(grid_cell[0] + 1, grid_cell[4] - 1, 2):
        if DungeonData.list_tiles[cur_x][grid_cell[6]][0] & 0x3 != 1:
            line_maze(
                cur_x,
                grid_cell[6],
                grid_cell[0],
                grid_cell[2],
                grid_cell[4],
                grid_cell[6],
                secondary,
                room,
            )

    # Left border
    for cur_y in range(grid_cell[2] + 1, grid_cell[6] - 1, 2):
        if DungeonData.list_tiles[grid_cell[0] - 1][cur_y][0] & 0x3 != 1:
            line_maze(
                grid_cell[0] - 1,
                cur_y,
                grid_cell[0],
                grid_cell[2],
                grid_cell[4],
                grid_cell[6],
                secondary,
                room,
            )

    # Fill in all the inner tiles with a stride of 2
    for cur_x in range(grid_cell[0] + 3, grid_cell[4] - 3, 2):
        for cur_y in range(grid_cell[2] + 3, grid_cell[6] - 3, 2):
            if DungeonData.list_tiles[cur_x][cur_y][0] & 0x3 == 1:
                if secondary:
                    DungeonData.list_tiles[cur_x][cur_y][0] &= ~0x3
                    DungeonData.list_tiles[cur_x][cur_y][0] |= 0x2
                else:
                    DungeonData.list_tiles[cur_x][cur_y][0] &= ~0x3
                # Do more random walks for good measure
                line_maze(
                    cur_x,
                    cur_y,
                    grid_cell[0],
                    grid_cell[2],
                    grid_cell[4],
                    grid_cell[6],
                    secondary,
                    room,
                )


# US: 02340224
def mazify(grid, max_nb_room_x, max_nb_room_y, maze_chance):
    if maze_chance > 0:
        if randrange(100) < maze_chance:
            if StaticParam.PATCH_APPLIED or DungeonData.maze_value < 0:
                # Count the number of rooms that can be mazified:
                #   - valid
                #   - not a merged room
                #   - connected
                #   - not a monster house
                #   - both dimensions are odd
                nb_valid = 0
                for y in range(max_nb_room_y):
                    for x in range(max_nb_room_x):
                        if (
                            grid[x][y][8] == 0
                            and grid[x][y][0x11] == 0
                            and grid[x][y][0xB] != 0
                            and grid[x][y][10] != 0
                            and grid[x][y][9] == 0
                            and grid[x][y][0xC] == 0
                            and grid[x][y][0xE] == 0
                            and grid[x][y][0xF] == 0
                        ):
                            if (grid[x][y][4] - grid[x][y][0]) & 1 and (
                                grid[x][y][6] - grid[x][y][2]
                            ) & 1:
                                nb_valid += 1
                if nb_valid > 0:
                    # a single 1, the rest 0's
                    values = [i == 0 for i in range(0x100)]
                    # Shuffle values
                    for x in range(0x40):
                        a = randrange(nb_valid)
                        b = randrange(nb_valid)
                        tmp = values[a]
                        values[a] = values[b]
                        values[b] = tmp
                    counter = 0
                    for y in range(max_nb_room_y):
                        for x in range(max_nb_room_x):
                            if (
                                grid[x][y][8] == 0
                                and grid[x][y][0x11] == 0
                                and grid[x][y][0xB] != 0
                                and grid[x][y][10] != 0
                                and grid[x][y][9] == 0
                                and grid[x][y][0xC] == 0
                                and grid[x][y][0xE] == 0
                                and grid[x][y][0xF] == 0
                            ):
                                if (grid[x][y][4] - grid[x][y][0]) & 1 and (
                                    grid[x][y][6] - grid[x][y][2]
                                ) & 1:
                                    # This room can be mazified
                                    if values[counter]:
                                        # Create a maze room
                                        create_maze(grid[x][y], 0)
                                    counter += 1


# US: 022E03B0
def get_floor_type():
    if (
        DungeonData.unknown_798 == 2
        and DungeonData.floor_dungeon_number == DungeonData.unknown_751
    ):
        return 2
    if DungeonData.fixed_floor_number > 0 and DungeonData.fixed_floor_number <= 0x6E:
        # One of the "normal" fixed rooms
        return 1
    return 0


# US: 0233FBE8
def generate_kecleon_shop(grid, max_nb_room_x, max_nb_room_y, kecleon_chance):
    if (
        StatusData.has_monster_house == 0
        and get_floor_type() != 2
        and kecleon_chance != 0
    ):
        if randrange(100) < kecleon_chance:
            # Randomize the order of rooms tried
            list_x = [i for i in range(0xF)]
            list_y = [i for i in range(0xF)]
            for x in range(200):
                a = randrange(0xF)
                b = randrange(0xF)
                tmp = list_x[a]
                list_x[a] = list_x[b]
                list_x[b] = tmp
            for x in range(200):
                a = randrange(0xF)
                b = randrange(0xF)
                tmp = list_y[a]
                list_y[a] = list_y[b]
                list_y[b] = tmp
            for i in range(0xF):
                if list_x[i] < max_nb_room_x:
                    x = list_x[i]
                    for j in range(0xF):
                        if list_y[j] < max_nb_room_y:
                            y = list_y[j]
                            # By this point, we have a random in-bounds grid
                            # cell. It can support a Kecleon shop if it:
                            #   - is valid
                            #   - is a room
                            #   - is not a merged room
                            #   - is connected
                            #   - has no other special features like mazes or
                            #     secondary structures
                            #   - has dimensions of at least 5x4
                            if (
                                grid[x][y][8] == 0
                                and grid[x][y][0x11] == 0
                                and grid[x][y][0x12] == 0
                                and grid[x][y][10] != 0
                                and grid[x][y][0xB] != 0
                                and grid[x][y][9] == 0
                                and grid[x][y][0x10] == 0
                                and grid[x][y][0x1D] == 0
                            ):
                                if (
                                    abs(grid[x][y][0] - grid[x][y][4]) >= 5
                                    and abs(grid[x][y][2] - grid[x][y][6]) >= 4
                                ):
                                    # Create the Kecleon shop
                                    StatusData.has_kecleon_shop = 1
                                    # The shop should span the whole room
                                    StatusData.kecleon_shop_min_x = grid[x][y][0]
                                    StatusData.kecleon_shop_min_y = grid[x][y][2]
                                    StatusData.kecleon_shop_max_x = grid[x][y][4]
                                    StatusData.kecleon_shop_max_y = grid[x][y][6]
                                    if grid[x][y][6] - grid[x][y][2] < 3:
                                        # This should never happen?
                                        StatusData.kecleon_shop_max_y = (
                                            grid[x][y][6] + 1
                                        )
                                    DungeonData.kecleon_shop_min_x = 9999
                                    DungeonData.kecleon_shop_min_y = 9999
                                    DungeonData.kecleon_shop_max_x = -9999
                                    DungeonData.kecleon_shop_max_y = -9999
                                    # Generate the actual shop on the
                                    # interior, leaving a 1-tile border from
                                    # the room walls
                                    for cur_x in range(
                                        StatusData.kecleon_shop_min_x + 1,
                                        StatusData.kecleon_shop_max_x - 1,
                                    ):
                                        for cur_y in range(
                                            StatusData.kecleon_shop_min_y + 1,
                                            StatusData.kecleon_shop_max_y - 1,
                                        ):
                                            # Kecleon shop bit
                                            DungeonData.list_tiles[cur_x][cur_y][
                                                0
                                            ] |= 0x20
                                            # Do not spawn stairs or monsters
                                            DungeonData.list_tiles[cur_x][cur_y][
                                                2
                                            ] &= ~0x9
                                            if cur_x <= DungeonData.kecleon_shop_min_x:
                                                DungeonData.kecleon_shop_min_x = cur_x
                                            if cur_y <= DungeonData.kecleon_shop_min_y:
                                                DungeonData.kecleon_shop_min_y = cur_y
                                            if cur_x >= DungeonData.kecleon_shop_max_x:
                                                DungeonData.kecleon_shop_max_x = cur_x
                                            if cur_y >= DungeonData.kecleon_shop_max_y:
                                                DungeonData.kecleon_shop_max_y = cur_y
                                    for cur_x in range(grid[x][y][0], grid[x][y][4]):
                                        for cur_y in range(
                                            grid[x][y][2], grid[x][y][6]
                                        ):
                                            DungeonData.list_tiles[cur_x][cur_y][
                                                2
                                            ] |= 0x10
                                    StatusData.kecleon_shop_middle_x = (
                                        StatusData.kecleon_shop_min_x
                                        + StatusData.kecleon_shop_max_x
                                    ) // 2
                                    StatusData.kecleon_shop_middle_y = (
                                        StatusData.kecleon_shop_min_y
                                        + StatusData.kecleon_shop_max_y
                                    ) // 2
                                    return


# US: 02349250
def is_current_mission_type(a, b):
    if (
        DungeonData.mission_flag != 0
        and DungeonData.mission_type_1 == a
        and DungeonData.mission_type_2 == b
    ):
        return True
    return False


# US: 02349250
def is_current_mission_special_type():
    if DungeonData.mission_flag != 0:
        if DungeonData.mission_type_1 in [0, 1, 2, 7, 8, 9, 10]:
            return True
    return False


# US: 0233FF9C
def generate_monster_house(grid, max_nb_room_x, max_nb_room_y, mh_chance):
    if mh_chance != 0:
        if randrange(100) < mh_chance:
            if StatusData.has_kecleon_shop == 0:
                if (
                    is_current_mission_type(10, 7)
                    or not is_current_mission_special_type()
                ) and get_floor_type() == 0:
                    nb_valid = 0
                    for x in range(max_nb_room_x):
                        for y in range(max_nb_room_y):
                            # A grid cell can support a Monster House if it:
                            #   - is valid
                            #   - is a room
                            #   - is not a merged room
                            #   - is connected
                            #   - is not a maze
                            if (
                                grid[x][y][8] == 0
                                and grid[x][y][0x11] == 0
                                and grid[x][y][0xC] == 0
                                and grid[x][y][10] != 0
                                and grid[x][y][0xB] != 0
                                and grid[x][y][9] == 0
                                and grid[x][y][0xF] == 0
                                and grid[x][y][0x10] == 0
                            ):
                                nb_valid += 1
                    if nb_valid > 0:
                        # Randomly select an index to become a Monster House
                        values = [i == 0 for i in range(0x100)]
                        for x in range(0x40):
                            a = randrange(nb_valid)
                            b = randrange(nb_valid)
                            tmp = values[a]
                            values[a] = values[b]
                            values[b] = tmp
                        counter = 0
                        for x in range(max_nb_room_x):
                            for y in range(max_nb_room_y):
                                if (
                                    grid[x][y][8] == 0
                                    and grid[x][y][0x11] == 0
                                    and grid[x][y][0xC] == 0
                                    and grid[x][y][10] != 0
                                    and grid[x][y][0xB] != 0
                                    and grid[x][y][9] == 0
                                    and grid[x][y][0xF] == 0
                                    and grid[x][y][0x10] == 0
                                ):
                                    if values[counter]:
                                        # The selected room can support a
                                        # Monster House, so generate one
                                        StatusData.has_monster_house = 1
                                        grid[x][y][0xE] = 1
                                        for cur_x in range(
                                            grid[x][y][0], grid[x][y][4]
                                        ):
                                            for cur_y in range(
                                                grid[x][y][2], grid[x][y][6]
                                            ):
                                                DungeonData.list_tiles[cur_x][cur_y][
                                                    0
                                                ] |= 0x40
                                                DungeonData.mh_room = (
                                                    DungeonData.list_tiles[cur_x][
                                                        cur_y
                                                    ][7]
                                                )
                                        return
                                    counter += 1


# US: 0233C9E8
# Excavate additional hallways via random walks
def generate_extra_hallways(grid, max_nb_room_x, max_nb_room_y, extra_hallways):
    # Try to generate up to the given number of extra hallways
    for i in range(extra_hallways):
        # Choose a random grid cell
        x = randrange(max_nb_room_x)
        y = randrange(max_nb_room_y)
        if (
            grid[x][y][10] != 0
            and grid[x][y][0xB] != 0
            and grid[x][y][8] == 0
            and grid[x][y][0x10] == 0
        ):
            # Choose a random tile in the room
            cur_x = randrange(grid[x][y][0], grid[x][y][4])
            cur_y = randrange(grid[x][y][2], grid[x][y][6])
            # Choose a random cardinal direction
            direction = randrange(4) * 2
            for j in range(3):
                if direction == 0 and y >= max_nb_room_y - 1:
                    direction = 2
                if direction == 2 and x >= max_nb_room_x - 1:
                    direction = 4
                if direction == 4 and y <= 0:
                    direction = 6
                if direction == 6 and x <= 0:
                    direction = 0
            room = DungeonData.list_tiles[cur_x][cur_y][7]
            # Walk in the random direction until out of the room
            ok = True
            while ok:
                if DungeonData.list_tiles[cur_x][cur_y][7] == room:
                    cur_x += StaticParam.LIST_DIRECTIONS[direction * 4]
                    cur_y += StaticParam.LIST_DIRECTIONS[direction * 4 + 2]
                else:
                    ok = False
            # Keep walking in the same direction until an obstacle is
            # encountered
            ok = True
            while ok:
                if DungeonData.list_tiles[cur_x][cur_y][0] & 0x3 == 1:
                    cur_x += StaticParam.LIST_DIRECTIONS[direction * 4]
                    cur_y += StaticParam.LIST_DIRECTIONS[direction * 4 + 2]
                else:
                    ok = False
            # Abort if secondary terrain
            if DungeonData.list_tiles[cur_x][cur_y][0] != 2:
                # Make sure the current tile is at least 2 tiles away from the
                # map border
                valid = True
                for x in range(cur_x - 2, cur_x + 3):
                    for y in range(cur_y - 2, cur_y + 3):
                        if x < 0 or x >= 56 or y < 0 or y >= 32:
                            valid = False
                            break
                    if not valid:
                        break
                if valid:
                    # Rotate 90 degrees counterclockwise and make sure the
                    # tile is not open
                    d = (direction + 2) & 0x6
                    if (
                        DungeonData.list_tiles[
                            cur_x + StaticParam.LIST_DIRECTIONS[d * 4]
                        ][cur_y + StaticParam.LIST_DIRECTIONS[d * 4 + 2]][0]
                        & 0x3
                        != 1
                    ):
                        # Rotate 90 degrees clockwise and make sure the tile
                        # is not open
                        d2 = (direction - 2) & 0x6
                        if (
                            DungeonData.list_tiles[
                                cur_x + StaticParam.LIST_DIRECTIONS[d2 * 4]
                            ][cur_y + StaticParam.LIST_DIRECTIONS[d2 * 4 + 2]][0]
                            & 0x3
                            != 1
                        ):
                            # Number of steps to walk in one direction before
                            # turning
                            steps = randrange(3) + 3
                            while True:
                                if (
                                    cur_x <= 1
                                    or cur_y <= 1
                                    or cur_x >= 55
                                    or cur_y >= 31
                                ):
                                    # Out of bounds or on the 1-tile border of
                                    # impassable walls
                                    break
                                if DungeonData.list_tiles[cur_x][cur_y][0] & 0x3 == 1:
                                    # Open terrain
                                    break
                                if DungeonData.list_tiles[cur_x][cur_y][0] & 0x10:
                                    # Impassable wall
                                    break
                                # This flag prevents a 2x2 square from being
                                # carved out, since that doesn't qualify as a
                                # "hallway"
                                flag = 1
                                # At least one of the three bottom-right
                                # directions must be an obstacle
                                passed = False
                                for v in [(1, 0), (1, 1), (0, 1)]:
                                    if (
                                        DungeonData.list_tiles[cur_x + v[0]][
                                            cur_y + v[1]
                                        ][0]
                                        & 0x3
                                        != 1
                                    ):
                                        passed = True
                                        break
                                if not passed:
                                    flag = 0
                                # At least one of the three top-right
                                # directions must be an obstacle
                                passed = False
                                for v in [(1, 0), (1, -1), (0, -1)]:
                                    if (
                                        DungeonData.list_tiles[cur_x + v[0]][
                                            cur_y + v[1]
                                        ][0]
                                        & 0x3
                                        != 1
                                    ):
                                        passed = True
                                        break
                                if not passed:
                                    flag = 0
                                # At least one of the three bottom-left
                                # directions must be an obstacle
                                passed = False
                                for v in [(-1, 0), (-1, 1), (0, 1)]:
                                    if (
                                        DungeonData.list_tiles[cur_x + v[0]][
                                            cur_y + v[1]
                                        ][0]
                                        & 0x3
                                        != 1
                                    ):
                                        passed = True
                                        break
                                if not passed:
                                    flag = 0
                                # At least one of the three top-left
                                # directions must be an obstacle
                                passed = False
                                for v in [(-1, 0), (-1, -1), (0, -1)]:
                                    if (
                                        DungeonData.list_tiles[cur_x + v[0]][
                                            cur_y + v[1]
                                        ][0]
                                        & 0x3
                                        != 1
                                    ):
                                        passed = True
                                        break
                                if not passed:
                                    flag = 0
                                # Only carve out a tile if it doesn't result
                                # in a 2x2 cavity. If flag is false by this
                                # point, we'll abort shortly due to the
                                # counterclockwise/clockwise neighbor checks
                                if flag:
                                    # Carve out an open tile
                                    DungeonData.list_tiles[cur_x][cur_y][0] &= ~0x3
                                    DungeonData.list_tiles[cur_x][cur_y][0] |= 0x1
                                d = (direction + 2) & 0x6
                                d2 = (direction - 2) & 0x6
                                if (
                                    DungeonData.list_tiles[
                                        cur_x + StaticParam.LIST_DIRECTIONS[d * 4]
                                    ][cur_y + StaticParam.LIST_DIRECTIONS[d * 4 + 2]][0]
                                    & 0x3
                                    == 1
                                ):
                                    # Counterclockwise cardinal direction is
                                    # open
                                    break
                                if (
                                    DungeonData.list_tiles[
                                        cur_x + StaticParam.LIST_DIRECTIONS[d2 * 4]
                                    ][cur_y + StaticParam.LIST_DIRECTIONS[d2 * 4 + 2]][
                                        0
                                    ]
                                    & 0x3
                                    == 1
                                ):
                                    # Clockwise cardinal direction is open
                                    break
                                steps -= 1
                                if steps == 0:
                                    steps = randrange(3) + 3
                                    # Turn left or right with equal probability
                                    sel = randrange(100)
                                    if sel < 50:
                                        direction += 2
                                    else:
                                        direction -= 2
                                    direction &= 6
                                    # If we would step into an invalid grid
                                    # cell, abort
                                    if (
                                        cur_x >= 32
                                        and StatusData.floor_size == 1
                                        and direction == 0x2
                                    ):
                                        break
                                    if (
                                        cur_x >= 48
                                        and StatusData.floor_size == 2
                                        and direction == 0x2
                                    ):
                                        break
                                # Move in the current direction
                                cur_x += StaticParam.LIST_DIRECTIONS[direction * 4]
                                cur_y += StaticParam.LIST_DIRECTIONS[direction * 4 + 2]


# US: 0233ED34
def generate_room_imperfections(grid, max_nb_room_x, max_nb_room_y):
    # For each grid cell
    for x in range(max_nb_room_x):
        for y in range(max_nb_room_y):
            # Grid checks. Note: 0x1C is the flag that enables room
            # imperfections
            if (
                grid[x][y][8] == 0
                and grid[x][y][0x11] == 0
                and grid[x][y][0x12] == 0
                and grid[x][y][10] != 0
                and grid[x][y][0xB] != 0
                and grid[x][y][9] == 0
                and grid[x][y][0x10] == 0
                and grid[x][y][0x1C] != 0
            ):
                # Randomly determine whether this room should have
                # imperfections or not
                if randrange(100) >= StaticParam.IMPERFECT_CHANCE:
                    length = (grid[x][y][4] - grid[x][y][0]) + (
                        grid[x][y][6] - grid[x][y][2]
                    )
                    length = max(length // 4, 1)
                    # Shrink the room from its corners either in the x or y
                    # direction, repeating a number of times equal to the
                    # average room length
                    for counter in range(length):
                        for i in range(2):
                            # Start from one of the four corners
                            # i == 0 means fill in walls counterclockwise
                            # i == 1 means fill in walls clockwise
                            starting_corner = randrange(4)
                            if starting_corner == 0:
                                # Top-left corner
                                pt_x = grid[x][y][0]
                                pt_y = grid[x][y][2]
                                if i == 0:
                                    move_y = 1  # r5
                                    move_x = 0  # r13+0x28
                                else:
                                    move_y = 0
                                    move_x = 1
                            elif starting_corner == 1:
                                # Top-right corner
                                pt_x = grid[x][y][4] - 1
                                pt_y = grid[x][y][2]
                                if i == 0:
                                    move_y = 0
                                    move_x = -1
                                else:
                                    move_y = 1
                                    move_x = 0
                            elif starting_corner == 2:
                                # Bottom-right corner
                                pt_x = grid[x][y][4] - 1
                                pt_y = grid[x][y][6] - 1
                                if i == 0:
                                    move_y = -1
                                    move_x = 0
                                else:
                                    move_y = 0
                                    move_x = -1
                            elif starting_corner == 3:
                                # Bottom-left corner
                                pt_x = grid[x][y][0]
                                pt_y = grid[x][y][6] - 1
                                if i == 0:
                                    move_y = 0
                                    move_x = 1
                                else:
                                    move_y = -1
                                    move_x = 0
                            # Fill in up to five tiles with walls from the
                            # selected starting corner and in the selected
                            # direction. Iterate 10 times because every other
                            # iteration is just moving the tile coordinate to
                            # fill in.
                            for v in range(10):
                                # Position bounds check
                                if (
                                    pt_x >= grid[x][y][0]
                                    and pt_x < grid[x][y][4]
                                    and pt_y >= grid[x][y][2]
                                    and pt_y < grid[x][y][6]
                                ):
                                    # If the tile is open terrain
                                    if DungeonData.list_tiles[pt_x][pt_y][0] & 0x3 == 1:
                                        # Check that there's no hallways
                                        # within 2 spaces from the current
                                        # tile. If there is, skip filling it
                                        # in.
                                        direction = 0
                                        while direction < 8:
                                            next_x = (
                                                pt_x
                                                + StaticParam.LIST_DIRECTIONS[
                                                    direction * 4
                                                ]
                                            )
                                            next_y = (
                                                pt_y
                                                + StaticParam.LIST_DIRECTIONS[
                                                    direction * 4 + 2
                                                ]
                                            )
                                            found = False
                                            for dx in [-1, 0, 1]:
                                                for dy in [-1, 0, 1]:
                                                    if (
                                                        DungeonData.list_tiles[
                                                            next_x + dx
                                                        ][next_y + dy][0]
                                                        & 0x3
                                                        == 1
                                                    ):
                                                        if (
                                                            DungeonData.list_tiles[
                                                                next_x + dx
                                                            ][next_y + dy][7]
                                                            == 0xFF
                                                        ):
                                                            found = True
                                                            break
                                                if found:
                                                    break
                                            if found:
                                                break
                                            direction += 1
                                        # direction == 8 means no hallways
                                        # were found and we're good to proceed
                                        if direction == 8:
                                            # Check the cardinal neighbors for
                                            # the expected terrain layout.
                                            # This ensures that imperfections
                                            # only extend out from existing
                                            # corners, rather than growing in
                                            # some weird fashion
                                            base = starting_corner * 8
                                            direction = 0
                                            while direction < 8:
                                                next_x = (
                                                    pt_x
                                                    + StaticParam.LIST_DIRECTIONS[
                                                        direction * 4
                                                    ]
                                                )
                                                next_y = (
                                                    pt_y
                                                    + StaticParam.LIST_DIRECTIONS[
                                                        direction * 4 + 2
                                                    ]
                                                )
                                                if (
                                                    DungeonData.list_tiles[next_x][
                                                        next_y
                                                    ][0]
                                                    & 0x3
                                                    == 1
                                                ):
                                                    # Neighbor terrain is open
                                                    # floor
                                                    is_open = 1
                                                else:
                                                    is_open = 0
                                                if (
                                                    StaticParam.LIST_CHECKS[
                                                        base + direction
                                                    ]
                                                    != is_open
                                                ):
                                                    break
                                                # Advance by 2 so we only check
                                                # cardinal directions
                                                direction += 2
                                            # direction == 8 means the
                                            # neighbors look as we expect
                                            if direction == 8:
                                                # Fill in the current open
                                                # floor tile with a wall
                                                DungeonData.list_tiles[pt_x][pt_y][
                                                    0
                                                ] &= ~0x3
                                        break
                                    else:
                                        # This tile was filled in or is already
                                        # a wall. Move onto the next tile
                                        pt_x += move_x
                                        pt_y += move_y
                                else:
                                    break


# US: 0234087C
def set_unk_20(grid_cell):
    for cur_x in range(grid_cell[0], grid_cell[4]):
        for cur_y in range(grid_cell[2], grid_cell[6]):
            DungeonData.list_tiles[cur_x][cur_y][2] |= 0x20


# US: 023408D0
# Checks if a position is a hallway tile or has one of a cardinal neighbor
def test_room(cur_x, cur_y):
    for dx in [-1, 0, 1]:
        if cur_x + dx < 0:
            continue
        if cur_x + dx >= 56:
            break
        for dy in [-1, 0, 1]:
            if cur_y + dy < 0:
                continue
            if cur_y + dy >= 32:
                break
            if dx != 0 and dy != 0:
                continue
            if (
                DungeonData.list_tiles[cur_x + dx][cur_y + dy][0] & 3 == 1
                and DungeonData.list_tiles[cur_x + dx][cur_y + dy][7] == 0xFF
            ):
                return True
    return False


# US: 0233D674
def generate_room_middle_secondary(grid, max_nb_room_x, max_nb_room_y):
    # Generate "secondary structures" in some rooms
    for y in range(max_nb_room_y):
        for x in range(max_nb_room_x):
            # Valid room that isn't a Monster House/merged room, doesn't have
            # imperfections, and is flagged for a secondary structure
            if (
                grid[x][y][8] == 0
                and grid[x][y][0xE] == 0
                and grid[x][y][0x12] == 0
                and grid[x][y][10] != 0
                and grid[x][y][0x1D] != 0
                and grid[x][y][0x1C] == 0
            ):
                rnd_val = randrange(6)
                if rnd_val == 1 and StatusData.middle_room_secondary > 0:
                    StatusData.middle_room_secondary -= 1
                    if (grid[x][y][4] - grid[x][y][0]) & 1 and (
                        grid[x][y][6] - grid[x][y][2]
                    ) & 1:
                        # Both dimensions are odd. Generate a maze room
                        set_unk_20(grid[x][y])
                        create_maze(grid[x][y], 1)
                    else:
                        middle_x = (grid[x][y][4] + grid[x][y][0]) // 2
                        middle_y = (grid[x][y][6] + grid[x][y][2]) // 2
                        if (
                            grid[x][y][4] - grid[x][y][0] >= 5
                            and grid[x][y][6] - grid[x][y][2] >= 5
                        ):
                            # Both dimensions are at least 5. Generate a
                            # water/lava cross in the center
                            DungeonData.list_tiles[middle_x][middle_y][0] &= ~0x3
                            DungeonData.list_tiles[middle_x][middle_y][0] |= 0x2
                            DungeonData.list_tiles[middle_x][middle_y - 1][0] &= ~0x3
                            DungeonData.list_tiles[middle_x][middle_y - 1][0] |= 0x2
                            DungeonData.list_tiles[middle_x - 1][middle_y][0] &= ~0x3
                            DungeonData.list_tiles[middle_x - 1][middle_y][0] |= 0x2
                            DungeonData.list_tiles[middle_x + 1][middle_y][0] &= ~0x3
                            DungeonData.list_tiles[middle_x + 1][middle_y][0] |= 0x2
                            DungeonData.list_tiles[middle_x][middle_y + 1][0] &= ~0x3
                            DungeonData.list_tiles[middle_x][middle_y + 1][0] |= 0x2
                        else:
                            # Generate a single water/lava spot in the center
                            DungeonData.list_tiles[middle_x][middle_y][0] &= ~0x3
                            DungeonData.list_tiles[middle_x][middle_y][0] |= 0x2
                    grid[x][y][9] = 1
                elif rnd_val == 2 and StatusData.middle_room_secondary > 0:
                    if (grid[x][y][4] - grid[x][y][0]) & 1 and (
                        grid[x][y][6] - grid[x][y][2]
                    ) & 1:
                        # Both dimensions are odd. Generate diagonal
                        # stripes/checkerboard of water/lava
                        StatusData.middle_room_secondary -= 1
                        set_unk_20(grid[x][y])
                        for i in range(0x40):
                            rnd_x = randrange(grid[x][y][4] - grid[x][y][0])
                            rnd_y = randrange(grid[x][y][6] - grid[x][y][2])
                            if (rnd_x + rnd_y) & 1:
                                DungeonData.list_tiles[grid[x][y][0] + rnd_x][
                                    grid[x][y][2] + rnd_y
                                ][0] &= ~0x3
                                DungeonData.list_tiles[grid[x][y][0] + rnd_x][
                                    grid[x][y][2] + rnd_y
                                ][0] |= 0x2
                        grid[x][y][9] = 1
                elif rnd_val == 3:
                    if (
                        grid[x][y][4] - grid[x][y][0] >= 5
                        and grid[x][y][6] - grid[x][y][2] >= 5
                    ):
                        rnd_x1 = randrangeswap(grid[x][y][0] + 2, grid[x][y][4] - 3)
                        rnd_y1 = randrangeswap(grid[x][y][2] + 2, grid[x][y][6] - 3)
                        rnd_x2 = randrangeswap(grid[x][y][0] + 2, grid[x][y][4] - 3)
                        rnd_y2 = randrangeswap(grid[x][y][2] + 2, grid[x][y][6] - 3)
                        if StatusData.middle_room_secondary > 0:
                            StatusData.middle_room_secondary -= 1
                            set_unk_20(grid[x][y])
                            if rnd_x1 > rnd_x2:
                                tmp = rnd_x1
                                rnd_x1 = rnd_x2
                                rnd_x2 = tmp
                            if rnd_y1 > rnd_y2:
                                tmp = rnd_y1
                                rnd_y1 = rnd_y2
                                rnd_y2 = tmp
                            # Generate a "pool" of water/lava
                            for cur_x in range(rnd_x1, rnd_x2 + 1):
                                for cur_y in range(rnd_y1, rnd_y2 + 1):
                                    DungeonData.list_tiles[cur_x][cur_y][0] &= ~0x3
                                    DungeonData.list_tiles[cur_x][cur_y][0] |= 0x2
                            grid[x][y][9] = 1
                elif rnd_val == 4:
                    if (
                        grid[x][y][4] - grid[x][y][0] >= 6
                        and grid[x][y][6] - grid[x][y][2] >= 6
                    ):
                        # Both dimensions are at least 6. Generate an "island"
                        # surrounded by water/lava with items and a Warp Tile
                        # at the center
                        middle_x = (grid[x][y][4] + grid[x][y][0]) // 2
                        middle_y = (grid[x][y][6] + grid[x][y][2]) // 2
                        if StatusData.middle_room_secondary > 0:
                            StatusData.middle_room_secondary -= 1
                            set_unk_20(grid[x][y])
                            # Generate water/lava "moat"
                            for t in [
                                (-2, -2),
                                (-1, -2),
                                (0, -2),
                                (1, -2),
                                (-2, -1),
                                (-2, 0),
                                (-2, 1),
                                (-2, 1),
                                (-1, 1),
                                (0, 1),
                                (1, -2),
                                (1, -1),
                                (1, 0),
                                (1, 1),
                            ]:
                                DungeonData.list_tiles[middle_x + t[0]][
                                    middle_y + t[1]
                                ][0] &= ~0x3
                                DungeonData.list_tiles[middle_x + t[0]][
                                    middle_y + t[1]
                                ][0] |= 0x6
                            # Warp Tile
                            DungeonData.list_tiles[middle_x - 1][middle_y - 1][
                                2
                            ] |= 0x54
                            # Items
                            DungeonData.list_tiles[middle_x][middle_y - 1][2] |= 0x12
                            DungeonData.list_tiles[middle_x - 1][middle_y][2] |= 0x12
                            DungeonData.list_tiles[middle_x][middle_y][2] |= 0x12
                            grid[x][y][9] = 1
                elif rnd_val == 5 and StatusData.middle_room_secondary > 0:
                    # Generate a "split room", with two sides separated by a
                    # line of water/lava
                    StatusData.middle_room_secondary -= 1
                    set_unk_20(grid[x][y])
                    if randrange(2) == 0:
                        # Split the room with a horizontal line
                        middle_y = (grid[x][y][6] + grid[x][y][2]) // 2
                        valid = True
                        for i in range(grid[x][y][0], grid[x][y][4]):
                            if test_room(i, middle_y):
                                valid = False
                                break
                        if valid:
                            for i in range(grid[x][y][0], grid[x][y][4]):
                                DungeonData.list_tiles[i][middle_y][0] &= ~0x3
                                DungeonData.list_tiles[i][middle_y][0] |= 0x2
                            for cur_x in range(grid[x][y][0], grid[x][y][4]):
                                for cur_y in range(grid[x][y][2], grid[x][y][6]):
                                    DungeonData.list_tiles[cur_x][cur_y][2] |= 0x80
                            grid[x][y][9] = 1
                    else:
                        # Split the room with a vertical line
                        middle_x = (grid[x][y][4] + grid[x][y][0]) // 2
                        valid = True
                        for i in range(grid[x][y][2], grid[x][y][6]):
                            if test_room(middle_x, i):
                                valid = False
                                break
                        if valid:
                            for i in range(grid[x][y][2], grid[x][y][6]):
                                DungeonData.list_tiles[middle_x][i][0] &= ~0x3
                                DungeonData.list_tiles[middle_x][i][0] |= 0x2
                            for cur_x in range(grid[x][y][0], grid[x][y][4]):
                                for cur_y in range(grid[x][y][2], grid[x][y][6]):
                                    DungeonData.list_tiles[cur_x][cur_y][2] |= 0x80
                            grid[x][y][9] = 1


# US: 0233B028
def generate_normal_floor(max_nb_room_x, max_nb_room_y, prop):
    list_x, list_y = generate_grid_positions(max_nb_room_x, max_nb_room_y)
    grid = init_grid(max_nb_room_x, max_nb_room_y)
    place_rooms(grid, max_nb_room_x, max_nb_room_y, prop.nb_rooms)
    # RandomGenerator.print()
    create_rooms(grid, max_nb_room_x, max_nb_room_y, list_x, list_y, prop.bit_flags)
    # RandomGenerator.print()
    rnd_x = randrange(max_nb_room_x)
    rnd_y = randrange(max_nb_room_y)
    create_connections(grid, max_nb_room_x, max_nb_room_y, rnd_x, rnd_y, prop)
    # RandomGenerator.print()
    create_hallways(grid, max_nb_room_x, max_nb_room_y, list_x, list_y, 0)
    # RandomGenerator.print()
    """
    print("-----------------------------")
    print("%08X" % max_nb_room_x)
    print("%08X" % max_nb_room_y)
    print("-----------------------------")
    for x in range(15):
        for y in range(15):
            c = grid[x][y]
            print("%04X" % c[0])
            print("%04X" % c[2])
            print("%04X" % c[4])
            print("%04X" % c[6])
            print("-----------------------------")
    """
    add_hallways(grid, max_nb_room_x, max_nb_room_y, list_x, list_y)
    # RandomGenerator.print()
    mazify(grid, max_nb_room_x, max_nb_room_y, prop.maze_chance)
    generate_kecleon_shop(grid, max_nb_room_x, max_nb_room_y, StatusData.kecleon_chance)
    generate_monster_house(grid, max_nb_room_x, max_nb_room_y, StatusData.mh_chance)
    # RandomGenerator.print()
    generate_extra_hallways(grid, max_nb_room_x, max_nb_room_y, prop.extra_hallways)
    # RandomGenerator.print()
    generate_room_imperfections(grid, max_nb_room_x, max_nb_room_y)
    # RandomGenerator.print()
    generate_room_middle_secondary(grid, max_nb_room_x, max_nb_room_y)
    # RandomGenerator.print()


# US: 02342B7C
def reset_y_borders():
    for x in range(56):
        DungeonData.list_tiles[x][1] = TileData()
        if x == 0 or x == 55:
            DungeonData.list_tiles[x][1][0] |= 0x10
        DungeonData.list_tiles[x][0x1E] = TileData()
        if x == 0 or x == 55:
            DungeonData.list_tiles[x][0x1E][0] |= 0x10


# US: 02340A78
def delete_status_10():
    for x in range(56):
        for y in range(32):
            if DungeonData.list_tiles[x][y][0] & 0x10:
                DungeonData.list_tiles[x][y][0] &= ~0x3


# US: 0233F93C
def generate_junctions():
    for x in range(56):
        for y in range(32):
            # Open terrain
            if DungeonData.list_tiles[x][y][0] & 3 == 1:
                # Not in a room
                if DungeonData.list_tiles[x][y][7] == 0xFF:
                    # Tile to the left is in a room (or anchor);
                    # mark as a junction
                    if x > 0 and DungeonData.list_tiles[x - 1][y][7] != 0xFF:
                        DungeonData.list_tiles[x - 1][y][0] |= 8
                        # If there's water/lava on the junction tile, remove it
                        if DungeonData.list_tiles[x - 1][y][0] & 3 == 2:
                            DungeonData.list_tiles[x - 1][y][0] &= ~0x3
                            DungeonData.list_tiles[x - 1][y][0] |= 1
                    # Tile above is in a room
                    if y > 0 and DungeonData.list_tiles[x][y - 1][7] != 0xFF:
                        DungeonData.list_tiles[x][y - 1][0] |= 8
                        if DungeonData.list_tiles[x][y - 1][0] & 3 == 2:
                            DungeonData.list_tiles[x][y - 1][0] &= ~0x3
                            DungeonData.list_tiles[x][y - 1][0] |= 1
                    # Tile below is in a room
                    if y < 31 and DungeonData.list_tiles[x][y + 1][7] != 0xFF:
                        DungeonData.list_tiles[x][y + 1][0] |= 8
                        if DungeonData.list_tiles[x][y + 1][0] & 3 == 2:
                            DungeonData.list_tiles[x][y + 1][0] &= ~0x3
                            DungeonData.list_tiles[x][y + 1][0] |= 1
                    # Tile to the right is in a room
                    if x < 55 and DungeonData.list_tiles[x + 1][y][7] != 0xFF:
                        DungeonData.list_tiles[x + 1][y][0] |= 8
                        if DungeonData.list_tiles[x + 1][y][0] & 3 == 2:
                            DungeonData.list_tiles[x + 1][y][0] &= ~0x3
                            DungeonData.list_tiles[x + 1][y][0] |= 1
                # Hallway anchor
                elif DungeonData.list_tiles[x][y][7] == 0xFE:
                    DungeonData.list_tiles[x][y][7] = 0xFF


# US: 02340CAC
def is_out_of_bounds(x, y):
    return x < 0 or x >= 56 or y < 0 or y >= 32


# US: 0234176C
def store_secondary_check(tile):
    if not tile[0] & 0x13:
        tile[0] &= ~0x3
        tile[0] |= 2


# US: 023417AC
# Generate secondary terrain (water/lava) formations
# "Rivers" that flow from top-to-bottom (or bottom-to-top)
# "Lakes", both after rivers and standalone
# Note that because store_secondary_check only lays secondary terrain over
# walls, the formations will not cut through existing rooms (although they are
# allowed to pass through to the other side of the room)
def generate_secondary(test_attrib, prop):
    if prop.bit_flags & test_attrib:
        # Generate 1-3 "river+lake" formations
        nb_gen = [1, 1, 1, 2, 2, 2, 3, 3][randrange(8)]
        for i in range(nb_gen):
            # Randomly pick between starting from the bottom and moving up,
            # or starting from the top and moving down
            if randrange(100) < 50:
                pt_y = 31
                dir_y = -1
                dir_y_upwards = True
            else:
                pt_y = 0
                dir_y = 1
                dir_y_upwards = False
            steps_until_lake = randrange(50) + 10
            # Pick a random column on the interior for the river to start on
            pt_x = randrange(2, 54)
            dir_x = 0
            done = False
            while not done:
                # Fill in tiles in chunks of size 2-7 before changing the flow
                # direction
                for v in range(randrange(6) + 2):
                    if 0 <= pt_x < 56:
                        if 0 <= pt_y < 32:
                            tile = DungeonData.list_tiles[pt_x][pt_y]
                        else:
                            tile = StaticParam.DEFAULT_TILE
                        if tile[0] & 3 == 2:
                            # Stop if we hit existing secondary terrain
                            done = True
                            break
                        if not is_out_of_bounds(pt_x, pt_y):
                            # Fill in secondary terrain as we go
                            store_secondary_check(DungeonData.list_tiles[pt_x][pt_y])
                    # Move to the next tile
                    pt_x += dir_x
                    pt_y += dir_y
                    if pt_y < 0 or pt_y >= 32:
                        # Vertically out of bounds; stop
                        break
                    steps_until_lake -= 1
                    # After a certain number of steps, create a "lake"
                    if steps_until_lake == 0:
                        # Try creating a tile up to 64 times. Note that
                        # There are only 49 possible tiles in the sample space
                        # for this step, but iterating more is useful since
                        # we only lay down secondary terrain if it's near
                        # existing secondary terrain, so repeats allow us to
                        # try a tile more than once
                        for j in range(0x40):
                            # Each tile is in a random location ±3 tiles from
                            # the current cursor in either direction
                            off_x = randrange(7) - 3
                            off_y = randrange(7) - 3
                            # Make sure there's space for the lake with a
                            # 2-tile margin for the map boundary
                            if 2 <= pt_x + off_x < 54 and 2 <= pt_y + off_y < 30:
                                # Create secondary terrain here if it's within
                                # 2 tiles of a like tile; this creates a
                                # "clustering" effect conducive to "lake"
                                # formation
                                second_near = False
                                for x in range(-1, 2):
                                    for y in range(-1, 2):
                                        if x != 0 or y != 0:
                                            if (
                                                DungeonData.list_tiles[
                                                    pt_x + off_x + x
                                                ][pt_y + off_y + y][0]
                                                & 3
                                                == 2
                                            ):
                                                second_near = True
                                                break
                                    if second_near:
                                        break
                                if second_near:
                                    if not is_out_of_bounds(pt_x + off_x, pt_y + off_y):
                                        store_secondary_check(
                                            DungeonData.list_tiles[pt_x + off_x][
                                                pt_y + off_y
                                            ]
                                        )
                        # Finalization/gap-filling step. The random approach
                        # above could've left weird gaps. Now exhaustively go
                        # through the sample space of ±3 in either direction,
                        # and do an online nearest-neighbor interpolation of
                        # secondary terrain tiles to smoothen out the "lake"
                        for off_x in range(-3, 4):
                            for off_y in range(-3, 4):
                                counter = 0
                                if 2 <= pt_x + off_x < 54 and 2 <= pt_y + off_y < 30:
                                    # Count the number of secondary terrain
                                    # tiles adjacent to the current one
                                    for x in range(-1, 2):
                                        for y in range(-1, 2):
                                            if x != 0 or y != 0:
                                                if (
                                                    DungeonData.list_tiles[
                                                        pt_x + off_x + x
                                                    ][pt_y + off_y + y][0]
                                                    & 3
                                                    == 2
                                                ):
                                                    counter += 1
                                    # If at least half of the surrounding
                                    # tiles are secondary terrain, make sure
                                    # that the current tile is also secondary
                                    # terrain
                                    if counter >= 4:
                                        if not is_out_of_bounds(
                                            pt_x + off_x, pt_y + off_y
                                        ):
                                            store_secondary_check(
                                                DungeonData.list_tiles[pt_x + off_x][
                                                    pt_y + off_y
                                                ]
                                            )
                    # Note that after creating a "lake" we aren't technically
                    # done yet. However, in the next iteration we'll probably
                    # hit the stopping condition that the current tile is
                    # secondary terrain. If not, we'll continue making a
                    # river...
                if not done:
                    # Alternate between horizontal and vertical movement each
                    # iteration
                    if dir_x != 0:
                        # The y direction never reverses, which ensures the
                        # "river" doesn't double back on itself and only cuts
                        # across the map once
                        if dir_y_upwards:
                            dir_y = -1
                        else:
                            dir_y = 1
                        dir_x = 0
                    else:
                        # Randomly pick between left and right
                        if randrange(100) < 50:
                            dir_x = -1
                        else:
                            dir_x = 1
                        dir_y = 0
                if pt_y < 0 or pt_y >= 32:
                    # Vertically out of bounds; stop
                    done = True
        # RandomGenerator.print()
        # Generate secondary_density standalone "lakes"
        for i in range(prop.secondary_density):
            # Try to pick a random tile on the interior by brute force to seed
            # the "lake". This should realistically never fail except by freak
            # accident (p = 3e-204).
            attempts = 0
            while attempts < 200:
                rnd_x = randrange(56)
                rnd_y = randrange(32)
                if 1 <= rnd_x < 55 and 1 <= rnd_y < 31:
                    break
                attempts += 1
            if attempts != 200:
                # 10x10 grid with True on the boundary and False on the
                # interior
                table = [
                    [(x == 0 or y == 0 or x == 9 or y == 9) for x in range(10)]
                    for y in range(10)
                ]
                # This forms an "inverse lake" formation
                for v in range(0x50):
                    # Random interior point of the 10x10 grid
                    x = randrange(8) + 1
                    y = randrange(8) + 1
                    # This allows the Trues on the boundary to randomly
                    # "diffuse" inward
                    if (
                        table[x - 1][y]
                        or table[x + 1][y]
                        or table[x][y + 1]
                        or table[x][y - 1]
                    ):
                        table[x][y] = True
                # Iterate through the 10x10 grid
                for x in range(10):
                    for y in range(10):
                        # Checking not table[x][y] inverts the "inverted lake",
                        # which just leaves us with a normal "lake" shape
                        if not table[x][y]:
                            # shift 0-10 -> ±5, so we build a lake that spans
                            # at most ±5 from the "lake seed" tile we chose
                            # earlier
                            if not is_out_of_bounds(rnd_x + x - 5, rnd_y + y - 5):
                                store_secondary_check(
                                    DungeonData.list_tiles[rnd_x + x - 5][rnd_y + y - 5]
                                )
                            else:
                                store_secondary_check(StaticParam.DEFAULT_TILE)
        # Clean up secondary terrain that got in places it shouldn't
        for x in range(56):
            for y in range(32):
                # Secondary terrain
                if DungeonData.list_tiles[x][y][0] & 0x3 == 2:
                    # Revert tiles back to open terrain if:
                    # - in a Kecleon shop,
                    # - in a Monster House
                    # - in impassable walls
                    # - on a stairs spawn point
                    # This probably shouldn't happen since we should never
                    # have laid secondary terrain in a room (i.e. not a wall)
                    # in the first place, but this provides extra safety
                    if (
                        DungeonData.list_tiles[x][y][0] & 0x160
                        or DungeonData.list_tiles[x][y][2] & 0x1
                    ):
                        DungeonData.list_tiles[x][y][0] &= ~0x3
                        DungeonData.list_tiles[x][y][0] |= 1
                    else:
                        # Revert tiles back to walls if on or past the inner
                        # boundary
                        if x <= 1 or x >= 55 or y <= 1 or y >= 31:
                            DungeonData.list_tiles[x][y][0] &= ~0x3


# US: 0233C774
def generate_one_mh_room():
    grid = init_grid(1, 1)
    grid[0][0][0] = 2
    grid[0][0][2] = 2
    grid[0][0][4] = 54
    grid[0][0][6] = 30
    grid[0][0][10] = 1
    grid[0][0][0xB] = 1
    grid[0][0][8] = 0
    for x in range(grid[0][0][0], grid[0][0][4]):
        for y in range(grid[0][0][2], grid[0][0][6]):
            DungeonData.list_tiles[x][y][0] &= ~0x3
            DungeonData.list_tiles[x][y][0] |= 1
            DungeonData.list_tiles[x][y][7] = 0
    generate_monster_house(grid, 1, 1, 999)


# US: 0233B190
def generate_ring(prop):
    max_nb_room_x = 6
    max_nb_room_y = 4
    list_x = [0, 5, 0x10, 0x1C, 0x27, 0x33, 0x38]
    list_y = [2, 7, 0x10, 0x19, 0x1E]
    grid = init_grid(max_nb_room_x, max_nb_room_y)

    # The outer ring has no rooms
    for i in range(6):
        grid[i][0][10] = 0
        grid[i][3][10] = 0

    for i in range(4):
        grid[0][i][10] = 0
        grid[5][i][10] = 0

    # The inner rectangle is all rooms
    for x in range(1, 5):
        for y in range(1, 3):
            grid[x][y][10] = 1
    room_nb = 0
    for y in range(4):
        for x in range(6):
            if grid[x][y][10]:
                # Room
                range_x = list_x[x + 1] - list_x[x] - 3
                range_y = list_y[y + 1] - list_y[y] - 3
                size_x = randrangeswap(5, range_x)
                size_y = randrangeswap(4, range_y)
                start_x = randrangeforce(range_x - size_x) + list_x[x] + 2
                start_y = randrangeforce(range_y - size_y) + list_y[y] + 2
                grid[x][y][0] = start_x
                grid[x][y][2] = start_y
                grid[x][y][4] = start_x + size_x
                grid[x][y][6] = start_y + size_y
                for cur_x in range(start_x, start_x + size_x):
                    for cur_y in range(start_y, start_y + size_y):
                        DungeonData.list_tiles[cur_x][cur_y][0] &= ~0x3
                        DungeonData.list_tiles[cur_x][cur_y][0] |= 1
                        DungeonData.list_tiles[cur_x][cur_y][7] = room_nb
                room_nb += 1
            else:
                # Outer ring
                start_x = randrangeswap(list_x[x] + 1, list_x[x + 1] - 2)
                start_y = randrangeswap(list_y[y] + 1, list_y[y + 1] - 2)
                grid[x][y][0] = start_x
                grid[x][y][2] = start_y
                grid[x][y][4] = start_x + 1
                grid[x][y][6] = start_y + 1
                DungeonData.list_tiles[start_x][start_y][0] &= ~0x3
                DungeonData.list_tiles[start_x][start_y][0] |= 1
                DungeonData.list_tiles[start_x][start_y][7] = 0xFF
    grid[0][0][0x16] = 1
    grid[1][0][0x15] = 1
    grid[1][0][0x16] = 1
    grid[2][0][0x15] = 1
    grid[2][0][0x16] = 1
    grid[3][0][0x15] = 1
    grid[3][0][0x16] = 1
    grid[4][0][0x15] = 1
    grid[4][0][0x16] = 1
    grid[5][0][0x15] = 1
    grid[0][0][0x14] = 1
    grid[0][1][0x13] = 1
    grid[0][1][0x14] = 1
    grid[0][2][0x13] = 1
    grid[0][2][0x14] = 1
    grid[0][3][0x13] = 1
    grid[0][3][0x16] = 1
    grid[1][3][0x15] = 1
    grid[1][3][0x16] = 1
    grid[2][3][0x15] = 1
    grid[2][3][0x16] = 1
    grid[3][3][0x15] = 1
    grid[3][3][0x16] = 1
    grid[4][3][0x15] = 1
    grid[4][3][0x16] = 1
    grid[5][3][0x15] = 1
    grid[5][0][0x14] = 1
    grid[5][1][0x13] = 1
    grid[5][1][0x14] = 1
    grid[5][2][0x13] = 1
    grid[5][2][0x14] = 1
    grid[5][3][0x13] = 1
    rnd_x = randrange(max_nb_room_x)
    rnd_y = randrange(max_nb_room_y)
    create_connections(grid, max_nb_room_x, max_nb_room_y, rnd_x, rnd_y, prop)
    create_hallways(grid, max_nb_room_x, max_nb_room_y, list_x, list_y, 0)
    add_hallways(grid, max_nb_room_x, max_nb_room_y, list_x, list_y)
    generate_kecleon_shop(grid, max_nb_room_x, max_nb_room_y, StatusData.kecleon_chance)
    generate_monster_house(grid, max_nb_room_x, max_nb_room_y, StatusData.mh_chance)
    generate_extra_hallways(grid, max_nb_room_x, max_nb_room_y, prop.extra_hallways)
    generate_room_imperfections(grid, max_nb_room_x, max_nb_room_y)


# US: 0233B61C
def generate_crossroads(prop):
    max_nb_room_x = 5
    max_nb_room_y = 4
    list_x = [0, 0xB, 0x16, 0x21, 0x2C, 0x38]
    list_y = [1, 9, 0x10, 0x17, 0x1F]
    grid = init_grid(max_nb_room_x, max_nb_room_y)
    # The boundary cells are rooms
    for i in range(5):
        grid[i][0][10] = 1
        grid[i][3][10] = 1
    for i in range(4):
        grid[0][i][10] = 1
        grid[4][i][10] = 1

    # Interior cells will only have hallways
    for x in range(1, 4):
        for y in range(1, 3):
            grid[x][y][10] = 0

    # Invalidate the corners
    grid[0][0][8] = 1
    grid[0][3][8] = 1
    grid[4][0][8] = 1
    grid[4][3][8] = 1

    room_nb = 0
    for y in range(4):
        for x in range(5):
            if grid[x][y][8] == 0:
                if grid[x][y][10]:
                    # Rooms
                    range_x = list_x[x + 1] - list_x[x] - 3
                    range_y = list_y[y + 1] - list_y[y] - 3
                    size_x = randrangeswap(5, range_x)
                    size_y = randrangeswap(4, range_y)
                    start_x = randrangeforce(range_x - size_x) + list_x[x] + 2
                    start_y = randrangeforce(range_y - size_y) + list_y[y] + 2
                    grid[x][y][0] = start_x
                    grid[x][y][2] = start_y
                    grid[x][y][4] = start_x + size_x
                    grid[x][y][6] = start_y + size_y
                    for cur_x in range(start_x, start_x + size_x):
                        for cur_y in range(start_y, start_y + size_y):
                            DungeonData.list_tiles[cur_x][cur_y][0] &= ~0x3
                            DungeonData.list_tiles[cur_x][cur_y][0] |= 1
                            DungeonData.list_tiles[cur_x][cur_y][7] = room_nb
                    room_nb += 1
                else:
                    # Hallways
                    start_x = randrangeswap(list_x[x] + 1, list_x[x + 1] - 2)
                    start_y = randrangeswap(list_y[y] + 1, list_y[y + 1] - 2)
                    grid[x][y][0] = start_x
                    grid[x][y][2] = start_y
                    grid[x][y][4] = start_x + 1
                    grid[x][y][6] = start_y + 1
                    DungeonData.list_tiles[start_x][start_y][0] &= ~0x3
                    DungeonData.list_tiles[start_x][start_y][0] |= 1
                    DungeonData.list_tiles[start_x][start_y][7] = 0xFF
    for x in range(1, 4):
        for y in range(3):
            grid[x][y][0x14] = 1
            grid[x][y + 1][0x13] = 1
    for x in range(4):
        for y in range(1, 3):
            grid[x][y][0x16] = 1
            grid[x + 1][y][0x15] = 1
    create_hallways(grid, max_nb_room_x, max_nb_room_y, list_x, list_y, 1)
    add_hallways(grid, max_nb_room_x, max_nb_room_y, list_x, list_y)
    generate_kecleon_shop(grid, max_nb_room_x, max_nb_room_y, StatusData.kecleon_chance)
    generate_monster_house(grid, max_nb_room_x, max_nb_room_y, StatusData.mh_chance)
    generate_extra_hallways(grid, max_nb_room_x, max_nb_room_y, prop.extra_hallways)
    generate_room_imperfections(grid, max_nb_room_x, max_nb_room_y)


# US: 0233C844
def generate_2_rooms_mh():
    max_nb_room_x = 2
    max_nb_room_y = 1
    list_x = [2, 0x1C, 0x36]
    list_y = [2, 0x1E]
    grid = init_grid(max_nb_room_x, max_nb_room_y)
    room_nb = 0
    y = 0
    for x in range(2):
        range_x = list_x[x + 1] - list_x[x] - 3
        range_y = list_y[y + 1] - list_y[y] - 3
        size_x = randrangeswap(10, range_x)
        size_y = randrangeswap(16, range_y)
        start_x = randrangeforce(range_x - size_x) + list_x[x] + 1
        start_y = randrangeforce(range_y - size_y) + list_y[y] + 1
        grid[x][y][0] = start_x
        grid[x][y][2] = start_y
        grid[x][y][4] = start_x + size_x
        grid[x][y][6] = start_y + size_y
        for cur_x in range(start_x, start_x + size_x):
            for cur_y in range(start_y, start_y + size_y):
                DungeonData.list_tiles[cur_x][cur_y][0] &= ~0x3
                DungeonData.list_tiles[cur_x][cur_y][0] |= 1
                DungeonData.list_tiles[cur_x][cur_y][7] = room_nb
        room_nb += 1
    grid[0][0][0x16] = 1
    grid[1][0][0x15] = 1
    create_hallways(grid, max_nb_room_x, max_nb_room_y, list_x, list_y, 0)
    generate_monster_house(grid, max_nb_room_x, max_nb_room_y, 999)


# US: 0233BA7C
def generate_room_line(prop):
    max_nb_room_x = 5
    max_nb_room_y = 1
    list_x = [0, 0xB, 0x16, 0x21, 0x2C, 0x38]
    list_y = [4, 0xF]
    grid = init_grid(max_nb_room_x, max_nb_room_y)
    place_rooms(grid, max_nb_room_x, max_nb_room_y, prop.nb_rooms)
    create_rooms(grid, max_nb_room_x, max_nb_room_y, list_x, list_y, prop.bit_flags)
    rnd_x = randrange(max_nb_room_x)
    rnd_y = randrange(max_nb_room_y)
    create_connections(grid, max_nb_room_x, max_nb_room_y, rnd_x, rnd_y, prop)
    create_hallways(grid, max_nb_room_x, max_nb_room_y, list_x, list_y, 1)
    add_hallways(grid, max_nb_room_x, max_nb_room_y, list_x, list_y)
    generate_kecleon_shop(grid, max_nb_room_x, max_nb_room_y, StatusData.kecleon_chance)
    generate_monster_house(grid, max_nb_room_x, max_nb_room_y, StatusData.mh_chance)
    generate_extra_hallways(grid, max_nb_room_x, max_nb_room_y, prop.extra_hallways)
    generate_room_imperfections(grid, max_nb_room_x, max_nb_room_y)


# US: 0233BBDC
def generate_cross(prop):
    max_nb_room_x = 3
    max_nb_room_y = 3
    list_x = [0xB, 0x16, 0x21, 0x2C]
    list_y = [2, 0xB, 0x14, 0x1E]
    grid = init_grid(max_nb_room_x, max_nb_room_y)
    # All cells are rooms
    for x in range(3):
        for y in range(3):
            grid[x][y][10] = 1
    # Invalidate the corners
    grid[0][0][8] = 1
    grid[0][2][8] = 1
    grid[2][0][8] = 1
    grid[2][2][8] = 1
    create_rooms(grid, max_nb_room_x, max_nb_room_y, list_x, list_y, prop.bit_flags)
    grid[1][0][0x14] = 1
    grid[1][1][0x13] = 1
    grid[1][1][0x14] = 1
    grid[1][2][0x13] = 1
    grid[0][1][0x16] = 1
    grid[1][1][0x15] = 1
    grid[1][1][0x16] = 1
    grid[2][1][0x15] = 1
    create_hallways(grid, max_nb_room_x, max_nb_room_y, list_x, list_y, 1)
    add_hallways(grid, max_nb_room_x, max_nb_room_y, list_x, list_y)
    generate_kecleon_shop(grid, max_nb_room_x, max_nb_room_y, StatusData.kecleon_chance)
    generate_monster_house(grid, max_nb_room_x, max_nb_room_y, StatusData.mh_chance)
    generate_extra_hallways(grid, max_nb_room_x, max_nb_room_y, prop.extra_hallways)
    generate_room_imperfections(grid, max_nb_room_x, max_nb_room_y)


# US: 0233BF30
def merge_rooms(room_x, room_y1, room_y2, grid):
    room_y2 += room_y1
    src_x = min(grid[room_x][room_y1][0], grid[room_x][room_y2][0])
    dst_x = max(grid[room_x][room_y1][4], grid[room_x][room_y2][4])
    src_y = grid[room_x][room_y1][2]
    dst_y = grid[room_x][room_y2][6]
    # Preserve the room index of the first room
    room = DungeonData.list_tiles[grid[room_x][room_y1][0]][grid[room_x][room_y1][2]][7]
    for x in range(src_x, dst_x):
        for y in range(src_y, dst_y):
            # Clear out the aggregate rectangle formed from the two rooms
            DungeonData.list_tiles[x][y][0] &= ~0x3
            DungeonData.list_tiles[x][y][0] |= 0x1
            DungeonData.list_tiles[x][y][7] = room
    # Set new grid cell parameters appropriately
    grid[room_x][room_y1][0] = src_x
    grid[room_x][room_y1][2] = src_y
    grid[room_x][room_y1][4] = dst_x
    grid[room_x][room_y1][6] = dst_y
    grid[room_x][room_y1][0x12] = 1
    grid[room_x][room_y2][0x12] = 1
    grid[room_x][room_y2][0xB] = 0
    grid[room_x][room_y2][0x11] = 1


# US: 0233BD74
def generate_beetle(prop):
    max_nb_room_x = 3
    max_nb_room_y = 3
    list_x = [0x5, 0xF, 0x23, 0x32]
    list_y = [2, 0xB, 0x14, 0x1E]
    grid = init_grid(max_nb_room_x, max_nb_room_y)
    for x in range(3):
        for y in range(3):
            grid[x][y][10] = 1
    create_rooms(grid, max_nb_room_x, max_nb_room_y, list_x, list_y, prop.bit_flags)
    for y in range(3):
        # Connect the rooms within a row together
        grid[0][y][0x16] = 1
        grid[1][y][0x15] = 1
        grid[1][y][0x16] = 1
        grid[2][y][0x15] = 1
    create_hallways(grid, max_nb_room_x, max_nb_room_y, list_x, list_y, 1)
    # Merge the central column into one big room
    merge_rooms(1, 0, 1, grid)
    merge_rooms(1, 0, 2, grid)
    add_hallways(grid, max_nb_room_x, max_nb_room_y, list_x, list_y)
    generate_kecleon_shop(grid, max_nb_room_x, max_nb_room_y, StatusData.kecleon_chance)
    generate_monster_house(grid, max_nb_room_x, max_nb_room_y, StatusData.mh_chance)
    generate_extra_hallways(grid, max_nb_room_x, max_nb_room_y, prop.extra_hallways)
    generate_room_imperfections(grid, max_nb_room_x, max_nb_room_y)


# US: 0233C07C
def generate_outer_room_floor(max_nb_room_x, max_nb_room_y, prop):
    list_x, list_y = generate_grid_positions(max_nb_room_x, max_nb_room_y)
    grid = init_grid(max_nb_room_x, max_nb_room_y)
    # Make all cells into rooms
    for x in range(max_nb_room_x):
        for y in range(max_nb_room_y):
            grid[x][y][10] = 1
    # Invalidate all grid cells on the interior
    for x in range(1, max_nb_room_x - 1):
        for y in range(1, max_nb_room_y - 1):
            grid[x][y][8] = 1
    create_rooms(grid, max_nb_room_x, max_nb_room_y, list_x, list_y, prop.bit_flags)
    if StaticParam.FIX_OUTER_ROOM_ERROR:
        for x in range(max_nb_room_x):
            if x > 0:
                # If not on the left border, connect to the left
                grid[x][0][0x15] = 1
                grid[x][max_nb_room_y - 1][0x15] = 1
            if x < max_nb_room_x - 1:
                # If not on the right border, connect to the right
                grid[x + 1][0][0x16] = 1
                grid[x + 1][max_nb_room_y - 1][0x16] = 1
        for y in range(max_nb_room_y):
            if y > 0:
                # If not on the top border, connect above
                grid[0][y][0x13] = 1
                grid[max_nb_room_x - 1][y][0x13] = 1
            if y < max_nb_room_y - 1:
                # If not on the bottom border, connect below
                grid[0][y + 1][0x14] = 1
                grid[max_nb_room_x - 1][y + 1][0x14] = 1
    else:
        # Normal algorithm has weird conditions
        # However, because of the way create_hallways() works,
        # this actually still leads to the right results as
        # long as max_nb_room_x >= 4
        for x in range(max_nb_room_x - 1):
            if x > 0:
                grid[x][0][0x16] = 1
                grid[x][max_nb_room_y - 1][0x16] = 1
            if x < max_nb_room_x - 2:
                grid[x + 1][0][0x15] = 1
                grid[x + 1][max_nb_room_y - 1][0x15] = 1
        for y in range(max_nb_room_y - 1):
            if y > 0:
                grid[0][y][0x13] = 1
                grid[max_nb_room_x - 1][y][0x13] = 1
            # Glitch on normal algorithm: connections are not made with the
            # last row
            if y < max_nb_room_y - 2:
                grid[0][y][0x14] = 1
                grid[max_nb_room_x - 1][y][0x14] = 1
    create_hallways(grid, max_nb_room_x, max_nb_room_y, list_x, list_y, 0)
    add_hallways(grid, max_nb_room_x, max_nb_room_y, list_x, list_y)
    mazify(grid, max_nb_room_x, max_nb_room_y, prop.maze_chance)
    generate_kecleon_shop(grid, max_nb_room_x, max_nb_room_y, StatusData.kecleon_chance)
    generate_monster_house(grid, max_nb_room_x, max_nb_room_y, StatusData.mh_chance)
    generate_extra_hallways(grid, max_nb_room_x, max_nb_room_y, prop.extra_hallways)
    generate_room_imperfections(grid, max_nb_room_x, max_nb_room_y)
    generate_room_middle_secondary(grid, max_nb_room_x, max_nb_room_y)


# SPECIAL
def generate_maze():
    grid = init_grid(1, 1)
    grid[0][0][0] = 2
    grid[0][0][2] = 2
    grid[0][0][4] = 53
    grid[0][0][6] = 29
    grid[0][0][10] = 1
    grid[0][0][0xB] = 1
    grid[0][0][8] = 0
    for x in range(grid[0][0][0], grid[0][0][4]):
        for y in range(grid[0][0][2], grid[0][0][6]):
            DungeonData.list_tiles[x][y][0] &= ~0x3
            DungeonData.list_tiles[x][y][0] |= 1
    create_maze(grid[0][0], 0)
    for x in range(2, 5):
        for y in range(2, 5):
            DungeonData.list_tiles[x][y][0] &= ~0x3
            DungeonData.list_tiles[x][y][0] |= 1
            DungeonData.list_tiles[x][y][7] = 0x0
    for x in range(2, 5):
        for y in range(26, 29):
            DungeonData.list_tiles[x][y][0] &= ~0x3
            DungeonData.list_tiles[x][y][0] |= 1
            DungeonData.list_tiles[x][y][7] = 0x1
    for x in range(50, 53):
        for y in range(2, 5):
            DungeonData.list_tiles[x][y][0] &= ~0x3
            DungeonData.list_tiles[x][y][0] |= 1
            DungeonData.list_tiles[x][y][7] = 0x2
    for x in range(50, 53):
        for y in range(26, 29):
            DungeonData.list_tiles[x][y][0] &= ~0x3
            DungeonData.list_tiles[x][y][0] |= 1
            DungeonData.list_tiles[x][y][7] = 0x3
    for x in range(26, 29):
        for y in range(14, 17):
            DungeonData.list_tiles[x][y][0] &= ~0x3
            DungeonData.list_tiles[x][y][0] |= 1
            DungeonData.list_tiles[x][y][7] = 0x4


# US: 02342C8C
# Spawn the stairs at the given location
def generate_stairs(spawn, hidden_stairs):
    x = spawn[0]
    y = spawn[1]
    DungeonData.list_tiles[x][y][2] |= 0x1
    DungeonData.list_tiles[x][y][2] &= ~0x2
    if not hidden_stairs:
        # Normal stairs
        DungeonData.stairs_spawn_x = x
        DungeonData.stairs_spawn_y = y
        StatusData.stairs_room = DungeonData.list_tiles[x][y][7]
    else:
        # Hidden stairs
        if StatusData.second_spawn:
            StatusData.hidden_stairs_spawn_x = x
            StatusData.hidden_stairs_spawn_y = y
        else:
            DungeonData.hidden_stairs_spawn_x = x
            DungeonData.hidden_stairs_spawn_y = y
            DungeonData.hidden_stairs_type = hidden_stairs
    # If spawning normal stairs and this is a rescue floor, make the stairs
    # room a Monster House
    if not hidden_stairs and get_floor_type() == 2:
        room = DungeonData.list_tiles[x][y][7]
        for x in range(56):
            for y in range(32):
                if (
                    DungeonData.list_tiles[x][y][0] & 3 == 1
                    and DungeonData.list_tiles[x][y][7] == room
                ):
                    DungeonData.list_tiles[x][y][0] |= 0x40
                    DungeonData.mh_room = DungeonData.list_tiles[x][y][7]


# US: 02340CE4
def shuffle_spawns(valid_spawns):
    # Do twice as many swaps as there are items in the array
    for i in range(len(valid_spawns) * 2):
        a = randrange(len(valid_spawns))
        b = randrange(len(valid_spawns))
        tmp = valid_spawns[a]
        valid_spawns[a] = valid_spawns[b]
        valid_spawns[b] = tmp


# US: 02340D4C
# Spawn all non-enemy entities (stairs, items, traps, player)
def generate_item_spawns(prop, empty):
    ### Spawn stairs
    if DungeonData.stairs_spawn_x == -1 or DungeonData.stairs_spawn_y == -1:
        valid_spawns = []
        for x in range(56):
            for y in range(32):
                # The stairs can spawn on tiles that are:
                # - open terrain
                # - in a room
                # - not in a Kecleon shop
                # - don't already have an enemy spawn
                # - aren't a junction (next to a hallway)
                # - aren't a special tile that can't be broken by Absolute
                #   Mover
                if (
                    DungeonData.list_tiles[x][y][0] & 0x3 == 1
                    and DungeonData.list_tiles[x][y][7] != 0xFF
                    and DungeonData.list_tiles[x][y][0] & 0x20 == 0
                    and DungeonData.list_tiles[x][y][2] & 0x8 == 0
                    and DungeonData.list_tiles[x][y][2] & 0x10 == 0
                    and DungeonData.list_tiles[x][y][0] & 0x8 == 0
                    and DungeonData.list_tiles[x][y][0] & 0x100 == 0
                ):
                    valid_spawns.append((x, y))
        if len(valid_spawns) > 0:
            # Randomly pick one of the valid tiles to spawn the stairs on
            stairs = randrange(len(valid_spawns))
            generate_stairs(valid_spawns[stairs], 0)
            if StatusData.hidden_stairs_type:
                # Also spawn hidden stairs
                # But not where we spawned the normal stairs
                del valid_spawns[stairs]
                # Only spawn hidden stairs if there are at least 2 floors left
                # in the dungeon
                if DungeonData.floor_dungeon_number + 1 < DungeonData.floor_dungeon_max:
                    use_gen_1(3)
                    # Spawn the hidden stairs on any of the valid tiles
                    # besides the one where we spawned the normal stairs
                    stairs = randrange(len(valid_spawns))
                    generate_stairs(valid_spawns[stairs], StatusData.hidden_stairs_type)
                    use_gen_0()
    # RandomGenerator.print()
    ### Spawn normal items
    valid_spawns = []
    for x in range(56):
        for y in range(32):
            # Normal items can spawn on tiles that are:
            # - open terrain
            # - in a room
            # - not in a Kecleon shop
            # - not in a Monster House
            # - not a junction (by a hallway)
            # - not a special tile that can't be broken by Absolute Mover
            if (
                DungeonData.list_tiles[x][y][0] & 0x3 == 1
                and DungeonData.list_tiles[x][y][7] != 0xFF
                and DungeonData.list_tiles[x][y][0] & 0x20 == 0
                and DungeonData.list_tiles[x][y][0] & 0x40 == 0
                and DungeonData.list_tiles[x][y][0] & 0x8 == 0
                and DungeonData.list_tiles[x][y][0] & 0x100 == 0
            ):
                valid_spawns.append((x, y))
    if len(valid_spawns) > 0:
        nb_items = prop.item_density
        if nb_items != 0:
            # Add slight variation in item count
            nb_items = max(randrange(nb_items - 2, nb_items + 2), 1)
        if DungeonData.guaranteed_item_id != 0:
            # Account for a guaranteed item spawn
            nb_items += 1
        DungeonData.nb_items = nb_items + 1
        if nb_items + 1 > 0:
            # Randomly pick among the valid item spawn spots
            shuffle_spawns(valid_spawns)
            start = randrange(len(valid_spawns))
            nb_items += 1
            for i in range(nb_items):
                c = valid_spawns[start]
                start += 1
                if start == len(valid_spawns):
                    # Wrap around to the front
                    start = 0
                # Spawn an item at this location
                DungeonData.list_tiles[c[0]][c[1]][2] |= 0x2
    # RandomGenerator.print()
    ### Spawn buried items (in walls)
    valid_spawns = []
    for x in range(56):
        for y in range(32):
            # Buried items can spawn in any wall tile
            if DungeonData.list_tiles[x][y][0] & 0x3 == 0:
                valid_spawns.append((x, y))
    if len(valid_spawns) > 0:
        # Same procedure as with normal items
        nb_items = prop.buried_item_density
        if nb_items != 0:
            nb_items = randrange(nb_items - 2, nb_items + 2)
        if nb_items > 0:
            shuffle_spawns(valid_spawns)
            start = randrange(len(valid_spawns))
            for i in range(nb_items):
                c = valid_spawns[start]
                start += 1
                if start == len(valid_spawns):
                    start = 0
                DungeonData.list_tiles[c[0]][c[1]][2] |= 0x2
    ### Spawn items/traps in a non-empty Monster House
    valid_spawns = []
    if not empty:
        for x in range(56):
            for y in range(32):
                # Monster House items/traps can spawn on tiles that are:
                # - not in a Kecleon shop
                # - in a Monster House
                # - not a junction (by a hallway)
                if (
                    DungeonData.list_tiles[x][y][0] & 0x20 == 0
                    and DungeonData.list_tiles[x][y][0] & 0x40
                    and DungeonData.list_tiles[x][y][0] & 0x8 == 0
                ):
                    valid_spawns.append((x, y))
    if len(valid_spawns) > 0:
        # Choose a subset of the available tiles to spawn stuff on
        nb_items = max(
            6,
            randrangeswap((5 * len(valid_spawns)) // 10, (8 * len(valid_spawns)) // 10),
        )
        if nb_items >= StaticParam.MH_NORMAL_SPAWN_ITEM:
            # Cap the number of non-monster spawns
            nb_items = StaticParam.MH_NORMAL_SPAWN_ITEM
        # Shuffle and start from a random point in the array
        shuffle_spawns(valid_spawns)
        start = randrange(len(valid_spawns))
        for i in range(nb_items):
            c = valid_spawns[start]
            start += 1
            if start == len(valid_spawns):
                # Wrap around to the front
                start = 0
            # 50/50 chance of spawning an item or a trap
            if randrange(2) == 1:
                # Item spawn
                DungeonData.list_tiles[c[0]][c[1]][2] |= 0x2
            # Monster House traps can only spawn in non-story mode and
            # starting in Dark Hill?
            elif (
                DungeonData.free_mode
                or DungeonData.dungeon_number >= StaticParam.MH_MIN_TRAP_DUNGEON
            ):
                # Trap spawn
                DungeonData.list_tiles[c[0]][c[1]][2] |= 0x4
    # RandomGenerator.print()
    ### Spawn normal traps
    valid_spawns = []
    for x in range(56):
        for y in range(32):
            # Normal traps can spawn on tiles that are:
            # - open terrain
            # - in a room
            # - not in a Kecleon shop
            # - don't already have an item or enemy spawn
            # - aren't a special tile that can't be destroyed by Absolute
            #   Mover
            if (
                DungeonData.list_tiles[x][y][0] & 0x3 == 1
                and DungeonData.list_tiles[x][y][7] != 0xFF
                and DungeonData.list_tiles[x][y][0] & 0x20 == 0
                and DungeonData.list_tiles[x][y][2] & 0x2 == 0
                and DungeonData.list_tiles[x][y][0] & 0x8 == 0
                and DungeonData.list_tiles[x][y][0] & 0x100 == 0
            ):
                valid_spawns.append((x, y))
    if len(valid_spawns) > 0:
        # Add some variation in trap count
        nb_traps = randrangeswap(prop.trap_density // 2, prop.trap_density)
        if nb_traps > 0:
            if nb_traps >= 56:
                # Cap the number of traps at 56
                nb_traps = 56
            # Shuffle array and start at a random index
            shuffle_spawns(valid_spawns)
            start = randrange(len(valid_spawns))
            for i in range(nb_traps):
                c = valid_spawns[start]
                start += 1
                if start == len(valid_spawns):
                    start = 0
                # Spawn a trap at this location
                DungeonData.list_tiles[c[0]][c[1]][2] |= 0x4
    if get_floor_type() == 2:
        # This is a rescue floor
        flag = True
    else:
        flag = False
    ### Spawn the player
    valid_spawns = []
    if DungeonData.player_spawn_x == -1 or DungeonData.player_spawn_y == -1:
        for x in range(56):
            for y in range(32):
                # The player can spawn on tiles that are:
                # - open terrain
                # - in a room
                # - not in a Kecleon shop
                # - not a junction (not by a hallway)
                # - not a special tile that can't be broken by Absolute Mover
                # - don't already have item, enemy, or trap spawns
                if (
                    DungeonData.list_tiles[x][y][0] & 0x3 == 1
                    and DungeonData.list_tiles[x][y][7] != 0xFF
                    and DungeonData.list_tiles[x][y][0] & 0x20 == 0
                    and DungeonData.list_tiles[x][y][0] & 0x8 == 0
                    and DungeonData.list_tiles[x][y][0] & 0x100 == 0
                    and DungeonData.list_tiles[x][y][2] & 0x2 == 0
                    and DungeonData.list_tiles[x][y][2] & 0x8 == 0
                    and DungeonData.list_tiles[x][y][2] & 0x4 == 0
                ):
                    # Furthermore, on rescue floors, the player also can't
                    # spawn on the stairs
                    if not flag or DungeonData.list_tiles[x][y][2] & 0x1 == 0:
                        valid_spawns.append((x, y))
        if len(valid_spawns) > 0:
            # Randomly spawn the player on one of the valid tiles
            spawn = valid_spawns[randrange(len(valid_spawns))]
            DungeonData.player_spawn_x = spawn[0]
            DungeonData.player_spawn_y = spawn[1]


# US: 02341470
# Spawn enemy monsters
def generate_monster_spawns(prop, empty):
    valid_spawns = []
    if prop.enemy_density < 1:
        # Nonpositive means exact value
        enemies = abs(prop.enemy_density)
    else:
        # Positive means a random value
        enemies = randrange(prop.enemy_density // 2, prop.enemy_density)
        if enemies < 1:
            enemies = 1
    for x in range(56):
        for y in range(32):
            # Enemies can only spawn on tiles that are:
            # - open terrain
            # - in a room
            # - not in a Kecleon shop
            # - don't also have a stairs, item, or other enemy spawn
            # - not a special tile that can't be broken by Absolute Mover
            # - not where the player spawns
            if (
                DungeonData.list_tiles[x][y][0] & 0x3 == 1
                and DungeonData.list_tiles[x][y][7] != 0xFF
                and DungeonData.list_tiles[x][y][0] & 0x20 == 0
                and DungeonData.list_tiles[x][y][2] & 0x2 == 0
                and DungeonData.list_tiles[x][y][2] & 0x1 == 0
                and DungeonData.list_tiles[x][y][0] & 0x8 == 0
                and DungeonData.list_tiles[x][y][0] & 0x100 == 0
            ):
                if DungeonData.player_spawn_x != x or DungeonData.player_spawn_y != y:
                    if (
                        StatusData.no_enemy_spawn == 0
                        or DungeonData.mh_room != DungeonData.list_tiles[x][y][7]
                    ):
                        valid_spawns.append((x, y))
    if len(valid_spawns) > 0 and enemies + 1 > 0:
        # From the valid spawn locations, pick a subset of them randomly
        shuffle_spawns(valid_spawns)
        enemies += 1
        # Also start at a random point in the shuffled array...
        # for extra randomness I guess??
        start = randrange(len(valid_spawns))
        for i in range(enemies):
            c = valid_spawns[start]
            start += 1
            if start == len(valid_spawns):
                # Wrap around to the front
                start = 0
            # Spawn an enemy at this location
            DungeonData.list_tiles[c[0]][c[1]][2] |= 0x8
    if DungeonData.create_mh:
        # The floor was marked as having a Monster House,
        # mark extra enemy spawns in the Monster House room
        valid_spawns = []
        mh_spawn = StaticParam.MH_NORMAL_SPAWN_ENM
        if empty:
            # "Empty" Monster House; only spawn 3 enemies
            mh_spawn = 3
        if DungeonData.create_mh:
            mh_spawn = (mh_spawn * 3) // 2
        # Similar procedure to the normal enemy spawns
        for x in range(56):
            for y in range(32):
                # Monster House enemies can only spawn on tiles that are:
                # - open terrain
                # - in a room
                # - not in a Kecleon shop
                # - not a special tile that can't be broken by Absolute Mover
                # - in a Monster House
                # - not where the player spawns
                if (
                    DungeonData.list_tiles[x][y][0] & 0x3 == 1
                    and DungeonData.list_tiles[x][y][7] != 0xFF
                    and DungeonData.list_tiles[x][y][0] & 0x20 == 0
                    and DungeonData.list_tiles[x][y][0] & 0x100 == 0
                    and DungeonData.list_tiles[x][y][0] & 0x40
                ):
                    if (
                        DungeonData.player_spawn_x != x
                        or DungeonData.player_spawn_y != y
                    ):
                        valid_spawns.append((x, y))
        if len(valid_spawns) > 0:
            # Select a random subset of the valid spawn points for enemies to
            # spawn on
            enemies = max(
                1,
                randrange((7 * len(valid_spawns)) // 10, (8 * len(valid_spawns)) // 10),
            )
            if enemies >= mh_spawn:
                # Don't spawn more enemies than the designated limit
                enemies = mh_spawn
            # Shuffle and start from a random index
            shuffle_spawns(valid_spawns)
            start = randrange(len(valid_spawns))
            for i in range(enemies):
                c = valid_spawns[start]
                start += 1
                if start == len(valid_spawns):
                    start = 0
                # Spawn an enemy at this location
                DungeonData.list_tiles[c[0]][c[1]][2] |= 0x8


# US: 02340974
# Resolve invalid spawn flags and spawn flag conflicts
def clear_safe():
    for x in range(56):
        for y in range(32):
            if DungeonData.list_tiles[x][y][0] & 0x3 != 1:
                if DungeonData.list_tiles[x][y][0] & 0x110:
                    # This tile is an impassable obstacle; ensure no items
                    # spawn here
                    DungeonData.list_tiles[x][y][2] &= ~0x2
                # This tile is an obstacle; ensure no traps spawn here
                DungeonData.list_tiles[x][y][2] &= ~0x4
            if DungeonData.list_tiles[x][y][2] & 0x1:
                # This tile has stairs on it; ensure the stairs bit is set
                # and make sure no traps spawn here
                DungeonData.list_tiles[x][y][0] |= 0x200
                DungeonData.list_tiles[x][y][2] &= ~0x4
            if DungeonData.list_tiles[x][y][2] & 0x2:
                # This tile has an item spawn; ensure no traps spawn here
                DungeonData.list_tiles[x][y][2] &= ~0x4


# US: 02341E6C
# Check that the stairs are reachable from all walkable tiles on the floor
def test_reachable(xpos, ypos, mark_invalid):
    # Bitflags:
    # 0 (0x1): tile is an obstacle and can't be corner-cut
    # 1 (0x2): tile is secondary terrain and can't be corner-cut
    # 4 (0x10): starting point
    # 6 (0x40): in the to-visit queue
    # 7 (0x80): visited
    tst = [[0 for y in range(32)] for x in range(56)]
    for x in range(56):
        for y in range(32):
            if mark_invalid:
                # Reset all the "unreachable" flags on the tiles, since we'll
                # recompute them from scratch shortly
                DungeonData.list_tiles[x][y][0] &= ~0x8000
            if DungeonData.list_tiles[x][y][0] & 0x3 != 1:
                if DungeonData.list_tiles[x][y][0] & 0x4 == 0:
                    tst[x][y] |= 0x1
            if DungeonData.list_tiles[x][y][0] & 0x3 == 2:
                if DungeonData.list_tiles[x][y][0] & 0x4 == 0:
                    tst[x][y] |= 0x2
    tst[xpos][ypos] |= 0x50
    if DungeonData.stairs_spawn_x != xpos and DungeonData.stairs_spawn_y != ypos:
        return False
    StatusData.unk_val_24 = 0
    count = 0
    checked = 1
    # This runs BFS starting from the stairs until all reachable tiles have
    # been visited, marked with 0x80 (well, sort of BFS; the visiting order
    # isn't strictly BFS, but it's the same idea).
    while checked:
        count += 1
        checked = 0
        for x in range(56):
            for y in range(32):
                if tst[x][y] & 0x80 == 0 and tst[x][y] & 0x40:
                    tst[x][y] &= ~0x40  # Pop from queue
                    tst[x][y] |= 0x80  # Mark as visited
                    checked += 1
                    if x > 0 and tst[x - 1][y] & 0x83 == 0:
                        # This might put already-visited tiles back on the
                        # queue, but it doesn't matter because they have the
                        # "visited" flag set so they won't be reprocessed
                        tst[x - 1][y] |= 0x40
                    if y > 0 and tst[x][y - 1] & 0x83 == 0:
                        tst[x][y - 1] |= 0x40
                    if x < 55 and tst[x + 1][y] & 0x83 == 0:
                        tst[x + 1][y] |= 0x40
                    if y < 31 and tst[x][y + 1] & 0x83 == 0:
                        tst[x][y + 1] |= 0x40
                    if (
                        x > 0
                        and y > 0
                        and tst[x - 1][y - 1] & 0x87 == 0
                        and tst[x][y - 1] & 0x1 == 0
                        and tst[x - 1][y] & 0x1 == 0
                    ):
                        tst[x - 1][y - 1] |= 0x40
                    if (
                        x < 55
                        and y > 0
                        and tst[x + 1][y - 1] & 0x87 == 0
                        and tst[x][y - 1] & 0x1 == 0
                        and tst[x + 1][y] & 0x1 == 0
                    ):
                        tst[x + 1][y - 1] |= 0x40
                    if (
                        x > 0
                        and y < 31
                        and tst[x - 1][y + 1] & 0x87 == 0
                        and tst[x][y + 1] & 0x1 == 0
                        and tst[x - 1][y] & 0x1 == 0
                    ):
                        tst[x - 1][y + 1] |= 0x40
                    if (
                        x < 55
                        and y < 31
                        and tst[x + 1][y + 1] & 0x87 == 0
                        and tst[x][y + 1] & 0x1 == 0
                        and tst[x + 1][y] & 0x1 == 0
                    ):
                        tst[x + 1][y + 1] |= 0x40
    StatusData.unk_val_24 = count  # Number of tiles that can reach the stairs
    for x in range(56):
        for y in range(32):
            if tst[x][y] & 0x87 == 0:
                # This is an open tile that wasn't visited by BFS, which means
                # It's unreachable starting from the stairs
                if mark_invalid:
                    # Bit 15: walkable but unreachable from the stairs
                    DungeonData.list_tiles[x][y][0] |= 0x8000
                else:
                    if DungeonData.list_tiles[x][y][0] & 0x100 == 0:
                        return False
                    # 0x100 means the tile cannot be broken by Absolute
                    # Mover... I guess this means it's not really open
                    # terrain, so ignore the fact that we can't reach it?
    return True


# US: 02340B0C
def reinit_tiles():
    DungeonData.clear_tiles()
    # Set the border to impassable walls
    for x in range(56):
        for y in range(32):
            if (
                is_out_of_bounds(x - 1, y)
                or is_out_of_bounds(x, y - 1)
                or is_out_of_bounds(x + 1, y)
                or is_out_of_bounds(x, y + 1)
                or is_out_of_bounds(x - 1, y - 1)
                or is_out_of_bounds(x - 1, y + 1)
                or is_out_of_bounds(x + 1, y - 1)
                or is_out_of_bounds(x + 1, y + 1)
            ):
                DungeonData.list_tiles[x][y][0] |= 0x10
    # Clear spawns
    DungeonData.stairs_spawn_x = -1
    DungeonData.stairs_spawn_y = -1
    DungeonData.clear_fixed_room()
    DungeonData.nb_active_items = 0
    DungeonData.clear_active_traps()


# US: 0233C32C
def process_fixed_room(fixed_floor_number, prop):
    return True  # TODO


# US: 0233A6D8
def generate_floor():
    StatusData.floor_size = 0
    prop = Properties
    DungeonData.fixed_floor_number = Properties.fixed_floor_number
    StatusData.mh_chance = Properties.mh_chance
    StatusData.kecleon_chance = Properties.kecleon_chance
    StatusData.middle_room_secondary = Properties.middle_room_secondary
    StatusData.hidden_stairs_type = Properties.hidden_stairs_type + 1
    gen_attempts2 = 0
    while gen_attempts2 < 10:
        DungeonData.player_spawn_x = -1
        DungeonData.player_spawn_y = -1
        DungeonData.stairs_spawn_x = -1
        DungeonData.stairs_spawn_y = -1
        DungeonData.hidden_stairs_spawn_x = -1
        DungeonData.hidden_stairs_spawn_y = -1

        gen_attempts = 0

        fixed_room = 0
        # Try to spawn the actual floor layout, up to 10 times per entity
        # spawn attempt
        while gen_attempts < 10:
            # RandomGenerator.print()
            ReturnData.invalid_generation = False
            if fixed_room != 0:
                if 0 < DungeonData.fixed_floor_number < 0xA5:
                    # This is a full-floor fixed room; we are done
                    break
                fixed_room = 0
            DungeonData.attempts = gen_attempts

            if gen_attempts >= 1:
                # If layout generation has failed once, turn off secondary
                # structure generation on subsequent attempts
                StatusData.middle_room_secondary = 0

            StatusData.is_not_valid = 0
            StatusData.kecleon_shop_middle_x = -1
            StatusData.kecleon_shop_middle_y = -1

            reinit_tiles()

            DungeonData.player_spawn_x = -1
            DungeonData.player_spawn_y = -1

            if DungeonData.fixed_floor_number != 0:
                # Special handling for fixed rooms
                if not process_fixed_room(DungeonData.fixed_floor_number, prop):
                    fixed_room = 1
                    # There should be a goto here that skips layout generation
                break

            max_nb_room_x = 2  # [r13,#+0x8]
            max_nb_room_y = 2  # [r13,#+0x4]
            # Try to generate random grid dimensions
            attempts = 0x20
            while attempts > 0:
                if prop.layout == 8:
                    max_x = 5
                    max_y = 4
                else:
                    max_x = 9
                    max_y = 8
                max_nb_room_x = randrange(2, max_x)
                max_nb_room_y = randrange(2, max_y)

                # Jointly limit the overall dimensions
                if max_nb_room_x <= 6 and max_nb_room_y <= 4:
                    break
                attempts -= 1

            if attempts == 0:
                # Failed to generate random grid dimensions, default to 4x4
                max_nb_room_x = max_nb_room_y = 4

            # Make sure there are at least 7 tiles per grid cell in both
            # dimensions. Otherwise, the grid size is too big so default to 1
            if 0x38 // max_nb_room_x <= 7:
                max_nb_room_x = 1
            if 0x20 // max_nb_room_y <= 7:
                max_nb_room_y = 1
            secondary_gen = 0
            # Try to generate the configured floor layout
            if prop.layout == 1:
                max_nb_room_x = 4
                max_nb_room_y = randrange(2) + 2
                StatusData.floor_size = 1
                generate_normal_floor(max_nb_room_x, max_nb_room_y, prop)
                secondary_gen = 1
            elif prop.layout == 2:
                generate_one_mh_room()
                DungeonData.create_mh = 1
            elif prop.layout == 3:
                generate_ring(prop)
                secondary_gen = 1
            elif prop.layout == 4:
                generate_crossroads(prop)
                secondary_gen = 1
            elif prop.layout == 5:
                generate_2_rooms_mh()
                DungeonData.create_mh = 1
            elif prop.layout == 6:
                generate_room_line(prop)
                secondary_gen = 1
            elif prop.layout == 7:
                generate_cross(prop)
            elif prop.layout == 9:
                generate_beetle(prop)
            elif prop.layout == 10:
                generate_outer_room_floor(max_nb_room_x, max_nb_room_y, prop)
                secondary_gen = 1
            elif prop.layout == 11:
                max_nb_room_x = 4
                max_nb_room_y = randrange(2) + 2
                StatusData.floor_size = 2
                generate_normal_floor(max_nb_room_x, max_nb_room_y, prop)
                secondary_gen = 1
            ##        elif prop.layout==12:
            ##            generate_maze()
            ##            secondary_gen = 1
            else:
                generate_normal_floor(max_nb_room_x, max_nb_room_y, prop)
                secondary_gen = 1
            reset_y_borders()
            delete_status_10()
            if not StatusData.is_not_valid:
                # Nothing failed. Make sure there's enough rooms

                # Map from room index to whether or not that room exists
                room = [False for i in range(0x40)]
                # Number of tiles in some room
                room_tiles = 0
                for x in range(56):
                    for y in range(32):
                        if DungeonData.list_tiles[x][y][0] & 0x3 == 1:
                            if DungeonData.list_tiles[x][y][7] < 0xF0:
                                room_tiles += 1
                                if DungeonData.list_tiles[x][y][7] < 0x40:
                                    room[DungeonData.list_tiles[x][y][7]] = True
                nb_rooms = room.count(True)
                # Make sure there are at least 2 rooms, with at least 20 total
                # tiles among all the rooms
                if nb_rooms >= 2 and room_tiles >= 20:
                    # This is a good layout!
                    break
            # Bad layout; try again next iteration
            gen_attempts += 1
            if StaticParam.SHOW_ERROR:
                ReturnData.invalid_generation = True
                break
        if gen_attempts == 10:
            # Failed to generate a layout in 10 attempts; abort and generate
            # a one-room Monster House floor layout
            ReturnData.invalid_generation = True
            StatusData.kecleon_shop_middle_x = -1
            StatusData.kecleon_shop_middle_y = -1
            generate_one_mh_room()
            DungeonData.create_mh = 1

        # Now that we have a good layout, do some finalization
        generate_junctions()
        if secondary_gen:
            # RandomGenerator.print()
            generate_secondary(1, prop)

        # Spawn entities (stairs, items, traps, player, enemy monsters)
        if randrange(100) < prop.empty_mh_chance:
            empty = True
        else:
            empty = False

        # RandomGenerator.print()
        generate_item_spawns(prop, empty)
        # RandomGenerator.print()
        generate_monster_spawns(prop, empty)
        # RandomGenerator.print()
        clear_safe()

        if DungeonData.player_spawn_x != -1 and DungeonData.player_spawn_y != -1:
            if get_floor_type() == 1:
                # Floor type 1 is one of the normal fixed rooms; no need to
                # check that the stairs are reachable in this case since the
                # layout is fixed
                break
            else:
                # Make sure the stairs are reachable from all open tiles
                if (
                    DungeonData.stairs_spawn_x != -1
                    and DungeonData.stairs_spawn_y != -1
                ):
                    if test_reachable(
                        DungeonData.stairs_spawn_x, DungeonData.stairs_spawn_y, False
                    ):
                        # Spawns are good! We're done!
                        break
        # There's some issue with the spawns. Raze the whole layout and try
        # and try again next iteration
        gen_attempts2 += 1
        if StaticParam.SHOW_ERROR:
            ReturnData.invalid_generation = True
            break
    if gen_attempts2 == 10:
        # Failed to generate spawns in the floor layout in 10 attempts; abort
        # and generate a one-room Monster House

        # Layout generation
        ReturnData.invalid_generation = True
        StatusData.kecleon_shop_middle_x = -1
        StatusData.kecleon_shop_middle_y = -1
        reinit_tiles()
        generate_one_mh_room()
        DungeonData.create_mh = 1

        # Layout finalization and spawns
        generate_junctions()
        generate_item_spawns(prop, 0)
        generate_monster_spawns(prop, 0)
        clear_safe()
    # Don't mind the rest of floor generation
