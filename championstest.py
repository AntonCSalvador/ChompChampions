import pygame


class Player:
    def __init__(self, x, y, direction):
        self.start_position = (x, y)
        self.current_position = self.start_position
        self.direction = direction

    def move(self, dx, dy):
        self.current_position = (self.current_position[0] + dx, self.current_position[1] + dy)

    def draw(self):  # needs to be updated or deleted in the future
        pass

    def update(self):  # needs to be updated or deleted in the future
        pass
        # this.position.y += this.velocity


# def animate():
#     requestAnimationFrame(animate)

class Projectile:
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


class HealthBar:
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


class ProfPicture:
    def __init__(self, x, y, w, h, img_path):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.image = pygame.image.load(img_path)  # Load the image
        self.image = pygame.transform.scale(self.image, (w, h))  # Scale the image to match the rectangle dimensions

    def draw(self, surface):
        pygame.draw.rect(surface, (255, 255, 255), (self.x, self.y, self.w, self.h))  # Draw the rectangle
        surface.blit(self.image, (self.x, self.y))  # Draw the image inside the rectangle


# Pygame initialization
pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

champ1Img = "static/champions/testImg/transparentDex.png"
champ2Img = "static/champions/testImg/dexHead.png"

# Create player objects and a Floor object
player1 = Player(100, 400, 'right')
player2 = Player(400, 400, 'left')
floor = Floor(0, 550, 800, 50)  # Creating a floor rectangle
health_bar1 = HealthBar(50, 10, 300, 40, 100)
health_bar2 = HealthBar(450, 10, 300, 40, 100)
profilePicP1 = ProfPicture(5, 10, 40, 40, champ1Img)
profilePicP2 = ProfPicture(755, 10, 40, 40, champ2Img)
player1_rect = pygame.Rect(player1.current_position[0] - 20, player1.current_position[1], 40, 40)
player2_rect = pygame.Rect(player2.current_position[0] - 20, player2.current_position[1], 40, 40)
pygame.draw.rect(screen, (255, 0, 0), player1_rect)
pygame.draw.rect(screen, (0, 0, 255), player2_rect)


projectiles1 = []  # List to store active projectiles for player 1
projectiles2 = []

melee_attacking1 = False
melee_attacking2 = False
melee_damage = 2

# all physics variables

# physics variables for player1
terminal_velocity1 = 15
gravity1 = 2
init_vel1 = 0
time1 = 0
velocity1 = 0

# physics variables for player2
terminal_velocity2 = 15
gravity2 = 2
init_vel2 = 0
time2 = 0
velocity2 = 0

# skill cool_downs
t_cooldown = 0
l_cooldown = 0
punch_reach1 = 0
punch_reach2 = 0
punch_dir1 = 'right'
punch_dir2 = 'left'

