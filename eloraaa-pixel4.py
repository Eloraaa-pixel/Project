import pygame
from pygame import display, font, event
from pygame.locals import *

# Setup display
pygame.init()
screen = display.set_mode()
display.set_caption("Capstone 2")
myFont = font.SysFont('arial', 25)  # Choose a font to use in game

# Directions displayed throughout game
directions = "Please press the 'Y' key for yes and the 'N' key for no."

# Counts how many questions have been asked
currentQuestion = 0


# Determines which question to ask
def story(answer, count):
    screen.fill("white")
    if count == 0:
        question1(answer)
    elif count == 1:
        question2(answer)
    elif count == 2:
        question3(answer)
    elif count == 3:
        end(answer)


# Displays the first part of the story
def intro():
    # Break up the string into multiple variables because there isn't text wrapping in Pygame
    intro1 = "One day, there was Yeti who was an art teacher named Mr. Abobinimal."
    intro2 = "Today he was teaching his students art!"
    intro3 = "Although it's -45 degrees out, he wants him and his students to go out and sketch."
    q1 = "Do you think they should go outside? Yes or no?"

    screen.fill("white")
    textSurface = myFont.render(intro1, True, "black")
    screen.blit(textSurface, (10, 10))
    textSurface = myFont.render(intro2, True, "black")
    screen.blit(textSurface, (10, 40))
    textSurface = myFont.render(intro3, True, "black")
    screen.blit(textSurface, (10, 70))
    textSurface = myFont.render(q1, True, "black")
    screen.blit(textSurface, (10, 100))
    textSurface = myFont.render(directions, True, "black")
    screen.blit(textSurface, (10, 130))


# Answer to the first question
def question1(answer):
    if answer == K_y:
        yes1 = "The kids headed out and put on their winter stuff so that they weren't cold."
        yes2 = "Eventually, they hear a very ferocious beast yell ROAR!"
        q2 = "Should they see what caused the sound? Yes or no?"

        textSurface = myFont.render(yes1, True, "black")
        screen.blit(textSurface, (10, 10))
        textSurface = myFont.render(yes2, True, "black")
        screen.blit(textSurface, (10, 40))
        textSurface = myFont.render(q2, True, "black")
        screen.blit(textSurface, (10, 70))
        textSurface = myFont.render(directions, True, "black")
        screen.blit(textSurface, (10, 100))

    elif answer == K_n:
        no1 = "These kids were glad! He had eventually changed his mind."
        no2 = "Although it's freezing out there, they watch droplets of snow fall down."
        no3 = "Suddenly, they hear a loud rumble! "
        no4 = "All the kids scrambled in fear. Although they want to investigate."
        q2 = "Should the kids and Mr. Abobinimal figure out this problem? Yes or no?"

        textSurface = myFont.render(no1, True, "black")
        screen.blit(textSurface, (10, 10))
        textSurface = myFont.render(no2, True, "black")
        screen.blit(textSurface, (10, 40))
        textSurface = myFont.render(no3, True, "black")
        screen.blit(textSurface, (10, 70))
        textSurface = myFont.render(no4, True, "black")
        screen.blit(textSurface, (10, 100))
        textSurface = myFont.render(q2, True, "black")
        screen.blit(textSurface, (10, 130))
        textSurface = myFont.render(directions, True, "black")
        screen.blit(textSurface, (10, 160))


# Answer to the second question
def question2(answer):
    if answer == K_y:
        yes1 = "Mr. Abobinimal and the students follow a mysterious cave."
        textSurface = myFont.render(yes1, True, "black")
        screen.blit(textSurface, (10, 10))

    elif answer == K_n:
        no1 = "They got frightened, but still decided to be brave."
        textSurface = myFont.render(no1, True, "black")
        screen.blit(textSurface, (10, 10))

    story2 = "As they're going through this random cave,"
    story3 = "they hear a bunch of grumbling noises."
    story4 = "What's this? They wonder with fear."
    q3 = "Do you think they should enter the cave? Yes or no?"

    textSurface = myFont.render(story2, True, "black")
    screen.blit(textSurface, (10, 40))
    textSurface = myFont.render(story3, True, "black")
    screen.blit(textSurface, (10, 70))
    textSurface = myFont.render(story4, True, "black")
    screen.blit(textSurface, (10, 100))
    textSurface = myFont.render(q3, True, "black")
    screen.blit(textSurface, (10, 130))
    textSurface = myFont.render(directions, True, "black")
    screen.blit(textSurface, (10, 160))


