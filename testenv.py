import pygame


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


# Pygame initialization
pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

champ1Img = "static/champions/testImg/transparentDex.png"
champ2Img = "static/champions/testImg/dexHead.png"

# Create player objects and a Floor object
player1 = Player(100, 400)
player2 = Player(400, 400)
floor = Floor(0, 550, 800, 50)  # Creating a floor rectangle
health_bar1 = HealthBar(50, 10, 300, 40, 100)
health_bar2 = HealthBar(450, 10, 300, 40, 100)
profilePicP1 = profPicture(5, 10, 40, 40, champ1Img)
profilePicP2 = profPicture(755, 10, 40, 40, champ2Img)

projectiles = []  # List to store active projectiles

melee_attacking = False
melee_damage = 2

# physics variables
# physics variables for player1
terminal_velocity1 = 15
gravity1 = 2
init_vel1 = 0
time1 = 0
velocity1 = 0
collision1_left = False
collision1_right = False

# physics variables for player2
terminal_velocity2 = 15
gravity2 = 2
init_vel2 = 0
time2 = 0
velocity2 = 0
collision2_left = False
collision2_right = False

# skill cooldowns
t_cooldown = 0
punch_reach = 0

# Load the background GIF image
background_image = pygame.image.load("static/champions/testImg/testBackground.gif")
background_image = pygame.transform.scale(background_image,
                                          (800, 600))  # Scale the image to match the screen dimensions

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

    # Player 1 movement
    if keys[pygame.K_w] and player1.current_position[1] + 40 >= floor.rect.y:
        init_vel1 = 0.5  # changes how high the player jumps
        time1 = 0
    else:
        pass

    if keys[pygame.K_d] and not collision1_right:  # Move player1 to the right
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
            health_bar2.hp = health_bar2.hp - 1
            print(health_bar2.hp)
            player2.move(0.5, 0)  # Positive dx value moves character to the right

    for projectile in projectiles_to_remove:
        projectiles.remove(projectile)

    # Melee attack
    if keys[pygame.K_t] and t_cooldown == 0:
        melee_attacking = True
        punch_reach = 0
        t_cooldown = 120

    if melee_attacking:
        # Draw a melee attack rectangle relative to player1's position
        melee_attack_rect = pygame.Rect(player1.current_position[0] + punch_reach, player1.current_position[1], 20, 20)
        pygame.draw.rect(screen, (255, 0, 0), melee_attack_rect)
        punch_reach = 0 - (t_cooldown * 2 - 240)

        # Check for collision with player2
        if melee_attack_rect.colliderect(player2_rect):
            projectiles_to_remove.append(Projectile)
            print(health_bar2.hp)
            health_bar2.hp -= melee_damage
            print(health_bar2.hp)
            melee_attacking = False
            init_vel2 = 1.5
            if (init_vel2 > 0):
                player2.move(10, 0)
                # might need to add acceleration to make more smooth

        if t_cooldown < 110:
            melee_attacking = False  # Reset melee_attacking flag
            punch_reach = 0

    if t_cooldown > 0:
        t_cooldown -= 1

    # Player 2 movement
    if keys[pygame.K_UP] and player2.current_position[1] + 40 >= floor.rect.y:
        init_vel2 = 0.5  # changes how high the player jumps
        time2 = 0
    else:
        pass
    if keys[pygame.K_RIGHT]:  # Move player2 to the right
        player2.move(2, 0)  # Positive dx value moves character to the right
    if keys[pygame.K_LEFT] and not collision2_left:  # Move player2 to the left
        player2.move(-2, 0)  # Negative dx value moves character to the left

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