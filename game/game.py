import pygame

pygame.init()
screen = pygame.display.set_mode((1280,720))
clock = pygame.time.Clock()
# player = load_player_image()
running = True

player_pos = pygame.Vector2(screen.get_width() / 2, screen.get_height() / 2)

dt = 0
while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
                running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("grey")

    # RENDER YOUR GAME HERE
    pygame.draw.circle(screen, "red", player_pos, 40)
    # pygame.draw.rect(screen, "red", (100, 320, 50, 200))
    # pygame.draw.line(screen, "white", player_pos, (40,0))

    key = pygame.key.get_pressed()
    print("player_pos.x: ", player_pos.x)
# 760 AND 680


    # if(player_pos.y <= 680):
    #     player_pos.y -= 300 * dt
    
    if(player_pos.y <= 680):
        if(key[pygame.K_s]):
            player_pos.y += 300 * dt
    if(player_pos.y >= 40):
        if(key[pygame.K_w]):
            player_pos.y -= 300 * dt
    if(player_pos.x >= 40):
        if(key[pygame.K_a]):
            player_pos.x -= 300 * dt
    if(player_pos.x <= 1240):
            if(key[pygame.K_d]):
                player_pos.x += 300 * dt

    # if(key[pygame.K_w]):
    #     player_pos.y -= 600 * dt
    # if(key[pygame.K_s]):
    #     player_pos.y += 300 * dt
    # if(key[pygame.K_a]):
    #     player_pos.x -= 300 * dt
    # if(key[pygame.K_d]):
    #     player_pos.x += 300 * dt


    # flip() the display to put your work on screen
    pygame.display.flip()
    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

    clock.tick(60)  # limits FPS to 60

pygame.quit()
