import math


# game settings
WINDOW_SIZE = WINDOW_WIDTH, WINDOW_HEIGHT = 1200, 800
HALF_WIDTH, HALF_HEIGHT = WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2
PENTA_HEIGHT = 5 * WINDOW_HEIGHT
DOUBLE_HEIGHT = 2 * WINDOW_HEIGHT
FPS = 60
TILE = 100
FPS_POS = (WINDOW_WIDTH - 65, 5)

# ray casting settings
FOV = math.pi / 3
HALF_FOV = FOV / 2
NUM_RAYS = 400
MAX_DEPTH = 800
DELTA_ANGLE = FOV / NUM_RAYS
DIST = NUM_RAYS / (2 * math.tan(HALF_FOV))
PROJ_COEFF = 3 * DIST * TILE
SCALE = WINDOW_WIDTH // NUM_RAYS

# sprite settings
DOUBLE_PI = 2 * math.pi
CENTER_RAY = NUM_RAYS // 2 - 1
FAKE_RAYS = 100
FAKE_RAYS_RANGE = NUM_RAYS - 1 + 2 * FAKE_RAYS

# texture settings (1200 x 1200)
TEXTURE_WIDTH = 1200
TEXTURE_HEIGHT = 1200
TEXTURE_SCALE = TEXTURE_WIDTH // TILE

# player settings
player_pos = (HALF_WIDTH // 4, HALF_HEIGHT - 50)
player_angle = 0
player_speed = 2

# colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
DARK_GRAY = (127, 127, 127)
PURPLE = (127, 0, 127)
SKY_BLUE = (0, 186, 255)
