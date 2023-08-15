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

# Pygame initialization
pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

# Create player objects and a Floor object
player1 = Player(100, 400)
player2 = Player(400, 400)
floor = Floor(0, 550, 800, 50)  # Creating a floor rectangle
health_bar1 = HealthBar(10, 10, 300, 40, 100)

projectiles = []  # List to store active projectiles

gravity = 0.25
player1_movement = 400
player1_velocity = 0  # New variable to track the vertical velocity of player1

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill((0, 0, 0))

    # Health bars
    health_bar1.draw(screen)

    # Physics
    # Check for collisions and apply gravity
    if player1.current_position[1] + 40 <= floor.rect.y:  # Adjusted for character's height
        player1.current_position = (player1.current_position[0], floor.rect.y - 40)  # Set character on top of the floor
        player1_velocity = 0  # Reset velocity when player1 is on the ground

    else:
        player1.move(0, 2)  # Apply gravity to player1
        player1_velocity += gravity  # Apply gravity to player1


    if player2.current_position[1] + 40 <= floor.rect.y:  # Adjusted for character's height
        player2.current_position = (player2.current_position[0], floor.rect.y - 40)  # Set character on top of the floor
    else:
        player2.move(0, 2)  # Apply gravity to player2




    # Move and draw player objects
    keys = pygame.key.get_pressed()

    # Player 1 movement
    if keys[pygame.K_w]:
        player1_velocity -= 1.5
    else:
        player1_velocity = 0

    player1_movement += player1_velocity  # Update vertical position based on velocity
    player1_movement += gravity
    player1_movement = max(player1_movement, 0)  # Ensure the player stays within screen bounds

    player1.move(0, player1_movement - player1.current_position[1])  # Update player1's vertical position

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
            player2_rect.collidepoint(projectile.current_position)):  # Check both rect collision and point collision
            projectiles_to_remove.append(projectile)
            print(health_bar1.hp)
            health_bar1.hp = health_bar1.hp - 1
            print(health_bar1.hp)


    for projectile in projectiles_to_remove:
        projectiles.remove(projectile)

    # Player 2 movement
    if keys[pygame.K_UP]:  # Move player2 up in the y-axis
        player2.move(0, -20)  # Negative dy value moves character upward
    if keys[pygame.K_RIGHT]:  # Move player2 to the right
        player2.move(2, 0)  # Positive dx value moves character to the right
    if keys[pygame.K_LEFT]:  # Move player2 to the left
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
