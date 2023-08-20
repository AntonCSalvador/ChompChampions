import pygame
import json

# Open and read the JSON file
with open('testFrames.json', 'r') as json_file:
    data = json.load(json_file)
testChamp = data[0]

pfp = testChamp['pfp']
rDamage = testChamp['Damage1']
tDamage = testChamp['Damage2']
health1 = testChamp['health']
animationDirectoryP1 = testChamp['animationDirectory']


class Player:
    def __init__(self, x, y):
        self.start_position = (x, y)
        self.current_position = self.start_position

    def move(self, dx, dy):
        self.current_position = (self.current_position[0] + dx, self.current_position[1] + dy)

    def draw(self):
        print("hi")

    def update(self):
        print("hi")
        # this.position.y += this.velocity


# def animate():
#     requestAnimationFrame(animate)

class Projectile:  # pee proj
    def __init__(self, x, y, velocity):
        self.start_position = (x, y)
        self.current_position = self.start_position
        self.velocity = velocity
        self.radius = 10  # Radius for the circle projectile
        self.rect = pygame.Rect(x - self.radius, y + 20 - self.radius, self.radius * 2, self.radius * 2)

    def move(self, dx, dy):
        self.current_position = (self.current_position[0] + dx, self.current_position[1] + dy)
        self.rect.move_ip(dx, dy)


class Floor:
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)

    def draw(self, surface):
        pygame.draw.rect(surface, (0, 255, 0), self.rect)  # Green color for the ground


class HealthBar():
    def __init__(self, x, y, w, h, max_hp):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.hp = max_hp  # Assume it starts at full health
        self.max_hp = max_hp

    def draw(self, surface):
        # Calculate health ratio
        ratio = self.hp / self.max_hp
        pygame.draw.rect(surface, "red", (self.x, self.y, self.w, self.h))
        pygame.draw.rect(surface, "green", (self.x, self.y, self.w * ratio, self.h))


class profPicture():
    def __init__(self, x, y, w, h, imgPath):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.image = pygame.image.load(imgPath)  # Load the image
        self.image = pygame.transform.scale(self.image, (w, h))  # Scale the image to match the rectangle dimensions

    def draw(self, surface):
        pygame.draw.rect(surface, (255, 255, 255), (self.x, self.y, self.w, self.h))  # Draw the rectangle
        surface.blit(self.image, (self.x, self.y))  # Draw the image inside the rectangle


