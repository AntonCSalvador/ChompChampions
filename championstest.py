import pygame

class Player:
    def __init__(self, x, y):
        self.start_position = (x, y)
        self.current_position = self.start_position

    def move(self, dx, dy):
        self.current_position = (self.current_position[0] + dx, self.current_position[1] + dy)

    def draw():
        print("hi")

    def update():
        print("hi")
        # this.position.y += this.velocity

# def animate():
#     requestAnimationFrame(animate)



class Floor:
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)

    def draw(self, surface):
        pygame.draw.rect(surface, (0, 255, 0), self.rect)  # Green color for the ground

# Pygame initialization
pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()

# Create player objects and a Floor object
player1 = Player(100, 400)
player2 = Player(400, 400)
floor = Floor(0, 550, 800, 50)  # Creating a floor rectangle

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Clear the screen
    screen.fill((0, 0, 0))

    #physics
    # Check for collisions and apply gravity
    if player1.current_position[1] + 40 <= floor.rect.y:  # Adjusted for character's height
        player1.current_position = (player1.current_position[0], floor.rect.y - 40)  # Set character on top of the floor
    else:
        player1.move(0, 2)  # Apply gravity to player1

    if player2.current_position[1] + 40 <= floor.rect.y:  # Adjusted for character's height
        player2.current_position = (player2.current_position[0], floor.rect.y - 40)  # Set character on top of the floor
    else:
        player2.move(0, 2)  # Apply gravity to player2

    # Move and draw player objects
    #if keypress  = w:
        #move player1 up in the y axis
    #if keypress = d:
        #move player1 to the right    
    keys = pygame.key.get_pressed()
    # Move player1 up in the y-axis
    if keys[pygame.K_w]:
        player1.move(0, -20)
    if keys[pygame.K_d]:  # Move player1 to the right
        player1.move(2, 0)  # Positive dx value moves character to the right
    # if keys[pygame.K_s]:  # Move player1 up in the y-axis
    #     player1.move(0, 2)  # Negative dy value moves character upward
    if keys[pygame.K_a]:  # Move player1 to the right
        player1.move(-2, 0)  # Positive dx value moves character to the right

    if keys[pygame.K_UP]:  # Move player1 up in the y-axis
        player2.move(0, -20)  # Negative dy value moves character upward
    if keys[pygame.K_RIGHT]:  # Move player1 to the right
        player2.move(2, 0)  # Positive dx value moves character to the right
    # if keys[pygame.K_DOWN]:  # Move player1 up in the y-axis
    #     player2.move(0, 2)  # Negative dy value moves character upward
    if keys[pygame.K_LEFT]:  # Move player1 to the right
        player2.move(-2, 0)  # Positive dx value moves character to the right


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


#physics temp
    # Move and draw player objects
    #if keypress = d:
        #move player1 to the right

    #create a floor
    #if position =< floor:
        #position = floor
            #or
        #gravity = 0

