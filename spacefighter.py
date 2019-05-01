from gamelib import*

game = Game(800,600,"Space Fighter")
bk = Image("worldspace.png",game)
spacestory = Image("spacestory.png",game)
spacestory.resizeTo(800,600)

title = Image("title.png",game)
title.resizeTo(500,200)
title.y-=150

play = Image("play.png",game)
play.resizeTo(200,100)
play.y+=20

story = Image("story.png",game)
story.resizeTo(200,100)
story.y+=150

heroship = Image("heroship.png",game)
heroship.resizeBy(-50)
heroship.y+=150

enemyship = Image("enemyship.png",game)
enemyship.resizeBy(-50)
enemyship.y-=150

explosion = Animation("explosion1.png",20,game,1254/20,64)
explosion.visible = False

#Minion Setup
minion = []
for index in range(50):
    minion.append(Animation("minion.png",1,game,564,383))

for index in range(50):
    x = randint(100,700)
    y = randint(100,1400)
    minion[index].moveTo(x,-y)
    minion[index].setSpeed(6,180)

#Ammo Setup
ammo = []
for index in range(20):
    ammo.append(Animation("ammo.png",11,game,352/11,32))

for index in range(20):
    x = randint(100,700)
    y = randint(100,1400)
    ammo[index].moveTo(x,-y)
    ammo[index].setSpeed(6,180)
game.setBackground(bk)

#title screen
while not game.over:
    game.processInput()

    game.scrollBackground("down",3)
    bk.draw()
    title.draw()
    play.draw()
    story.draw()
    game.update(30)
    spacestory.draw()
    story.visible=True
    spacestory.visible=False
    if story.collidedWith(mouse)and mouse.LeftClick:
        game.over = True
        spacestorystory.visible=True
        game.update(30)

    if play.collidedWith(mouse) and mouse.LeftClick:
        game.over = True
        
    game.update(30)

game.over = True

#Level 1
ammocount = 0
while not game.over:
    game.processInput()

    game.scrollBackground("down",2)
    heroship.draw()
    explosion.draw(False)
    enemyship.draw()
    #minion

    for index in range(50):
        minion[index].move()
        if minion[index].collidedWith(hero):
            hero.health -=2
            explosion.moveTo(minion[index].x,minion[index].y)
            explosion.visible = True
        if minion[index].isOffScreen("bottom") and minion[index].visible:
            minionPassed +=1
            minion[index].visible = False

        if minionPassed >=50:
            game.over = True

for index in range(20):
    ammo[index].move()
    if ammo[index].collidedWith(heroship):
        ammocount +=0.5
        ammo[index].visible = True

game.update(30)
game.over=True

game.quit()