class inGameTimer():
    def __init__(self, x, y, w, h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.remaining_time = 90  # Initialize the remaining time to 90 seconds

    def draw(self, surface):
        pygame.draw.rect(surface, (255, 255, 255), (self.x, self.y, self.w, self.h))  # Draw the rectangle

        # Calculate the text to display
        font = pygame.font.Font(None, 36)
        text = font.render(str(round(self.remaining_time)), True, (0, 0, 0))
        text_rect = text.get_rect(center=(self.x + self.w // 2, self.y + self.h // 2))
        surface.blit(text, text_rect)

        self.remaining_time -= 0.01  # Decrease the remaining time by 1 each frame

        if self.remaining_time <= 0:
            self.remaining_time = 0  # Reset the timer if it goes below 0
            return self.remaining_time

def animateFrames(framesArray, frameDesc):
    for y in range(0, frameDesc.get_height(), frame_height):
        for x in range(0, frameDesc.get_width(), frame_width):
            frame = frameDesc.subsurface(pygame.Rect(x, y, frame_width, frame_height))
            framesArray.append(frame)

def update_mask(image):
    mask = pygame.mask.from_surface(image)
    mask_image = mask.to_surface()
    transparent_color = (0, 0, 0, 0)  # Set the transparent color (RGBA: 0, 0, 0, 0)
    mask_image.set_colorkey(transparent_color)
    return mask, mask_image


# Pygame initialization
pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

champ1Img = "static/champions/testImg/transparentDex.png"
champ2Img = pfp

# Create player objects and a Floor object
player1 = Player(100, 400) #spawnpoint P1
player2 = Player(400, 400) #spawnpoint P2
floor = Floor(0, 550, 800, 50)  # Creating a floor rectangle
health_bar1 = HealthBar(50, 10, 300, 40, health1)
health_bar2 = HealthBar(450, 10, 300, 40, 100)
profilePicP1 = profPicture(5, 10, 40, 40, champ1Img)
profilePicP2 = profPicture(755, 10, 40, 40, champ2Img)
player1Idle = pygame.image.load("static/champions/"+ animationDirectoryP1 + "/Sprites/IdleTest.png")
player1Walk = pygame.image.load("static/champions/"+ animationDirectoryP1 +"/Sprites/RunTest.png")
player1Thrust = pygame.image.load("static/champions/"+ animationDirectoryP1 +"/Sprites/Attack1Floor.png")

# Get the dimensions of the sprite sheet images
idle_sheet_width = player1Idle.get_width()
idle_sheet_height = player1Idle.get_height()

walk_sheet_width = player1Walk.get_width()
walk_sheet_height = player1Walk.get_height()

thrust_sheet_height = player1Thrust.get_height()
thrust_sheet_width = player1Thrust.get_width()

# Print the dimensions
print("Player1 Idle Sprite Sheet Dimensions:", idle_sheet_width, "x", idle_sheet_height)
print("Player1 Walk Sprite Sheet Dimensions:", walk_sheet_width, "x", walk_sheet_height)
print("Player1 Walk Sprite Sheet Dimensions:", thrust_sheet_width, "x", thrust_sheet_height)


# Define the dimensions of each frame in the sprite sheet
frame_width = 200
frame_height = 200

# Create a list to store the individual frames
player1_frames = []

#turn into function
animateFrames(player1_frames, player1Idle)
animateFrames(player1_frames, player1Walk)
animateFrames(player1_frames, player1Thrust)

# for y in range(0, player1Idle.get_height(), frame_height):
#     for x in range(0, player1Idle.get_width(), frame_width):
#         frame = player1Idle.subsurface(pygame.Rect(x, y, frame_width, frame_height))
#         player1_frames.append(frame)
# for y in range(0, player1Thrust.get_height(), frame_height):
#     for x in range(0, player1Thrust.get_width(), frame_width):
#         frame = player1Thrust.subsurface(pygame.Rect(x, y, frame_width, frame_height))
#         player1_frames.append(frame)

# Define animation sequences as lists of frame indices
idle_animation = [0, 1, 2, 3]  # Example: idle animation frames
walk_animation = [4, 5, 6, 7, 8, 9, 10, 11]  # Example: walking animation frames
thrust_animation = [12, 13, 14, 15]
current_animation = idle_animation  # Start with idle animation
current_frame_index = 0

idle_mask = pygame.mask.from_surface(player1_frames[idle_animation[0]])
idle_mask_image = idle_mask.to_surface()  # delete this later bc this is just to see the actual mask, ideally the mask is invisible
previous_animation = None


timer = inGameTimer(365, 10, 70, 40)

projectiles = []  # List to store active projectiles

draw_custom_rectangle = False
melee_attacking = False
melee_damage = 2

# physics variables
# physics variables for player1
terminal_velocity1 = 15
gravity1 = 2
init_vel1 = 0
time1 = 0
velocity1 = 0
player1_refresh = 0
t_collide = False
t_up = False
slide_frames = 10

# physics variables for player2
terminal_velocity2 = 15
gravity2 = 2
init_vel2 = 0
time2 = 0
velocity2 = 0

# skill cooldowns
t_cooldown = 0
punch_reach = 0

# Load the background GIF image
# background_image = pygame.image.load("static/champions/testImg/testBackground.gif")
# background_image = pygame.transform.scale(background_image, (800, 600))
# Scale the image to match the screen dimensions

# Load the background image
background = pygame.image.load("static/champions/testImg/testBackground.gif")
background = pygame.transform.scale(background, (800, 600))  # Scale the image to match the screen dimensions
background_y = 0
background_x = 450

cloud = pygame.image.load("static/champions/testImg/cloud.png")
cloudHeight = cloud.get_height()
cloudWidth = cloud.get_width()
print("Height: ", cloudHeight, " Width: ", cloudWidth)
cloud = pygame.transform.scale(cloud, (300, 100))

# Set the title of the game window
pygame.display.set_caption("Chomp Champions")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # use this concept for clouds
    # Decrement background_y to move the background up
    background_y -= 0.05

    # Reset background_y if it reaches the negative height of the image
    if background_y <= -background.get_height():
        background_y = 0

    background_x -= 1
    if background_x <= - 800:
        background_x = 0

    player1_rect = pygame.Rect(player1.current_position[0] - 20, player1.current_position[1], 40, 40)
    pygame.draw.rect(screen, (255, 0, 0), player1_rect)

    # Clear the screen
    screen.fill((0, 0, 0))

    # Draw the background at the current position
    screen.blit(background, (0, background_y))

    screen.blit(cloud, (background_x, 60))

    # player1_rect = pygame.Rect(player1.current_position[0] - 20, player1.current_position[1], 40, 40)
    # pygame.draw.rect(screen, (255, 0, 0), player1_rect)

    # for basic animation
    # for basic animation
    current_frame = player1_frames[current_animation[current_frame_index]]
    player1_size = 400
    player1.current_frame = pygame.transform.scale(current_frame, (player1_size, player1_size))  # Adjust size as needed
    if player1_refresh == 0:
        current_frame_index = (current_frame_index + 1) % len(current_animation)
        player1_refresh = 5
    screen.blit(player1.current_frame, (player1.current_position[0] - (player1_size/2), player1.current_position[1] - (player1_size - 40)))
    player1_refresh -= 1

    # reset sword attack skill after hitting
    if current_animation == thrust_animation:
        if current_frame_index == 3:
            current_frame_index = 0
            current_animation = idle_animation

    #this updates the mask to the current frame being used by the player
    if current_animation != previous_animation:
        idle_mask, idle_mask_image = update_mask(player1_frames[current_animation[current_frame_index]])
        previous_animation = current_animation
    
    screen.blit(idle_mask_image, (player1.current_position[0] - 100, player1.current_position[1] - 160)) #this is just temporary to test looking at the mask

    # Health bars
    health_bar1.draw(screen)
    health_bar2.draw(screen)

    # pfp
    profilePicP1.draw(screen)
    profilePicP2.draw(screen)

    # timer
    timer.draw(screen)

    fpsFont = pygame.font.Font(None, 36)

    # Calculate FPS
    fps = int(clock.get_fps())

    # Render FPS text
    fps_text = fpsFont.render(f"FPS: {fps}", True, (255, 255, 255))  # White text color

    # Get the rect for the text
    fps_rect = fps_text.get_rect(topright=(800, 0))  # Adjust the position as needed

    # Draw FPS text
    screen.blit(fps_text, fps_rect)

    # Physics
    # Check for collisions and apply gravity
    # Physics for player1
    velocity1 = gravity1 * (time1 / 60) - init_vel1
    if abs(velocity1) > 10:
        velocity1 = 10 * (velocity1 / abs(velocity1))
    player1.current_position = (player1.current_position[0], player1.current_position[1] + velocity1 * 4)
    time1 += 1
    if player1.current_position[1] + 40 >= floor.rect.y:
        player1.current_position = (player1.current_position[0], floor.rect.y - 40)
        velocity1 = 0
        init_vel1 = 0
        time1 = 0

    # Physics for player2
    velocity2 = gravity2 * (time2 / 60) - init_vel2
    if abs(velocity2) > 10:
        velocity2 = 10 * (velocity2 / abs(velocity2))
    player2.current_position = (player2.current_position[0], player2.current_position[1] + velocity2 * 4)
    time2 += 1
    if player2.current_position[1] + 40 >= floor.rect.y:
        player2.current_position = (player2.current_position[0], floor.rect.y - 40)
        velocity2 = 0
        init_vel2 = 0
        time2 = 0

    # Move and draw player objects
    keys = pygame.key.get_pressed()

    # Player 1 movement
    if keys[pygame.K_w] and player1.current_position[1] + 40 >= floor.rect.y:
        init_vel1 = 0.5  # changes how high the player jumps
        time1 = 0
    else:
        pass

    if keys[pygame.K_d] or keys[pygame.K_a]:
        if current_animation == thrust_animation:
            pass
        else:
            current_animation = walk_animation
    else:
        if current_animation == thrust_animation:
            pass
        else:
            current_frame_index = 0
            current_animation = idle_animation

    if keys[pygame.K_d]:  # Move player1 to the right
        player1.move(2, 0)  # Positive dx value moves character to the right
    if keys[pygame.K_a]:  # Move player1 to the left
        player1.move(-2, 0)  # Negative dx value moves character to the left

    # Projectile throw for player1
    if keys[pygame.K_r]:
        throw = Projectile(player1.current_position[0], player1.current_position[1], 2)
        projectiles.append(throw)  # Add the new projectile to the list
        print("projectile thrown")

    # Remove collided projectiles
    projectiles_to_remove = []  # List to store projectiles that should be removed
    for projectile in projectiles:
        projectile.move(projectile.velocity, 0)  # Move projectile horizontally
        pygame.draw.circle(screen, (255, 255, 0), projectile.current_position, 10)  # Draw the projectile

        # Check for collision with player2 using bounding boxes
        if (projectile.rect.colliderect(player2_rect) and
                player2_rect.collidepoint(
                    projectile.current_position)):  # Check both rect collision and point collision
            projectiles_to_remove.append(projectile)
            print(health_bar2.hp)
            health_bar2.hp = health_bar2.hp - rDamage
            print(health_bar2.hp)
            player2.move(0.5, 0)  # Positive dx value moves character to the right

    for projectile in projectiles_to_remove:
        projectiles.remove(projectile)

    # Melee attack
    if keys[pygame.K_t] and t_cooldown == 0:
        melee_attacking = True
        punch_reach = 0
        t_cooldown = 120
        current_frame_index = 0  # Reset the frame index for the new animation
        current_animation = thrust_animation

    if melee_attacking:
        # Draw a melee attack rectangle relative to player1's position
        melee_attack_rect = pygame.Rect(player1.current_position[0] + 50, player1.current_position[1] - 40, 100, 50)
        #  pygame.draw.rect(screen, (255, 0, 0), melee_attack_rect)
        punch_reach = 0 - (t_cooldown / 1.2 - 240)

        # Check for collision with player2
        if melee_attack_rect.colliderect(player2_rect):
            projectiles_to_remove.append(Projectile)
            print(health_bar2.hp)
            health_bar2.hp -= tDamage
            print(health_bar2.hp)
            melee_attacking = False
            current_frame_index = 0
            t_collide = True
            t_up = True
            slide_frames = 10

        if t_cooldown < 110:
            melee_attacking = False  # Reset melee_attacking flag
            punch_reach = 0
            current_animation = idle_animation
            t_collide = False

    if t_collide:
        if t_up:
            init_vel2 = 1
            t_up = False
        if player2.current_position[1] <= floor.rect.y - 41:
            player2.move(2, 0)
            print('player moved 5')
        else:
            slide_frames -= 1
            if slide_frames > 6:
                player2.move(2, 0)
            elif slide_frames > 3:
                player2.move(1, 0)
            elif slide_frames > 0:
                player2.move(0.5, 0)
            else:
                t_collide = False



    if t_cooldown > 0:
        t_cooldown -= 1

    # history major spawn
    if keys[pygame.K_z]:
        draw_custom_rectangle = True
        custom_rect_x = player1_rect.right + 10

    if draw_custom_rectangle:
        custom_rect_x += 1  # Position it to the right of player1_rect
        custom_rect_y = player1_rect.top
        custom_rect = pygame.Rect(custom_rect_x, floor.rect.y - 40, 40, 40)  # Create the custom rectangle
        pygame.draw.rect(screen, (255, 0, 0), custom_rect)  # Draw the custom rectangle
        if custom_rect_x > 800:
            draw_custom_rectangle = False


    # Player 2 movement
    if keys[pygame.K_UP] and player2.current_position[1] + 40 >= floor.rect.y:
        init_vel2 = 0.5  # changes how high the player jumps
        time2 = 0
    else:
        pass
    if keys[pygame.K_RIGHT]:  # Move player2 to the right
        player2.move(2, 0)  # Positive dx value moves character to the right
    if keys[pygame.K_LEFT]:  # Move player2 to the left
        player2.move(-2, 0)  # Negative dx value moves character to the left

    # Draw floor
    floor.draw(screen)

    # Draw rectangles for characters
    player2_rect = pygame.Rect(player2.current_position[0] - 20, player2.current_position[1], 40, 40)
    pygame.draw.rect(screen, (0, 0, 255), player2_rect)

    pygame.display.flip()

    clock.tick(60)

pygame.quit()