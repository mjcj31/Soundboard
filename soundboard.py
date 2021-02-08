# from pydub import AudioSegment
# from pydub.playback import play
from playsound import playsound
import keyboard
import pygame #// UNCOMMENT THIS WHEN USING PYGAME 

# sound = pygame.mixer.Sound("dodgeSound.mp3") // example of how to use sound in pygame
# or
# sound = pygame.mixer.music.load("dodgeSound.mp3") // example of how to use sound in pygame

# sound.play() // can use this on the condition statements to play individual sounds

pygame.init() #// Initialize pygame
pygame.mixer.init() #// Initialize mixer (This will be used for sounds)

screen_width = 1400
screen_height = 300
surface = pygame.display.set_mode([screen_width, screen_height]) #// Initial screen display

WHITE = (255,255,255) #// This will represent the color white
GRAY = (135,135,135) #// This will represent the color gray
BLUE = (0,0,255)
RED = (255,0,0)
BLACK = (0,0,0)

surface.fill(BLACK)

#// Will add rectangles
block1 = pygame.draw.rect(surface,WHITE,(100,100,50,150))
block2 = pygame.draw.rect(surface,WHITE,(200,100,50,150))
block3 = pygame.draw.rect(surface,WHITE,(300,100,50,150))
block4 = pygame.draw.rect(surface,WHITE,(400,100,50,150))
block5 = pygame.draw.rect(surface,WHITE,(500,100,50,150))
block6 = pygame.draw.rect(surface,WHITE,(600,100,50,150))
block7 = pygame.draw.rect(surface,WHITE,(700,100,50,150))
block8 = pygame.draw.rect(surface,WHITE,(800,100,50,150))
block9 = pygame.draw.rect(surface,WHITE,(900,100,50,150))
block10 = pygame.draw.rect(surface,WHITE,(1000,100,50,150))
block11 = pygame.draw.rect(surface,WHITE,(1100,100,50,150))
block12 = pygame.draw.rect(surface,WHITE,(1200,100,50,150))

pygame.display.update()

#sounds = ["68437__pinkyfinger__piano-a.wav","68438__pinkyfinger__piano-b.wav","68439__pinkyfinger__piano-bb.wav","68440__pinkyfinger__piano-c.wav","68441__pinkyfinger__piano-c.wav","68442__pinkyfinger__piano-d.wav","68443__pinkyfinger__piano-e.wav","68444__pinkyfinger__piano-eb.wav","68445__pinkyfinger__piano-f.wav","68446__pinkyfinger__piano-f.wav","68447__pinkyfinger__piano-g.wav","68448__pinkyfinger__piano-g.wav"]

sound1 = pygame.mixer.Sound("Sounds/68437__pinkyfinger__piano-a.wav")
sound2 = pygame.mixer.Sound("Sounds/68438__pinkyfinger__piano-b.wav")
sound3 = pygame.mixer.Sound("Sounds/68439__pinkyfinger__piano-bb.wav")
sound4 = pygame.mixer.Sound("Sounds/68440__pinkyfinger__piano-c.wav")
sound5 = pygame.mixer.Sound("Sounds/68441__pinkyfinger__piano-c.wav")
sound6 = pygame.mixer.Sound("Sounds/68442__pinkyfinger__piano-d.wav")
sound7 = pygame.mixer.Sound("Sounds/68443__pinkyfinger__piano-e.wav") 
sound8 = pygame.mixer.Sound("Sounds/68444__pinkyfinger__piano-eb.wav")
sound9 = pygame.mixer.Sound("Sounds/68445__pinkyfinger__piano-f.wav")
sound10 = pygame.mixer.Sound("Sounds/68446__pinkyfinger__piano-f.wav")
sound11 = pygame.mixer.Sound("Sounds/68447__pinkyfinger__piano-g.wav")
sound12 = pygame.mixer.Sound("Sounds/68448__pinkyfinger__piano-g.wav")

flag = True

#key_input = input("> ")