# Answer to the third question
def question3(answer):
    if answer == K_y:
        yes1 = "They enter the cave."
        yes2 = "Turns out, it's a pretty large place"
        yes3 = "It may have been sunny out, but in the cave it was dark."
        yes4 = "They all acted scared at first, but then the noises began to stop."
        q4 = "Should they go any deeper? Yes or No?"

        textSurface = myFont.render(yes1, True, "black")
        screen.blit(textSurface, (10, 10))
        textSurface = myFont.render(yes2, True, "black")
        screen.blit(textSurface, (10, 40))
        textSurface = myFont.render(yes3, True, "black")
        screen.blit(textSurface, (10, 70))
        textSurface = myFont.render(yes4, True, "black")
        screen.blit(textSurface, (10, 100))
        textSurface = myFont.render(q4, True, "black")
        screen.blit(textSurface, (10, 130))
        textSurface = myFont.render(directions, True, "black")
        screen.blit(textSurface, (10, 160))

    elif answer == K_n:
        no1 = "The teacher and students hesitate for a moment,"
        no2 = "they realized as long as they didn't get eaten, they're fine."
        no3 = "They leave it to themselves to find the monster,"
        no4 = "but still, they're wondering IF they should do it."
        q4 = "Should they find the monster?"

        textSurface = myFont.render(no1, True, "black")
        screen.blit(textSurface, (10, 10))
        textSurface = myFont.render(no2, True, "black")
        screen.blit(textSurface, (10, 40))
        textSurface = myFont.render(no3, True, "black")
        screen.blit(textSurface, (10, 70))
        textSurface = myFont.render(no4, True, "black")
        screen.blit(textSurface, (10, 100))
        textSurface = myFont.render(q4, True, "black")
        screen.blit(textSurface, (10, 130))
        textSurface = myFont.render(directions, True, "black")
        screen.blit(textSurface, (10, 160))


# This is the ending
def end(answer):
    if answer == K_y:
        yes1 = "Suspense fills the air as they uncover this beast."
        end1 = "After the time being used to find the monster,"
        end2 = "it ended up being Mr. Abobinimal's lost baby!"
        end3 = "Turns out, Mr. Abobinimal has been looking for his baby for three days!"
        end4 = "The act of bravery to find him wasn't that bad."
        end5 = "Moral of the story (sort of) is to expect the unexpected"
        end6 = "The end!"

        textSurface = myFont.render(yes1, True, "black")
        screen.blit(textSurface, (10, 10))
        textSurface = myFont.render(end1, True, "black")
        screen.blit(textSurface, (10, 40))
        textSurface = myFont.render(end2, True, "black")
        screen.blit(textSurface, (10, 70))
        textSurface = myFont.render(end3, True, "black")
        screen.blit(textSurface, (10, 100))
        textSurface = myFont.render(end4, True, "black")
        screen.blit(textSurface, (10, 130))
        textSurface = myFont.render(end5, True, "black")
        screen.blit(textSurface, (10, 160))
        textSurface = myFont.render(end6, True, "black")
        screen.blit(textSurface, (10, 190))

    elif answer == K_n:
        no1 = "They may have not gone any deeper,"
        end1 = "but they still found out who is was."
        end2 = "It was Mr. Abobinimal's child. Who's name was apparentley, Abob Jr."
        end3 = "They ended the journey with peace and everyone was safe."
        end4 = "The end!"

        textSurface = myFont.render(no1, True, "black")
        screen.blit(textSurface, (10, 10))
        textSurface = myFont.render(end1, True, "black")
        screen.blit(textSurface, (10, 40))
        textSurface = myFont.render(end2, True, "black")
        screen.blit(textSurface, (10, 70))
        textSurface = myFont.render(end3, True, "black")
        screen.blit(textSurface, (10, 100))
        textSurface = myFont.render(end4, True, "black")
        screen.blit(textSurface, (10, 130))


# Game loop
while True:
    # Checks to see if at beginning of game
    if currentQuestion == 0:
        intro()

    # Get the most recent event
    currentEvent = event.poll()

    # Displays the correct question based on event that occurs
    if currentEvent.type == KEYDOWN:
        story(currentEvent.key, currentQuestion)
        currentQuestion = currentQuestion + 1

    # add text to screen
    display.update()
