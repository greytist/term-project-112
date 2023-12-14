from cmu_graphics import *
from PIL import Image
from textInListForm import *
from changeListOriginal import *
import random
import copy

class Character:
    charDict=dict()#go into this to get characters, they r stored here
    currentExpression="happy"
    talkingTo = None #"Blake", "Charlie", or None
    def __init__(self, charList): #charList is a list of char name in[0] and sprite dict in [1]
        self.name=charList[0]
        #relation is how much character likes player
        Character.charDict[self.name]={"sprites":charList[1],
                                        "relation":10,
                                        "self": self}

    def __repr__(self):
        return f'name={self.name}, relation={Character.charDict[Character.talkingTo]["relation"]}'

    @staticmethod
    def addRelation(amountAdd):
        if isinstance(amountAdd, int):
            curRelation = Character.charDict[Character.talkingTo]["relation"]
            curRelation +=amountAdd
            if curRelation>100:
                curRelation=100
            Character.charDict[Character.talkingTo]["relation"] = curRelation

    @staticmethod
    def removeRelation(amountRemove):
        if isinstance(amountRemove, int):
            curRelation = Character.charDict[Character.talkingTo]["relation"]
            curRelation-=amountRemove
            if curRelation<0:
                curRelation=0
            Character.charDict[Character.talkingTo]["relation"] = curRelation
    
class Player:
    def __init__(self, name):
        self.name=name
        self.smarts=10#get from studying/lose from skipping class
        # self.hunger=100#100 is not hungry, fill by eating 

    def __repr__(self):
        return f'Player name = {self.name}, smarts={self.smarts}'#, hunger={self.hunger}'

    def study(self, amountStudied):
        if isinstance(amountStudied, int):
            self.smarts+=amountStudied
            if self.smarts>100:
                self.smarts=100
    
    def getDumb(self, amountLost):
        if isinstance(amountLost, int):
            self.smarts-=amountLost
            if self.smarts<0:
                self.smarts=0

class GameState():
    daysLeft=2
    gameStateDict=dict()
    curGameState="titleScreen"

    #gameState will take in a variable that is a dict, that includes the name\
    #of the state, the background, and more

    def __init__(self, stateName, gameStates): #statename is string
        self.name=gameStates[stateName]["name"]#name will be same as background
        self.background=gameStates[stateName]["background"]
        GameState.gameStateDict[self.name]={"background":self.background}

    def __repr__(self):
        return f'name={self.name} and background={self.background}'
    
    @staticmethod
    def nextDay():
        GameState.daysLeft-=1
    
    @staticmethod
    def curBackground():
        return(GameState.gameStateDict[GameState.curGameState]["background"])

    @staticmethod
    def changeState(newState):
        GameState.curGameState = newState

#amalia told me to make a class for buttons (such good advice)
class Button:
    def __init__(self, name, x, y, width, height, color, size, functionCall, *functionParameters):
        self.name = name
        self.x, self.y = x, y
        self.width = width
        self.height = height
        self.color = color
        self.wordSize = size
        self.functionCall = functionCall
        self.parameter = functionParameters
        pass
    
    def __repr__(self):
        return(str(self.name))
    
    def __hash__(self):
        return(hash(str(self.name)))

    def pressButton(self, app):
        self.functionCall(*self.parameter)
        pass

    def drawButton(self, app):
        drawRect(self.x, self.y, self.width, self.height, fill=self.color, align="center", border="black")
        drawLabel(self.name, self.x, self.y, size=self.wordSize)
        pass

#######################
#     CHARACTERS      #
#######################

def loadCharacters(app):
    charlieExpressionSprites =\
        {
            "happy":"charlieHappy.png",
            "upset":"charlieUpset.png" 
        }
    Charlie =  ["Charlie", charlieExpressionSprites]
    Character(Charlie)

    blakeExpressionSprites =\
        {
            "happy":"blakeHappy.png",
            "upset":"blakeUpset.png"
        } 
    Blake = ["Blake", blakeExpressionSprites]
    Character(Blake)

#######################
#     GAME STATES     #
#######################

#background screens cropped and edited by David Lu
def loadGameStates(app):
    stateNames=["titleScreen", "morningTime", "dayTime", "nightTime", "insideDorm", "laPrima", "dohurty", "abp"]
#image citations are in a different text file called "imageCitations"
    gameStates=\
        {"titleScreen":{"background":app.titlemage, "name":"titleScreen"}, 
         "morningTime":{"background":app.morningmage, "name":"morningTime"},
         "dayTime":{"background":app.daymage, "name":"dayTime"},
         "nightTime":{"background":app.nightmage, "name":"nightTime"},
         "insideDorm":{"background":app.dormmage, "name":"insideDorm"},
         "laPrima":{"background":app.primmage, "name":"laPrima"},
         "dohurty":{"background":app.dohurty, "name":"dohurty"}, #this is doherty
         "abp":{"background":app.abpmage, "name":"abp"}
         }
    for name in stateNames:
        GameState(name, gameStates)