while(flag):
    for event in pygame.event.get():
        if(event.type == pygame.KEYDOWN or event.type == pygame.MOUSEBUTTONUP):
            pos = pygame.mouse.get_pos()
            click1,click2,click3 = pygame.mouse.get_pressed()
            print(click1,click2,click3)
            if(event.key == pygame.K_q or (block1.collidepoint(pos) and click1)): # Second part of statement does not work. May need to add 'pygame.MOUSEBUTTONDOWN' to parent statement
                #playsound(sounds[0])
                block1 = pygame.draw.rect(surface,RED,(100,100,50,150))
                pygame.display.update()
                sound1.play()
                print("q pressed")
                continue
            elif(event.key == pygame.K_w):
                #playsound(sounds[1])
                block2 = pygame.draw.rect(surface,RED,(200,100,50,150))
                pygame.display.update()
                sound2.play()
                print("w pressed")
                continue
            elif(event.key == pygame.K_e):
                #playsound(sounds[2])
                block3 = pygame.draw.rect(surface,RED,(300,100,50,150))
                pygame.display.update()
                sound3.play()
                print("e pressed")
                continue
            elif(event.key == pygame.K_r):
                #playsound(sounds[3])
                block4 = pygame.draw.rect(surface,RED,(400,100,50,150))
                pygame.display.update()
                sound4.play()
                print("r pressed")
                continue
            elif(event.key == pygame.K_t):
                #playsound(sounds[4])
                block5 = pygame.draw.rect(surface,RED,(500,100,50,150))
                pygame.display.update()
                sound5.play()
                print("t pressed")
                continue
            elif(event.key == pygame.K_y):
                #playsound(sounds[5])
                block6 = pygame.draw.rect(surface,RED,(600,100,50,150))
                pygame.display.update()
                sound6.play()
                print("y pressed")
                continue
            elif(event.key == pygame.K_u):
                #playsound(sounds[6])
                block7 = pygame.draw.rect(surface,RED,(700,100,50,150))
                pygame.display.update()
                sound7.play()
                print("u pressed")
                continue
            elif(event.key == pygame.K_i):
                #playsound(sounds[7])
                block8 = pygame.draw.rect(surface,RED,(800,100,50,150))
                pygame.display.update()
                sound8.play()
                print("i pressed")
                continue
            elif(event.key == pygame.K_o):
                #playsound(sounds[8])
                block9 = pygame.draw.rect(surface,RED,(900,100,50,150))
                pygame.display.update()
                sound9.play()
                print("o pressed")
                continue
            elif(event.key == pygame.K_p):
                #playsound(sounds[9])
                block10 = pygame.draw.rect(surface,RED,(1000,100,50,150))
                pygame.display.update()
                sound10.play()
                print("p pressed")
                continue
            elif(event.key == pygame.K_LEFTBRACKET):
                #playsound(sounds[10])
                block11 = pygame.draw.rect(surface,RED,(1100,100,50,150))
                pygame.display.update()
                sound11.play()
                print("[ pressed")
                continue
            elif(event.key == pygame.K_RIGHTBRACKET):
                #playsound(sounds[11])
                block12 = pygame.draw.rect(surface,RED,(1200,100,50,150))
                pygame.display.update()
                sound12.play()
                print("] pressed")
                continue
            else:
                print("Non-sound Input")
                flag = False
        elif(event.type == pygame.KEYUP):
            block1 = pygame.draw.rect(surface,WHITE,(100,100,50,150))
            block2 = pygame.draw.rect(surface,WHITE,(200,100,50,150))
            block3 = pygame.draw.rect(surface,WHITE,(300,100,50,150))
            block4 = pygame.draw.rect(surface,WHITE,(400,100,50,150))
            block5 = pygame.draw.rect(surface,WHITE,(500,100,50,150))
            block6 = pygame.draw.rect(surface,WHITE,(600,100,50,150))
            block7 = pygame.draw.rect(surface,WHITE,(700,100,50,150))
            block8 = pygame.draw.rect(surface,WHITE,(800,100,50,150))
            block9 = pygame.draw.rect(surface,WHITE,(900,100,50,150))
            block10 = pygame.draw.rect(surface,WHITE,(1000,100,50,150))
            block11 = pygame.draw.rect(surface,WHITE,(1100,100,50,150))
            block12 = pygame.draw.rect(surface,WHITE,(1200,100,50,150))
            pygame.display.update()