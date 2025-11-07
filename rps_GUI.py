#1- all imports
import pygame, pygwidgets, sys, random 

#GUI = Graphical User Interface

#2- define constants
WINDOW_WIDTH = 1100
WINDOW_HEIGHT = 850
BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (0,0,255)
PURPLE = (180,167,214)
UPCLR = (144,238,144)
HVRCLR = (0, 100, 0)
FPS = 24

#3- initialise the world
pygame.init()
pygame.font.init()
window=pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT)) 

clock = pygame.time.Clock()

#4- load assets,images,sounds
title = pygwidgets.DisplayText(window , ((WINDOW_WIDTH-350)//2 , 30), "Rock Paper Scissor","comicsansms",33,width=350,textColor=BLACK,justified="center",)

start_button = pygwidgets.Image(window,(380 , 250),"playbutton12345.png")

#make rock, paper, scissor images
rock_img = pygame.image.load("rock.png")
rock_img_small = pygame.transform.scale(rock_img,(225,225))
rock_button = pygwidgets.Image(window,(50 , 75), rock_img_small)

paper_img = pygame.image.load("paper.png")
paper_img_small = pygame.transform.scale(paper_img,(225,225))
paper_button = pygwidgets.Image(window,(50 , 325), paper_img_small)

scissor_img = pygame.image.load("scissor.png")
scissor_img_small = pygame.transform.scale(scissor_img,(225,225))
scissor_button = pygwidgets.Image(window,(50 , 565), scissor_img_small)


computer_button = pygwidgets.Image(window,(20000 , 325), scissor_img_small)

exit_button_img = pygame.image.load("correctexitbutton.png")
exit_button_imgsmall = pygame.transform.scale(exit_button_img,(100,100))
exit_button_real = pygwidgets.Image(window, (995,1),exit_button_imgsmall)

player_score = 0
com_score = 0

player_score_text = pygwidgets.DisplayText(window, (430, 80), f"Player:{player_score}","comicsansms",30,textColor=PURPLE,justified="center" )
com_score_text = pygwidgets.DisplayText(window, (570, 80), f"Computer:{com_score}","comicsansms",30,textColor=BLUE,justified="center" )

next_button_img = pygame.image.load("nextround.png")
next_button_supasmall = pygame.transform.scale(next_button_img,(125,100))
next_button_realpotato = pygwidgets.Image(window, (995,750), next_button_supasmall)

computer_selection  = ""
player_selection = ""

gamestate = "intro"

#5- loop forever.......loop forever.......
while True:
    #6 - check for handle events
 
    for event in pygame.event.get():
        #quit the screen and system
# to close pygame
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
        if start_button.handleEvent(event):
            gamestate = "OISTART"

        if exit_button_real.handleEvent(event):
            gamestate = "intro"
            player_score = 0
            com_score = 0
            player_score_text.setText(f"Player:{player_score}")
            com_score_text.setText(f"Computer:{com_score}")
        if rock_button.handleEvent(event) and gamestate == "OISTART":
            player_selection = "rock"
            rock_button = pygwidgets.Image(window, (300,315), rock_img_small)
            gamestate = "compPlay"
        
        if paper_button.handleEvent(event) and gamestate == "OISTART":
            player_selection = "paper"
            paper_button = pygwidgets.Image(window, (300,315), paper_img_small )
            gamestate = "compPlay"

        if scissor_button.handleEvent(event) and gamestate == "OISTART":
            player_selection = "scissor"
            scissor_button = pygwidgets.Image(window, (300,315), scissor_img_small )
            gamestate = "compPlay"

        if next_button_realpotato.handleEvent(event) and gamestate == "nextRound":
            rock_button = pygwidgets.Image(window,(50 , 75), rock_img_small)
            paper_button = pygwidgets.Image(window,(50 , 325), paper_img_small)
            scissor_button = pygwidgets.Image(window,(50 , 565), scissor_img_small)
            computer_button = pygwidgets.Image(window,(20000 , 325), scissor_img_small)
            gamestate = "OISTART"
            #STOP
    if gamestate == "compPlay": 
        r = random.randint(1,3)
        gamestate = "checkWin"
        if r == 1:
            computer_selection = "rock"
            computer_button = pygwidgets.Image(window, (540,315), rock_img_small)
        if r == 2:
            computer_selection = "paper"
            computer_button = pygwidgets.Image(window, (540,315), paper_img_small)
        if r == 3:
            computer_selection = "scissor"
            computer_button = pygwidgets.Image(window, (540,315), scissor_img_small)
    
    
    if gamestate == "checkWin":
        print(f"player: {player_selection}, computer: {computer_selection}")
        if player_selection == "paper" and computer_selection == "rock":
            player_score = player_score + 1
            gamestate = "nextRound"
        elif player_selection == "paper" and computer_selection == "scissor":
            com_score = com_score + 1
            gamestate = "nextRound"
        elif player_selection == "paper" and computer_selection == "paper":
            gamestate = "nextRound"
        elif player_selection == "rock" and computer_selection == "scissor":
            player_score = player_score + 1
            gamestate = "nextRound"
        elif player_selection == "rock" and computer_selection == "paper":
            com_score = com_score + 1
            gamestate = "nextRound"
        elif player_selection == "rock" and computer_selection == "rock":
            gamestate = "nextRound"
        elif player_selection == "scissor" and computer_selection == "paper":
            player_score = player_score + 1
            gamestate = "nextRound"
        elif player_selection == "scissor" and computer_selection == "rock":
            com_score = com_score + 1
            gamestate = "nextRound"
        elif player_selection == "scissor" and computer_selection == "scissor":
            gamestate = "nextRound"
       
        player_score_text.setText(f"Player:{player_score}")
        com_score_text.setText(f"Computer:{com_score}")
        
            
    if gamestate == "intro":
        rock_button = pygwidgets.Image(window,(50 , 75), rock_img_small)
        paper_button = pygwidgets.Image(window,(50 , 325), paper_img_small)
        scissor_button = pygwidgets.Image(window,(50 , 565), scissor_img_small)
        computer_button = pygwidgets.Image(window,(2000 , 325), scissor_img_small)

        rock_button.hide()
        paper_button.hide()
        scissor_button.hide()
        computer_button.hide()
        exit_button_real.hide()
        start_button.show()
        player_score_text.hide()
        com_score_text.hide()
        next_button_realpotato.hide()
    if gamestate == "OISTART":
        rock_button.show()
        paper_button.show()
        scissor_button.show()
        computer_button.show()
        exit_button_real.show()
        player_score_text.show()
        com_score_text.show()
        start_button.hide()
        next_button_realpotato.hide()
    if gamestate == "nextRound":
        next_button_realpotato.show()

    #7 -do any every frame actions


    #8- clear the Windows
    window.fill(WHITE)


    #9- draw all window elements 
    title.draw()
    start_button.draw()
    rock_button.draw()
    paper_button.draw()
    scissor_button.draw()
    computer_button.draw()
    exit_button_real.draw()
    com_score_text.draw()
    player_score_text.draw()
    next_button_realpotato.draw()


    #10- update the window 
    pygame.display.update()


    #11- set FPS
    clock.tick(FPS) #slow while loop a little




