######################
#       Buttons      #
######################

def loadButtons(app):
    #titleScreenButtons
    app.titleStartButton = Button("Start", app.width//2, app.height//4*3, app.width//4, app.height//6, "violet", 30, GameState.changeState, "insideDorm")
    app.controlsMenuButton = Button("Controls",app.width//3,app.height//2+25,app.width//4, app.height//7, "violet", 22, showControlsMenu, app)
    app.controlsBackButton = Button("Back",app.width//2, app.height//4*3, app.width//5, app.height//7, "violet", 22, showControlsMenu, app)
    app.acknowledgementsMenuButton = Button("Acknowledgements",app.width//3*2,app.height//2+25,app.width//4, app.height//7, "violet", 22, showAcknowledgementsMenu, app)
    app.acknowledgementsBackButton = Button("Back",app.width//2, app.height//4*3, app.width//5, app.height//7, "violet", 22, showAcknowledgementsMenu, app)
    app.drawLaPrimaControlsButton = Button("Controls",app.width//2, 75, app.width//5, 75, "violet", 20, showLaPrimaControls, app)
    app.drawLaPrimaBackButton = Button("Back",app.width//2, 75, app.width//5, 75, "violet", 20, showLaPrimaControls, app)
    app.statsMenuButton = Button("Stats", 125,45,100,40,"violet",18,showStatsMenu,app)
    app.statsBackButton = Button("Back", 125,45,100,40,"violet",18,showStatsMenu,app)
    app.nextDayButton = Button("Start Next Day!", app.width//2,app.height//2,400,300,"violet",50,goToSleep,app)
    app.endGameExitButton = Button("EXIT", app.width//2,app.height//4*3,200,100,"lavenderblush",25,app.quit)

def loadDialogueButtons(app):
    #dialogueButtons 
    app.responceOption1 = Button(app.text[1][0][0], app.width//4*3, app.height//3, 200, 60, "violet", 20, chooseDialogue, app, 2)# 2 is index to choose
    app.responceOption2 = Button(app.text[1][1][0], app.width//4*3, app.height//3+100, 200, 60, "violet", 20, chooseDialogue, app, 3)# 3 is index to choose

def loadLectureButtons(app, answers):
    #lecture game buttons
    app.lectureButton1 = Button(answers[0], 250,300,260,80,"white",22,pickAnswer,app,answers[0])
    app.lectureButton2 = Button(answers[1], 250,400,260,80,"white",22,pickAnswer,app,answers[1])
    app.lectureButton3 = Button(answers[2], 550,300,260,80,"white",22,pickAnswer,app,answers[2])
    app.lectureButton4 = Button(answers[3], 550,400,260,80,"white",22,pickAnswer,app,answers[3])

################################################################################
#main game code happens here:###################################################
################################################################################

def onAppStart(app):
    app.width, app.height = 800, 600
    createCMUImages(app)
    loadCharacters(app)
    loadGameStates(app)
    loadVariables(app)
    loadBoard(app)
    loadButtons(app)
    loadLectureGame(app)
    pass

def loadVariables(app):
    app.currentNameEntry = ""
    app.playerName = None
    app.askingForName = False
    app.talking = True
    app.responding = False
    app.currentButtons = []
    app.minigame = "" #laPrima or lectureCheck
    app.minigameOver = False
    app.text = createTextList(app)
    app.changeStatesList = changes

    app.acknowledgementsMenu=False
    app.controlsMenu=False
    app.showStats=False
    app.primaControls=False
    app.plsClickForNextDay=False
    app.startingEndgame=False
    app.showGameOver=False
    app.gameOverMessage=None
    app.ending=False

def loadBoard(app):
    app.rows, app.cols = 14, 14
    app.board = [([None] * app.cols) for row in range(app.rows)]
    app.boardWidth = 600
    app.boardHeight = 500
    app.boardTop, app.boardLeft = 50, 100
    app.occupied = (12,12)
    app.goal = (2,2)
    app.coffee = [(1,2), app.coffeeCup, False]
    app.randomObjects = []
    app.constantObjects = [(0,1),(0,12),(1,1),(1,2),(1,3),(1,4),(1,5),(1,6),(1,7),(1,8),(1,9),
                   (1,10),(1,11),(1,12),(2,12),(3,12),(4,12),(5,12),(6,12),(7,12),(8,12),
                   (9,12),(10,12),(10,13)]
    makeRandomObjects(app)

def loadLectureGame(app):
    app.questions = loadLectureQuestions(app)
    app.lectureGameStarted=False
    app.lectureGameOver=False
    app.lecturePassed=None
    app.currentCorrectAnswer = None

def createCMUImages(app):
    app.titlemage = CMUImage(Image.open("titleScreen.png"))
    app.morningmage = CMUImage(Image.open("morningTime.png"))
    app.daymage = CMUImage(Image.open("dayTime.png"))
    app.nightmage = CMUImage(Image.open("nightTime.jpg"))
    app.dormmage = CMUImage(Image.open("insideDorm.png"))
    app.primmage = CMUImage(Image.open("laPrima.jpg"))
    app.dohurty = CMUImage(Image.open("dohurty.jpg"))
    app.abpmage = CMUImage(Image.open("abp.png"))

    app.blakeHappy = CMUImage(Image.open("blakeHappy.png"))
    app.blakeUpset = CMUImage(Image.open("blakeUpset.png"))
    app.charlieHappy = CMUImage(Image.open("charlieHappy.png"))
    app.charlieUpset = CMUImage(Image.open("charlieUpset.png"))

    app.chair = CMUImage(Image.open("chair.png"))
    app.coffeeCup = CMUImage(Image.open("coffeeCup.png"))

def redrawAll(app):
    #draw current background
    drawBackground(app)
    #draw title menus
    drawControlsMenu(app)
    drawAcknowledgementsMenu(app)
    #draw any characters on screen
    drawCharacters(app)
    #draw text boxes and text over characters
    drawTextBoxes(app)
    #show stats over characters
    drawStatsMenu(app)
    drawGameOverScreen(app)
    #when needed, start a minigame
    drawMinigames(app)
    drawLaPrimaControls(app)
    #draw the clickable buttons
    drawButtons(app)

def drawBackground(app):
    drawImage(GameState.curBackground(), app.width//2, app.height//2, align="center")
    if GameState.curGameState == "titleScreen":
        #add words and buttons and shapes here
        drawRect(app.width//2, app.height//4, 650, 200, fill="violet", align="center", opacity=84) #title box
        drawLabel("Getting a Date at CMU!", app.width//2, app.height//4-20, size=60) #title
        drawLabel("(Is it even possible!?)", app.width//2, app.height//4+25, size=20) #subtitle

def showControlsMenu(app): #accessed by buttons
    app.controlsMenu = not app.controlsMenu

def drawControlsMenu(app):
    if app.controlsMenu:
        drawRect(0,0,app.width,app.height,fill="palegreen")
        drawRect(20,20,app.width-20,app.height-40,fill="darkseagreen")
        drawRect(app.width//8-15,app.height//8,app.width//4*3+20,315, fill="palegreen", border="grey")

        drawLabel("GENERAL CONTROLS",app.width//2,app.height//4-30,size=26,bold=True)
        drawLabel("Buttons must be clicked with the mouse!",app.width//2,app.height//4+5,size=18)
        drawLabel("Spacebar, enter, and mouse click all progress the dialogue.",app.width//2,app.height//4+35,size=18)
        drawLabel("When you meet the in game characters, dialogue choices can appear.",app.width//2,app.height//4+65,size=18)
        drawLabel("Depending on the choice you make, your relationship with them will change.",app.width//2,app.height//4+95,size=18)
        drawLabel("When doing lecture, you gain smarts if correct, or lose some if wrong.",app.width//2,app.height//4+125,size=18)
        drawLabel("The quality of your stats change the ending! Pay attention!",app.width//2,app.height//4+155,size=18)

def showAcknowledgementsMenu(app):#accessed by buttons
    app.acknowledgementsMenu=not app.acknowledgementsMenu

def drawAcknowledgementsMenu(app):
    if app.acknowledgementsMenu:
        drawRect(0,0,app.width,app.height,fill="peru")
        drawRect(20,20,app.width-40,app.height-40,fill="sienna")
        drawRect(app.width//8-5,app.height//8,app.width//4*3,app.height//3+100, fill="peru", border="saddlebrown")

        drawLabel("ACKNOWLEDGEMENTS",app.width//2,app.height//8+30,bold=True,size=26)
        drawLabel("Thank you to these people who gave me fun Trivia questions:",app.width//2,app.height//8+60,size=17)
        drawLabel("Kenechukwu Echezona, Justin Peng, Chieri Nnadozie",app.width//2,app.height//8+90,size=17)
        drawLabel("Thank you to these people who I explained how my code was",app.width//2,app.height//8+120,size=17)
        drawLabel("supposed to work to, which made me realize how much it didn't:",app.width//2,app.height//8+150,size=17)
        drawLabel("David Lu, Eshaan Joshi",app.width//2,app.height//8+180,size=17)
        drawLabel("Thank you to my friend David Lu who edited all the pictures",app.width//2,app.height//8+210,size=17)
        drawLabel("Thanks to my very cool TP mentor Amalia Akamon for all the help :)",app.width//2,app.height//8+240,size=17)

def showStatsMenu(app):#accessed by buttons
    app.showStats= not app.showStats

def drawStatsMenu(app):
    if app.showStats:
        drawRect(0,0,app.width,app.height,fill="pink")
        drawRect(app.width//4,app.height//4+25,350,100,align="center",fill="lightcyan",border="turquoise")
        drawRect(app.width//4*3,app.height//4+25,350,100,align="center",fill="lightcyan",border="turquoise")
        drawRect(app.width//2,app.height//3*2-25,300,100,align="center",fill="lightcyan",border="turquoise")
        drawLabel("Relationship with Blake", app.width//4, app.height//4,size=28)
        drawLabel(str(Character.charDict["Blake"]["relation"])+"/100", app.width//4,app.height//3,size=22)
        drawLabel("Relationship with Charlie", app.width//4*3, app.height//4,size=28)
        drawLabel(str(Character.charDict["Charlie"]["relation"])+"/100", app.width//4*3,app.height//3,size=22)
        drawLabel("Your smarts",app.width//2,app.height//2+50,size=28)
        if app.playerName!=None:
            drawLabel(str(app.Name.smarts)+"/100",app.width//2,app.height//3*2,size=22)
        else: 
            drawLabel("10/100",app.width//2,app.height//3*2,size=22)

def drawGameOverScreen(app):
    #dont need a show variable because once you get to game over you cant go back
    if app.ending==True and app.showGameOver==True and app.gameOverMessage!=None:
        drawRect(0,0,app.width,app.height,fill="purple")
        drawRect(20,20,app.width-40,app.height-40,fill="violet")
        drawRect(app.width//2,150,app.width-50,150,fill="lavenderblush",border="purple",align="center")
        drawLabel(app.gameOverMessage,app.width//2,150,size=40)

def chooseDialogue(app, index): #this is used by some buttons
    if app.startingEndgame==True:
        candidate=str(app.text[1][index-2][0])
        commenceFinalCountdown(app,candidate)
        app.startingEndgame=False
    elif app.text[1][index-2][1]==1:
        Character.addRelation(5)
    elif app.text[1][index-2][1]==0:
        Character.removeRelation(5)
    elif app.text[1][index-2][1]==2:
        pass
    app.text[1]=app.text[1][index]
    app.changeStatesList[1]=app.changeStatesList[1][index-2]
    app.currentButtons = []
    app.responding=False

def commenceFinalCountdown(app,person):
    if person=="Charlie":
        if Character.charDict["Charlie"]["relation"]>=30 and app.Name.smarts>=35:
            restWords=loadFinalScene(app,"CharlieW")
            restActions=loadEndgameActions("CharlieW")
        elif Character.charDict["Charlie"]["relation"]>=30:
            restWords=loadFinalScene(app,"CharlieNotSmart")
            restActions=loadEndgameActions("CharlieNotSmart")
        else:
            restWords=loadFinalScene(app,"CharlieNotLike")
            restActions=loadEndgameActions("CharlieNotLike")
    elif person=="Blake":
        if Character.charDict["Blake"]["relation"]>=30 and app.Name.smarts>=35:
            restWords=loadFinalScene(app,"BlakeW")
            restActions=loadEndgameActions("BlakeW")
        elif Character.charDict["Blake"]["relation"]>=30:
            restWords=loadFinalScene(app,"BlakeNotSmart")
            restActions=loadEndgameActions("BlakeNotSmart")
        else:
            restWords=loadFinalScene(app,"BlakeNotLike")
            restActions=loadEndgameActions("BlakeNotLike")
    app.ending=True
    app.text.extend(restWords)
    app.changeStatesList.extend(restActions)
    app.currentButtons=[]

def goToSleep(app):
    app.Name.study(10)
    GameState.nextDay()
    app.text=app.text[1:]
    app.changeStatesList=app.changeStatesList[1:]

def getCurrentButtons(app):
    if GameState.curGameState == "titleScreen":
        if app.controlsMenu:
            app.currentButtons = [app.controlsBackButton]
        elif app.acknowledgementsMenu:
            app.currentButtons = [app.acknowledgementsBackButton]
        else: app.currentButtons = [app.titleStartButton, app.controlsMenuButton, app.acknowledgementsMenuButton]
    elif app.minigame=="laPrima":
        if app.primaControls==True:
            app.currentButtons=[app.drawLaPrimaBackButton]
        else: app.currentButtons = [app.drawLaPrimaControlsButton]
    elif app.showStats==True:
        app.currentButtons = [app.statsBackButton]
    elif app.responding==True:
        app.currentButtons = [app.responceOption1, app.responceOption2, app.statsMenuButton]
    elif app.minigame=="lectureCheck" and app.lectureGameStarted==True:
        app.currentButtons = [app.lectureButton1, app.lectureButton2, app.lectureButton3, app.lectureButton4]
    elif app.plsClickForNextDay==True:
        app.currentButtons = [app.nextDayButton, app.statsMenuButton]
    elif app.showGameOver:
        app.currentButtons = [app.endGameExitButton]
    else:
        app.currentButtons = [app.statsMenuButton]
    
def onStep(app):
    getCurrentButtons(app)
    if app.showGameOver==False:
        changeStatesWithText(app, app.changeStatesList)
        if app.ending==True and len(app.text)<=1:
            app.showGameOver=True
        # if isinstance(app.text[1][0], list):
        elif len(app.text)>1 and isinstance(app.text[1][0], list):
            loadDialogueButtons(app)

def makeTextTypeItself(app, text):
    #text will be a 2d list where each row is one row of text on screen and each list itself is all the text that can fit at once
    if Character.talkingTo!=None:
        x, y = 60, app.height//2+110
    else: x, y = 60, app.height//2+100
    for row in range(len(text[0])):
        drawLabel(text[0][row], x, y+(30*row), size=18, align="left")

def changeStatesWithText(app, changes):
    #this takes in a list that is connected to the dialogue so as the story 
    #progresses the things that are happening on screen and stuff progress too
    if app.askingForName!=True:
        if GameState.curGameState!="titleScreen":
            if changes[0][0]!=0:
                GameState.curGameState=changes[0][0]
            if changes[0][1]!=0:
                Character.talkingTo=changes[0][1]
            else: Character.talkingTo = None
            if changes[0][2]!=0:
                Character.currentExpression=changes[0][2]
            if changes[0][3]!=0:
                app.miniGameOver=False
                app.minigame=changes[0][3]
            else: app.minigame=""        
            if changes[0][4]!=0:
                app.responding=True
            else: app.responding=False
            if changes[0][5]!=0:
                app.talking=True
            else: app.talking=False
            if changes[0][6]!=0:
                app.askingForName=True
            else: app.askingForName=False
            if changes[0][7]!=0:
                app.plsClickForNextDay=True
            else: app.plsClickForNextDay=False
            if changes[0][8]!=0: app.startingEndgame=True
            else: app.startingEndgame=False
            if len(changes[0])>9:
                app.gameOverMessage=changes[0][9]

def onMousePress(app, mouseX, mouseY):
    for button in app.currentButtons:
        if button.x-(button.width//2)<=mouseX<=button.x+(button.width//2) and \
            button.y-(button.height//2)<=mouseY<=button.y+(button.height//2):
            button.pressButton(app)
    if GameState.curGameState!="titleScreen" and app.askingForName!=True and app.minigame==""\
          and app.showStats==False and app.responding==False and app.plsClickForNextDay==False and app.showGameOver==False:
        if (75<=mouseX<=175 and 25<=mouseY<=65)==False: 
            app.text=app.text[1:]
            app.changeStatesList=app.changeStatesList[1:]
    if app.minigame=="lectureCheck":
        if not app.lectureGameStarted: #not in the gameplay
            if app.lecturePassed!=None and app.lectureGameOver==True:#after the end splash screen
                if app.lecturePassed:#if passed
                    app.Name.study(10)
                    app.text[1]=app.text[1][1]
                else: 
                    app.Name.getDumb(2) #if not passed
                    app.text[1]=app.text[1][0]
                app.lectureGameStarted=False
                app.lectureGameOver=False
                app.lecturePassed=None
                app.minigame=""
                app.text=app.text[1:]
                app.changeStatesList=app.changeStatesList[1:]
            else: #title screen
                app.lectureGameStarted=True
                app.triviaLabels=chooseRandomQuestion(app,app.questions) #returns 4 random answers
        elif app.lectureGameStarted == True and app.lectureGameOver==False:#checks button clicks
            for button in app.currentButtons:
                if button.x-(button.width//2)<=mouseX<=button.x+(button.width//2) and \
                    button.y-(button.height//2)<=mouseY<=button.y+(button.height//2):
                    button.pressButton(app)
        elif app.lectureGameStarted == True and app.lecturePassed!=None:#splashscreen
            app.currentButtons=[]
            app.lectureGameOver=True
            app.lectureGameStarted=False
    
def drawTextBoxes(app):
    if GameState.curGameState != "titleScreen":
        if app.talking == True:
            drawRect(20, app.height//2+60, app.width-40, app.height//3, fill="violet", borderWidth=4, border="black")
            if Character.talkingTo != None:
                drawRect(50, app.height//2+30, 150, 60, fill="violet", border="black", borderWidth=3)
                drawLabel(Character.talkingTo, 125, app.height//2+60, bold=True, size=20)
            if app.askingForName == True:
                drawTextAskForName(app)
            else:
                makeTextTypeItself(app, app.text)
        drawRect(app.width-175, 25, 100, 40, fill="violet", border="black")#days left box
        if GameState.daysLeft != 0:
            drawLabel("Days Left: " + str(GameState.daysLeft), app.width-125, 45)        
        else:
            drawLabel("Final Day", app.width-125, 45)                

def drawTextAskForName(app):
    drawLabel("What is your name?", 60, app.height//2+110, size = 20, align="left")
    drawLabel("(Max of 10 characters. Only alphabetical characters and spaces allowed.)", 
              60, app.height//2+140, size=18, align="left")
    drawLabel("(Must have at least one alphabetical character)", 60, app.height//2+170, size=18, align="left")
    drawLabel(">>", 60, app.height//2+200, size=20, align="left")
    drawLabel(app.currentNameEntry, 85, app.height//2+200, size=20, align="left")

def drawCharacters(app):
    if Character.talkingTo == "Blake":
        x,y=100,app.height-560
    elif Character.talkingTo == "Charlie":
        x,y=120,app.height-540
    if GameState.curGameState != "titleScreen" and Character.talkingTo not in [None,"???"]:
        drawImage(Character.charDict[Character.talkingTo]["sprites"][Character.currentExpression],x, y)

def drawButtons(app):
    if app.minigame!="lectureCheck":
        for button in app.currentButtons:
            button.drawButton(app)
        
def drawMinigames(app):
    if app.minigame == "laPrima" and app.minigameOver!=True:
        drawImage(app.primmage,0,0)
        drawRect(100, 50, app.width-200, app.height-100, fill="tan")
        drawBoard(app)
    
    elif app.minigame == "lectureCheck" and app.minigameOver != True:
        drawScreenBorder(app)
        if not app.lectureGameStarted:
            drawStartScreen(app)
        else:
            drawLectureGame(app)
        if app.lectureGameOver:
            drawFinishScreen(app)

def showLaPrimaControls(app):
    app.primaControls=not app.primaControls

def drawLaPrimaControls(app):
    if app.primaControls==True:
        drawRect(0,0,app.width,app.height,fill="palegreen")
        drawRect(20,20,app.width-40,app.height-40,fill="darkseagreen")
        drawRect(app.width//8-5,app.height//4-50,app.width//4*3+10,app.height//4, fill="palegreen", border="grey")
        drawRect(app.width//8-5,app.height//2,app.width//4*3+10,175, fill="palegreen", border="grey")

        drawLabel("LA PRIMA CONTROLS", app.width//2,app.height//3-28,bold=True,size=26)
        drawLabel("Move the green square with the arrow keys. The goal is to get the coffee",app.width//2,app.height//2+55,size=18)
        drawLabel("from the counter(top left) into the light blue end zone(bottom right).",app.width//2,app.height//2+80,size=18)
        drawLabel("When you are in a square next to the coffee cup, press space to pick it up.",app.width//2,app.height//2+105,size=18)
        drawLabel("Bring the coffee cup to the end zone and press space to deliver it.",app.width//2,app.height//2+130,size=18)

#got an idea of how to start this by looking at csacademy 3.11 Number Guessing Game
def onKeyPress(app, key):
    if GameState.curGameState!="titleScreen" and app.showStats==False and app.plsClickForNextDay==False and app.showGameOver==False:
        if app.askingForName == True:
            keyPressPlayerName(app, key)
            if key == "enter":
                app.askingForName = False
        elif (app.minigame not in ["laPrima", "lectureCheck"]) and (app.responding==False):
            if key == "space" or key == "enter":
                app.text=app.text[1:]
                app.changeStatesList=app.changeStatesList[1:]

        if app.minigame == "lectureCheck":
            if key == "space" or key == "enter":
                if not app.lectureGameStarted: #not in the gameplay
                    if app.lecturePassed!=None and app.lectureGameOver==True:#after the end splash screen
                        if app.lecturePassed:
                            app.Name.study(10) #if passed
                            app.text[1]=app.text[1][1]
                        else: 
                            app.Name.getDumb(2) #if not passed
                            app.text[1]=app.text[1][0]
                        app.lectureGameStarted=False
                        app.lectureGameOver=False
                        app.lecturePassed=None
                        app.minigame=""
                        app.text=app.text[1:]
                        app.changeStatesList=app.changeStatesList[1:]
                if not app.lectureGameStarted and not app.lectureGameOver:
                    app.lectureGameStarted=True
                    app.triviaLabels=chooseRandomQuestion(app,app.questions)#returns right answ, 3 wrong answ]

        if app.minigame == "laPrima":
            if key == 'left':    movePerson(app, 0, -1)
            elif key == 'right': movePerson(app, 0, +1)
            elif key == 'up':    movePerson(app ,-1, 0)
            elif key == 'down':  movePerson(app, +1, 0)
            elif key == "space" and app.coffee[2]==False: 
                if app.occupied in [(2,2),(2,1),(2,3)]:
                    app.coffee[2]=True #true means u picked up coffee, pic should disappear
            elif key=="space" and app.coffee[2]==True and app.occupied in [(13,12),(12,12),(11,12),(13,13),(12,13),(11,13)]:
                Character.addRelation(10)
                app.minigameOver=False
                app.minigame=""
                loadBoard(app)
                app.text=app.text[1:]
                app.changeStatesList=app.changeStatesList[1:]

def keyPressPlayerName(app, key):
    #used to enter player name
    if key.isalpha() and (len(key)<2) and len(app.currentNameEntry)<10:
        app.currentNameEntry += key
    if key == "space":
        app.currentNameEntry += " "
    if key == "backspace":
        if len(app.currentNameEntry) >= 1:
            app.currentNameEntry = app.currentNameEntry[:-1]
    if key == "enter":
        if app.currentNameEntry.isspace() or app.currentNameEntry=="":
            pass # WE DO NOT WANT EMPTY NAMES!!
        else:
            app.playerName = app.currentNameEntry
            app.Name = Player(app.playerName)
            app.askingforName = False
            app.text.extend(loadRestOfText(app))
            app.text=app.text[1:]
            app.changeStatesList=app.changeStatesList[1:]

#######################
###     LECTURE     ###
#######################

def drawScreenBorder(app):
    drawRect(0,0,app.width,app.height,fill="lightgrey")
    rectHeight=35
    vars=[(app.width//2, rectHeight), (app.width-rectHeight, app.height//2),
           (app.width//2, app.height-rectHeight),(rectHeight, app.height//2)]
    for i in range(len(vars)):
        drawRect(vars[i][0], vars[i][1], 50, 50, align="center", 
                 rotateAngle=45+(90*i),fill="navy")
        drawRect(vars[i][0], vars[i][1], app.width, rectHeight,
                  rotateAngle=0+(90*i),fill="lightskyblue", align="center", border="blue")

def drawStartScreen(app):
    drawRect(app.width//2, app.height//3, app.width//2+80, app.height//4, fill="white", align="center")
    drawLabel("Lecture Check!", app.width//2, app.height//3-30, size=60)
    drawLabel("Time to see if you paid attention in class today!", app.width//2, app.height//3+30, size=18)
    drawLabel("Press Spacebar, Enter, or click anywhere to begin!", app.width//2, app.height//3*2, size=18)

def drawFinishScreen(app):
    for i in range(10):
        drawRect(app.width//2, app.height//2, app.width-106-(i*30), app.height-100-(i*30), fill="white", opacity=10+(i*10), align="center")
    if app.lecturePassed:
        endMessages=["Yay! You got it right!","You gained +10 knowledge"]
    elif not app.lecturePassed:
        endMessages=["Oh no! You must've missed something :(","You didn't gain any knowledge"]
    for x in range(len(endMessages)):
        #displays appropriate message based on if you chose the right answer
        drawLabel(endMessages[x], app.width//2, app.height//3+(x*100), size=30)

def drawLectureGame(app):
    #draws the question and the buttons
    for k in range(len(app.question)):
        drawLabel(app.triviaLabels[1][k], app.width//2, app.height//4+(45*k), size=38)#question
    if not app.lectureGameOver:
        for button in app.currentButtons:
            Button.drawButton(button, app)

def chooseRandomQuestion(app, questions): 
    questionn = random.choice(list(questions.keys()))
    correctAnswer = questions[questionn]["correctAnswer"]
    app.currentCorrectAnswer = correctAnswer
    answerList = [questionn, questions[questionn]["question"], app.currentCorrectAnswer]
    while len(answerList)<6: #this gets random answers so that it is different every time
        randomWrongAnswer = random.choice(questions[questionn]["incorrectAnswers"])
        if randomWrongAnswer not in answerList:
            answerList.append(randomWrongAnswer)
    app.question = answerList[1]
    randomAnswerList=answerList[2:]
    random.shuffle(randomAnswerList)
    loadLectureButtons(app, randomAnswerList) #loads class button instances
    return answerList #4 random choices

def pickAnswer(app, answer):
    if app.lecturePassed==None:
    #this checks to see if the answer chosen was correct and returns true or false
        if answer == app.currentCorrectAnswer:
            app.lecturePassed = True
        else: app.lecturePassed = False
        app.lectureGameOver = True

def loadLectureQuestions(app):
#comments in this dictionary indicate the person I got the question from
    questions = {
    "Geography": 
                {
                 "correctAnswer":"Ankara",
                 "incorrectAnswers": ["Istanbul","Constantinople","Bursa","Lebanon","Georgia","Turkey"],
                 "question":["What is the capital of Turkey?"]
                 },
    "RGB":
            {
             "correctAnswer":"yellow",
             "incorrectAnswers": ["green","purple","brown","red","orange"],
             "question":["Which of these colors is closest to", "this rgb value: 237, 246, 49"]
             },
    "iphone!": #Kenechukwu Echezona
            {
             "correctAnswer":"2007",
             "incorrectAnswers": ["2005","1999","1776","2009","2010","1997"],
             "question":["What year did the first IPhone launch?"]
             },
    "coasters": #Justin Peng
            {
             "correctAnswer":"The steel coaster",
             "incorrectAnswers": ["Loop-de-loops", "Brakes", "Upstop wheels", "Rollercoasters"],
             "question":["What major rollercoaster innovation", "was developed at Disneyland in 1959?"]
             },
    "Canada": #Chieri Nnadozie
            {
             "correctAnswer":"3%",
             "incorrectAnswers": ["60%","12%","8%","420%","50%","34%","1%","0%"],
             "question":["Quebec holds what percentage of the", "world's freshwater sources?"]
             },
    "pizza":
            {
             "correctAnswer":"Dominos",
             "incorrectAnswers": ["Papa John's","Pizza Hut","Little Ceasers","California Pizza Kitchen"],
             "question":["(734) 930 3030 is the number", "for which pizza establishment?"]
             },
    }
    return questions

#######################
###   LA PRIMA!!!   ###
#######################

#got draw board from cs academy, animation with 2d lists
def drawBoard(app):
    for row in range(app.rows):
        for col in range(app.cols):
            drawCell(app, row, col)

#got draw cell originally from cs academy, but I heavily modified it
def drawCell(app, row, col):
    cellLeft, cellTop = getCellLeftTop(app, row, col)
    cellWidth, cellHeight = getCellSize(app)
    if (row,col) in [(13,12),(12,12),(11,12),(13,13),(12,13),(11,13)]:
        app.board[row][col]="lightsteelblue"
    if (row, col) in app.constantObjects:
        app.board[row][col] = "grey"
    if (row,col) == app.occupied:
        app.board[row][col] = "green"
    if (row,col) in app.randomObjects:
        drawImage(app.chair, cellLeft, cellTop)
    drawRect(cellLeft, cellTop, cellWidth, cellHeight, fill=app.board[row][col], border="black", borderWidth=1)
    if (row,col) == app.coffee[0] and app.coffee[2]==False:
        drawImage(app.coffee[1], cellLeft, cellTop)

#got get cell left top from cs academy animation with 2d lists
def getCellLeftTop(app, row, col):
    cellWidth, cellHeight = getCellSize(app)
    cellLeft = app.boardLeft + col * cellWidth
    cellTop = app.boardTop + row * cellHeight
    return (cellLeft, cellTop)

#got get cell size from cs acedmy animation with 2d lists
def getCellSize(app):
    cellWidth = app.boardWidth / app.cols
    cellHeight = app.boardHeight / app.rows
    return (cellWidth, cellHeight)

#got move person from cs academy but I heavily modified it
def movePerson(app, drow, dcol):
    selectedRow, selectedCol = app.occupied
    newRow = (selectedRow + drow) 
    newCol = (selectedCol + dcol)
    if (newRow,newCol) in app.constantObjects or\
        (newRow,newCol) in app.randomObjects or\
        newRow<0 or newRow>13 or newCol<0 or newCol>13:
        newRow,newCol = app.occupied
    app.occupied = (newRow, newCol)
    app.board[selectedRow][selectedCol] = None

# check board after each piece is placed and if a piece breaks the map, remove it <-- amalia's solid advice
def makeRandomObjects(app):
    app.randomObjects=[]
    for i in range(70):
        app.randomObjects.append((random.randint(2,13),random.randint(0,11)))
        if checkPrimaBoard(app,12,12) == None:
            app.randomObjects.pop()

#referenced cs academy backtracking examples while writing checkPrimaBoard, also lecture notes and also amalia helped debug it a little
def checkPrimaBoard(app, startX, startY):
    board = copy.deepcopy(app.board)
    return checkPrimaBoardHelper(app, startX, startY, board)

def checkPrimaBoardHelper(app, startX, startY, board):
    if (startX, startY) == app.goal:
        return True
    if board[startX][startY] == "0":
        return None
    board[startX][startY] = "0"
    for move in [(0,-1),(-1,0),(1,0),(0,1)]:
        newX = startX+move[0]
        newY = startY+move[1]
        if legalPrimaMove(app, newX, newY, board):
            solution = checkPrimaBoardHelper(app, newX, newY, board)
            if solution ==True:
                return True  
    return None   

def legalPrimaMove(app, newRow, newCol, board):
    if ((newRow,newCol) in app.randomObjects) or ((newRow,newCol) in app.constantObjects)\
    or (newRow<2) or (newRow>13) or (newCol<0) or (newCol>13):
        return False
    return True

def main():
    runApp()

main()