# Load the background GIF image
background_image = pygame.image.load("static/champions/testImg/testBackground.gif")
background_image = pygame.transform.scale(background_image, (800, 600))  # Scale the image to match the screen dims


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill((0, 0, 0))

    # Draw the background frame
    screen.blit(background_image, (0, 0))

    # Health bars
    health_bar1.draw(screen)
    health_bar2.draw(screen)

    # pfp
    profilePicP1.draw(screen)
    profilePicP2.draw(screen)

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

    """
    Player 1 attributes, abilities, movement, etc.
    """

    # Player 1 movement
    if keys[pygame.K_w] and player1.current_position[1] + 40 >= floor.rect.y:
        init_vel1 = 0.5  # changes how high the player jumps
        time1 = 0
    if keys[pygame.K_d]:  # Move player1 to the right
        player1.move(2, 0)  # Positive dx value moves character to the right
        player1.direction = 'right'
    if keys[pygame.K_a]:  # Move player1 to the left
        player1.move(-2, 0)  # Negative dx value moves character to the left
        player1.direction = 'left'

    # Projectile throw for player1
    if keys[pygame.K_r]:
        if player1.direction == 'left':
            proj_vel1 = -2
        else:
            proj_vel1 = 2
        throw1 = Projectile(player1.current_position[0], player1.current_position[1], proj_vel1)
        projectiles1.append(throw1)  # Add the new projectile to the list
        print("projectile thrown")

    # Remove collided projectiles for player1
    projectiles1_to_remove = []  # List to store projectiles that should be removed
    for projectile1 in projectiles1:
        projectile1.move(projectile1.velocity, 0)  # Move projectile horizontally
        pygame.draw.circle(screen, (255, 255, 0), projectile1.current_position, 10)  # Draw the projectile

        # Check for collision with player2 using bounding boxes
        if (projectile1.rect.colliderect(player2_rect) and
                player2_rect.collidepoint(
                    projectile1.current_position)):  # Check both rect collision and point collision
            projectiles1_to_remove.append(projectile1)
            print(health_bar2.hp)
            health_bar2.hp = health_bar2.hp - 1
            print(health_bar2.hp)
            if projectile1.velocity > 0:
                player2.move(0.5, 0)  # Positive dx value moves character to the right
            else:
                player2.move(-0.5, 0)

    for projectile1 in projectiles1_to_remove:
        projectiles1.remove(projectile1)

    # Melee attack for player 1
    if keys[pygame.K_t] and t_cooldown == 0:
        punch_dir1 = player1.direction
        melee_attacking1 = True
        punch_reach1 = 0
        t_cooldown = 120

    if melee_attacking1:
        # Draw a melee attack rectangle relative to player1's position
        melee_attack_rect1 = pygame.Rect(player1.current_position[0] + punch_reach1, player1.current_position[1],
                                         20, 20)
        pygame.draw.rect(screen, (255, 0, 0), melee_attack_rect1)
        if punch_dir1 == 'right':
            punch_reach1 = 0 - (t_cooldown * 2 - 240)
        else:
            punch_reach1 = -20 + (t_cooldown * 2 - 240)

        # Check for collision with player2
        if melee_attack_rect1.colliderect(player2_rect):
            projectiles1_to_remove.append(Projectile)
            print(health_bar2.hp)
            health_bar2.hp -= melee_damage
            print(health_bar2.hp)
            melee_attacking1 = False
            init_vel2 = 1.5 
            if init_vel2 > 0:
                if punch_dir1 == 'right':
                    player2.move(10, 0)
                else:
                    player2.move(-10, 0)
                # might need to add acceleration to make more smooth

        if t_cooldown < 110:
            melee_attacking1 = False  # Reset melee_attacking flag
            punch_reach1 = 0

    if t_cooldown > 0:
        t_cooldown -= 1

    """
    Player 2 attributes, movement, and attacks
    """

    # Player 2 movement
    if keys[pygame.K_UP] and player2.current_position[1] + 40 >= floor.rect.y:
        init_vel2 = 0.5  # changes how high the player jumps
        time2 = 0
    if keys[pygame.K_RIGHT]:  # Move player2 to the right
        player2.move(2, 0)  # Positive dx value moves character to the right
        player2.direction = 'right'
    if keys[pygame.K_LEFT]:  # Move player2 to the left
        player2.move(-2, 0)  # Negative dx value moves character to the left
        player2.direction = 'left'

    # Projectile throw for player2
    if keys[pygame.K_k]:
        if player2.direction == 'left':
            proj_vel2 = -2
        else:
            proj_vel2 = 2
        throw2 = Projectile(player2.current_position[0], player2.current_position[1], proj_vel2)
        projectiles2.append(throw2)  # Add the new projectile to the list
        print("projectile thrown")

    # Remove collided projectiles for player 2
    projectiles2_to_remove = []  # List to store projectiles that should be removed
    for projectile2 in projectiles2:
        projectile2.move(projectile2.velocity, 0)  # Move projectile horizontally
        pygame.draw.circle(screen, (255, 255, 0), projectile2.current_position, 10)  # Draw the projectile

        # Check for collision with player2 using bounding boxes
        if (projectile2.rect.colliderect(player1_rect) and
                player1_rect.collidepoint(
                    projectile2.current_position)):  # Check both rect collision and point collision
            projectiles2_to_remove.append(projectile2)
            print(health_bar1.hp)
            health_bar1.hp = health_bar1.hp - 1
            print(health_bar1.hp)
            if projectile2.velocity > 0:
                player1.move(0.5, 0)  # Positive dx value moves character to the right
            else:
                player1.move(-0.5, 0)

    for projectile2 in projectiles2_to_remove:
        projectiles2.remove(projectile2)

    # Melee attack for player 2
    if keys[pygame.K_l] and l_cooldown == 0:
        punch_dir2 = player2.direction
        melee_attacking2 = True
        punch_reach2 = 0
        l_cooldown = 120

    if melee_attacking2:
        # Draw a melee attack rectangle relative to player2's position
        melee_attack_rect2 = pygame.Rect(player2.current_position[0] + punch_reach2, player2.current_position[1],
                                         20, 20)
        pygame.draw.rect(screen, (255, 0, 0), melee_attack_rect2)
        if punch_dir2 == 'right':
            punch_reach2 = 0 - (l_cooldown * 2 - 240)
        else:
            punch_reach2 = -20 + (l_cooldown * 2 - 240)

        # Check for collision with player2
        if melee_attack_rect2.colliderect(player1_rect):
            projectiles2_to_remove.append(Projectile)
            print(health_bar1.hp)
            health_bar1.hp -= melee_damage
            print(health_bar1.hp)
            melee_attacking2 = False
            init_vel1 = 1.5
            if init_vel1 > 0:
                if punch_dir2 == 'right':
                    player1.move(10, 0)
                else:
                    player1.move(-10, 0)
                # might need to add acceleration to make more smooth

        if l_cooldown < 110:
            melee_attacking2 = False  # Reset melee_attacking flag
            punch_reach2 = 0

    if l_cooldown > 0:
        l_cooldown -= 1

    # Draw floor
    floor.draw(screen)

    # Draw rectangles for characters
    player1_rect = pygame.Rect(player1.current_position[0] - 20, player1.current_position[1], 40, 40)
    player2_rect = pygame.Rect(player2.current_position[0] - 20, player2.current_position[1], 40, 40)
    pygame.draw.rect(screen, (255, 0, 0), player1_rect)
    pygame.draw.rect(screen, (0, 0, 255), player2_rect)

    pygame.display.flip()

    clock.tick(60)

pygame.quit()
