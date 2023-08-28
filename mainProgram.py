### Modules ###

from tkinter import *
from tkinter import ttk,messagebox
import time
from classes import Yahtzee,Record



### Shortcuts ###

def background():
    label=Label(root,bg='green')
    label.place(x=0,y=0,width=2000,height=800)
    fullTime=StringVar()
    fullTime.set(time.asctime())
    fullTimeLabel=Label(root,textvariable=fullTime,fg='white',bg='green',font=('Tempus Sans ITC',10,'bold'))
    fullTimeLabel.place(x=25,y=625,width=200,height=40)
def buttons():
    quitGameButton=Button(root,text='Quit Game',font=('Tempus Sans ITC',13,'bold'),command=quitGame,relief=GROOVE)
    quitGameButton.place(x=620,y=610,width=150,height=40)
    quitButton=Button(root,text='Quit',font=('Tempus Sans ITC',13,'bold'),command=Quit,relief=GROOVE)
    quitButton.place(x=800,y=610,width=150,height=40)
def beforeThrowDieLabels():
    dieOneImageLabel=Label(root,image=dieOneImage)
    dieOneImageLabel.place(x=100,y=275)
    dieTwoImageLabel=Label(root,image=dieTwoImage)
    dieTwoImageLabel.place(x=150,y=275)
    dieThreeImageLabel=Label(root,image=dieThreeImage)
    dieThreeImageLabel.place(x=200,y=275)
    dieFourImageLabel=Label(root,image=dieFourImage)
    dieFourImageLabel.place(x=250,y=275)
    dieFiveImageLabel=Label(root,image=dieFiveImage)
    dieFiveImageLabel.place(x=300,y=275)
def scorecard():
    global player1Name,player2Name,p1Ones,p2Ones,p1Twos,p2Twos,p1Threes,p2Threes,p1Fours,p2Fours,p1Fives,p2Fives,p1Sixes,p2Sixes,p1Sum,p2Sum,p1Bonus,p2Bonus,p1ThreeOfAKind,p2ThreeOfAKind,p1FourOfAKind,p2FourOfAKind,p1FullHouse,p2FullHouse,p1SmallStraight,p2SmallStraight,p1LargeStraight,p2LargeStraight,p1Chance,p2Chance,p1Yahtzee,p2Yahtzee,p1TotalScore,p2TotalScore
    
    player1Name.set(play.p1Name)    
    player2Name.set(play.p2Name)
    if(play.scoreList[0][0]=='x'):
        p1Ones.set(' ')
    else:
        p1Ones.set(play.scoreList[0][0])
    if(play.scoreList[0][1]=='x'):
        p2Ones.set(' ')
    else:
        p2Ones.set(play.scoreList[0][1])
    if(play.scoreList[1][0]=='x'):
        p1Twos.set(' ')
    else:
        p1Twos.set(play.scoreList[1][0])
    if(play.scoreList[1][1]=='x'):
        p2Twos.set(' ')
    else:
        p2Twos.set(play.scoreList[1][1])
    if(play.scoreList[2][0]=='x'):
        p1Threes.set(' ')
    else:
        p1Threes.set(play.scoreList[2][0])
    if(play.scoreList[2][1]=='x'):
        p2Threes.set(' ')
    else:
        p2Threes.set(play.scoreList[2][1])
    if(play.scoreList[3][0]=='x'):
        p1Fours.set(' ')
    else:
        p1Fours.set(play.scoreList[3][0])
    if(play.scoreList[3][1]=='x'):
        p2Fours.set(' ')
    else:
        p2Fours.set(play.scoreList[3][1])
    if(play.scoreList[4][0]=='x'):
        p1Fives.set(' ')
    else:
        p1Fives.set(play.scoreList[4][0])
    if(play.scoreList[4][1]=='x'):
        p2Fives.set(' ')
    else:
        p2Fives.set(play.scoreList[4][1])
    if(play.scoreList[5][0]=='x'):
        p1Sixes.set(' ')
    else:
        p1Sixes.set(play.scoreList[5][0])
    if(play.scoreList[5][1]=='x'):
        p2Sixes.set(' ')
    else:
        p2Sixes.set(play.scoreList[5][1])
    if(play.scoreList[6][0]=='x'):
        p1Sum.set(' ')
    else:
        p1Sum.set(play.scoreList[6][0])
    if(play.scoreList[6][1]=='x'):
        p2Sum.set(' ')
    else:
        p2Sum.set(play.scoreList[6][1])
    if(play.scoreList[7][0]=='x'):
        p1Bonus.set(' ')
    else:
        p1Bonus.set(play.scoreList[7][0])
    if(play.scoreList[7][1]=='x'):
        p2Bonus.set(' ')
    else:
        p2Bonus.set(play.scoreList[7][1])
    if(play.scoreList[8][0]=='x'):
        p1ThreeOfAKind.set(' ')
    else:
        p1ThreeOfAKind.set(play.scoreList[8][0])
    if(play.scoreList[8][1]=='x'):
        p2ThreeOfAKind.set(' ')
    else:
        p2ThreeOfAKind.set(play.scoreList[8][1])
    if(play.scoreList[9][0]=='x'):
        p1FourOfAKind.set(' ')
    else:
        p1FourOfAKind.set(play.scoreList[9][0])
    if(play.scoreList[9][1]=='x'):
        p2FourOfAKind.set(' ')
    else:
        p2FourOfAKind.set(play.scoreList[9][1])
    if(play.scoreList[10][0]=='x'):
        p1FullHouse.set(' ')
    else:
        p1FullHouse.set(play.scoreList[10][0])
    if(play.scoreList[10][1]=='x'):
        p2FullHouse.set(' ')
    else:
        p2FullHouse.set(play.scoreList[10][1])
    if(play.scoreList[11][0]=='x'):
        p1SmallStraight.set(' ')
    else:
        p1SmallStraight.set(play.scoreList[11][0])
    if(play.scoreList[11][1]=='x'):
        p2SmallStraight.set(' ')
    else:
        p2SmallStraight.set(play.scoreList[11][1])
    if(play.scoreList[12][0]=='x'):
        p1LargeStraight.set(' ')
    else:
        p1LargeStraight.set(play.scoreList[12][0])
    if(play.scoreList[12][1]=='x'):
        p2LargeStraight.set(' ')
    else:
        p2LargeStraight.set(play.scoreList[12][1])
    if(play.scoreList[13][0]=='x'):
        p1Chance.set(' ')
    else:
        p1Chance.set(play.scoreList[13][0])
    if(play.scoreList[13][1]=='x'):
        p2Chance.set(' ')
    else:
        p2Chance.set(play.scoreList[13][1])
    if(play.scoreList[14][0]=='x'):
        p1Yahtzee.set(' ')
    else:
        p1Yahtzee.set(play.scoreList[14][0])
    if(play.scoreList[14][1]=='x'):
        p2Yahtzee.set(' ')
    else:
        p2Yahtzee.set(play.scoreList[14][1])
    if(play.scoreList[15][0]=='x'):
        p1TotalScore.set(' ')
    else:
        p1TotalScore.set(play.scoreList[15][0])
    if(play.scoreList[15][1]=='x'):
        p2TotalScore.set(' ')
    else:
        p2TotalScore.set(play.scoreList[15][1])   

    ### Score Types ###
    blankLabel=Label(root,bg='white',relief=GROOVE)
    blankLabel.place(x=450,y=50,width=200,height=40)
    onesLabel=Label(root,text='Ones',fg='black',bg='white',font=('Tempus Sans ITC',12,'bold'),relief=GROOVE)
    onesLabel.place(x=450,y=90,width=200,height=30)
    TwosLabel=Label(root,text='Twos',fg='black',bg='white',font=('Tempus Sans ITC',12,'bold'),relief=GROOVE)
    TwosLabel.place(x=450,y=120,width=200,height=30)
    ThreesLabel=Label(root,text='Threes',fg='black',bg='white',font=('Tempus Sans ITC',12,'bold'),relief=GROOVE)
    ThreesLabel.place(x=450,y=150,width=200,height=30)
    foursLabel=Label(root,text='Fours',fg='black',bg='white',font=('Tempus Sans ITC',12,'bold'),relief=GROOVE)
    foursLabel.place(x=450,y=180,width=200,height=30)
    fivesLabel=Label(root,text='Fives',fg='black',bg='white',font=('Tempus Sans ITC',12,'bold'),relief=GROOVE)
    fivesLabel.place(x=450,y=210,width=200,height=30)
    sixesLabel=Label(root,text='Sixes',fg='black',bg='white',font=('Tempus Sans ITC',12,'bold'),relief=GROOVE)
    sixesLabel.place(x=450,y=240,width=200,height=30)
    sumLabel=Label(root,text='Sum',fg='black',bg='white',font=('Tempus Sans ITC',12,'bold'),relief=GROOVE)
    sumLabel.place(x=450,y=270,width=200,height=30)
    bonusLabel=Label(root,text='Bonus',fg='black',bg='white',font=('Tempus Sans ITC',12,'bold'),relief=GROOVE)
    bonusLabel.place(x=450,y=300,width=200,height=30)
    threeOfAKindLabel=Label(root,text='Three of a Kind',fg='black',bg='white',font=('Tempus Sans ITC',12,'bold'),relief=GROOVE)
    threeOfAKindLabel.place(x=450,y=330,width=200,height=30)
    fourOFAKindLabel=Label(root,text='Four of a Kind',fg='black',bg='white',font=('Tempus Sans ITC',12,'bold'),relief=GROOVE)
    fourOFAKindLabel.place(x=450,y=360,width=200,height=30)
    fullHouseLabel=Label(root,text='Full House',fg='black',bg='white',font=('Tempus Sans ITC',12,'bold'),relief=GROOVE)
    fullHouseLabel.place(x=450,y=390,width=200,height=30)
    smallStraightLabel=Label(root,text='Small Straight',fg='black',bg='white',font=('Tempus Sans ITC',12,'bold'),relief=GROOVE)
    smallStraightLabel.place(x=450,y=420,width=200,height=30)
    largeStraightLabel=Label(root,text='Large Straight',fg='black',bg='white',font=('Tempus Sans ITC',12,'bold'),relief=GROOVE)
    largeStraightLabel.place(x=450,y=450,width=200,height=30)
    chanceLabel=Label(root,text='Chance',fg='black',bg='white',font=('Tempus Sans ITC',12,'bold'),relief=GROOVE)
    chanceLabel.place(x=450,y=480,width=200,height=30)
    yahtzeeLabel=Label(root,text='YAHTZEE',fg='black',bg='white',font=('Tempus Sans ITC',12,'bold'),relief=GROOVE)
    yahtzeeLabel.place(x=450,y=510,width=200,height=30)
    totalScoreLabel=Label(root,text='Total Score',fg='black',bg='white',font=('Tempus Sans ITC',12,'bold'),relief=GROOVE)
    totalScoreLabel.place(x=450,y=540,width=200,height=30)

    ### Player 1 Scores ###
    p1Label=Label(root,textvariable=player1Name,fg='black',bg='white',font=('Tempus Sans ITC',12,'bold'),relief=GROOVE)
    p1Label.place(x=650,y=50,width=150,height=40)
    p1OnesLabel=Label(root,textvariable=p1Ones,fg='black',bg='white',font=('Tempus Sans ITC',12),relief=GROOVE)
    p1OnesLabel.place(x=650,y=90,width=150,height=30)
    p1TwosLabel=Label(root,textvariable=p1Twos,fg='black',bg='white',font=('Tempus Sans ITC',12),relief=GROOVE)
    p1TwosLabel.place(x=650,y=120,width=150,height=30)
    p1ThreesLabel=Label(root,textvariable=p1Threes,fg='black',bg='white',font=('Tempus Sans ITC',12),relief=GROOVE)
    p1ThreesLabel.place(x=650,y=150,width=150,height=30)
    p1FoursLabel=Label(root,textvariable=p1Fours,fg='black',bg='white',font=('Tempus Sans ITC',12),relief=GROOVE)
    p1FoursLabel.place(x=650,y=180,width=150,height=30)
    p1FivesLabel=Label(root,textvariable=p1Fives,fg='black',bg='white',font=('Tempus Sans ITC',12),relief=GROOVE)
    p1FivesLabel.place(x=650,y=210,width=150,height=30)
    p1SixesLabel=Label(root,textvariable=p1Sixes,fg='black',bg='white',font=('Tempus Sans ITC',12),relief=GROOVE)
    p1SixesLabel.place(x=650,y=240,width=150,height=30)
    p1SumLabel=Label(root,textvariable=p1Sum,fg='black',bg='white',font=('Tempus Sans ITC',12,'bold'),relief=GROOVE)
    p1SumLabel.place(x=650,y=270,width=150,height=30)
    p1BonusLabel=Label(root,textvariable=p1Bonus,fg='black',bg='white',font=('Tempus Sans ITC',12,'bold'),relief=GROOVE)
    p1BonusLabel.place(x=650,y=300,width=150,height=30)
    p1ThreeOfAKindLabel=Label(root,textvariable=p1ThreeOfAKind,fg='black',bg='white',font=('Tempus Sans ITC',12),relief=GROOVE)
    p1ThreeOfAKindLabel.place(x=650,y=330,width=150,height=30)
    p1FourOfAKindLabel=Label(root,textvariable=p1FourOfAKind,fg='black',bg='white',font=('Tempus Sans ITC',12),relief=GROOVE)
    p1FourOfAKindLabel.place(x=650,y=360,width=150,height=30)
    p1FullHouseLabel=Label(root,textvariable=p1FullHouse,fg='black',bg='white',font=('Tempus Sans ITC',12),relief=GROOVE)
    p1FullHouseLabel.place(x=650,y=390,width=150,height=30)
    p1SmallStraightLabel=Label(root,textvariable=p1SmallStraight,fg='black',bg='white',font=('Tempus Sans ITC',12),relief=GROOVE)
    p1SmallStraightLabel.place(x=650,y=420,width=150,height=30)
    p1LargeStraightLabel=Label(root,textvariable=p1LargeStraight,fg='black',bg='white',font=('Tempus Sans ITC',12),relief=GROOVE)
    p1LargeStraightLabel.place(x=650,y=450,width=150,height=30)
    p1ChanceLabel=Label(root,textvariable=p1Chance,fg='black',bg='white',font=('Tempus Sans ITC',12),relief=GROOVE)
    p1ChanceLabel.place(x=650,y=480,width=150,height=30)
    p1YahtzeeLabel=Label(root,textvariable=p1Yahtzee,fg='black',bg='white',font=('Tempus Sans ITC',12),relief=GROOVE)
    p1YahtzeeLabel.place(x=650,y=510,width=150,height=30)
    p1TotalScoreLabel=Label(root,textvariable=p1TotalScore,fg='black',bg='white',font=('Tempus Sans ITC',12,'bold'),relief=GROOVE)
    p1TotalScoreLabel.place(x=650,y=540,width=150,height=30)
    
    ### Player 2 Score ###
    p2Label=Label(root,textvariable=player2Name,fg='black',bg='white',font=('Tempus Sans ITC',12,'bold'),relief=GROOVE)
    p2Label.place(x=800,y=50,width=150,height=40)
    p2OnesLabel=Label(root,textvariable=p2Ones,fg='black',bg='white',font=('Tempus Sans ITC',12),relief=GROOVE)
    p2OnesLabel.place(x=800,y=90,width=150,height=30)
    p2TwosLabel=Label(root,textvariable=p2Twos,fg='black',bg='white',font=('Tempus Sans ITC',12),relief=GROOVE)
    p2TwosLabel.place(x=800,y=120,width=150,height=30)
    p2ThreesLabel=Label(root,textvariable=p2Threes,fg='black',bg='white',font=('Tempus Sans ITC',12),relief=GROOVE)
    p2ThreesLabel.place(x=800,y=150,width=150,height=30)
    p2FoursLabel=Label(root,textvariable=p2Fours,fg='black',bg='white',font=('Tempus Sans ITC',12),relief=GROOVE)
    p2FoursLabel.place(x=800,y=180,width=150,height=30)
    p2FivesLabel=Label(root,textvariable=p2Fives,fg='black',bg='white',font=('Tempus Sans ITC',12),relief=GROOVE)
    p2FivesLabel.place(x=800,y=210,width=150,height=30)
    p2SixesLabel=Label(root,textvariable=p2Sixes,fg='black',bg='white',font=('Tempus Sans ITC',12),relief=GROOVE)
    p2SixesLabel.place(x=800,y=240,width=150,height=30)
    p2SumLabel=Label(root,textvariable=p2Sum,fg='black',bg='white',font=('Tempus Sans ITC',12,'bold'),relief=GROOVE)
    p2SumLabel.place(x=800,y=270,width=150,height=30)
    p2BonusLabel=Label(root,textvariable=p2Bonus,fg='black',bg='white',font=('Tempus Sans ITC',12,'bold'),relief=GROOVE)
    p2BonusLabel.place(x=800,y=300,width=150,height=30)
    p2ThreeOfAKindLabel=Label(root,textvariable=p2ThreeOfAKind,fg='black',bg='white',font=('Tempus Sans ITC',12),relief=GROOVE)
    p2ThreeOfAKindLabel.place(x=800,y=330,width=150,height=30)
    p2FourOfAKindLabel=Label(root,textvariable=p2FourOfAKind,fg='black',bg='white',font=('Tempus Sans ITC',12),relief=GROOVE)
    p2FourOfAKindLabel.place(x=800,y=360,width=150,height=30)
    p2FullHouseLabel=Label(root,textvariable=p2FullHouse,fg='black',bg='white',font=('Tempus Sans ITC',12),relief=GROOVE)
    p2FullHouseLabel.place(x=800,y=390,width=150,height=30)
    p2SmallStraightLabel=Label(root,textvariable=p2SmallStraight,fg='black',bg='white',font=('Tempus Sans ITC',12),relief=GROOVE)
    p2SmallStraightLabel.place(x=800,y=420,width=150,height=30)
    p2LargeStraightLabel=Label(root,textvariable=p2LargeStraight,fg='black',bg='white',font=('Tempus Sans ITC',12),relief=GROOVE)
    p2LargeStraightLabel.place(x=800,y=450,width=150,height=30)
    p2ChanceLabel=Label(root,textvariable=p2Chance,fg='black',bg='white',font=('Tempus Sans ITC',12),relief=GROOVE)
    p2ChanceLabel.place(x=800,y=480,width=150,height=30)
    p2YahtzeeLabel=Label(root,textvariable=p2Yahtzee,fg='black',bg='white',font=('Tempus Sans ITC',12),relief=GROOVE)
    p2YahtzeeLabel.place(x=800,y=510,width=150,height=30)
    p2TotalScoreLabel=Label(root,textvariable=p2TotalScore,fg='black',bg='white',font=('Tempus Sans ITC',12,'bold'),relief=GROOVE)
    p2TotalScoreLabel.place(x=800,y=540,width=150,height=30)
def player1Score():    # Detects type of score(s) of Player 1
    global play,throw,keptNumbers,p1Ones,p1Twos,p1Threes,p1Fours,p1Fives,p1Sixes,p1ThreeOfAKind,p1FourOfAKind,p1FullHouse,p1SmallStraight,p1LargeStraight,p1Chance,p1Yahtzee
    
    p1ScoreAlready='no'
    if((keptNumbers.count(1)>=1 or throw.count(1)>=1) and play.scoreList[0][0]=='x'):
        p1Ones.set(keptNumbers.count(1)+throw.count(1))
        p1OnesButton=Button(root,textvariable=p1Ones,fg='black',bg='cyan',font=('Tempus Sans ITC',12),command=p1OnesClick,relief=GROOVE)
        p1OnesButton.place(x=650,y=90,width=150,height=30)
        p1ScoreAlready='yes'
    if((keptNumbers.count(2)>=1 or throw.count(2)>=1) and play.scoreList[1][0]=='x'):
        p1Twos.set((keptNumbers.count(2)+throw.count(2))*2)
        p1TwosButton=Button(root,textvariable=p1Twos,fg='black',bg='cyan',font=('Tempus Sans ITC',12),command=p1TwosClick,relief=GROOVE)
        p1TwosButton.place(x=650,y=120,width=150,height=30)
        p1ScoreAlready='yes'
    if((keptNumbers.count(3)>=1 or throw.count(3)>=1) and play.scoreList[2][0]=='x'):
        p1Threes.set((keptNumbers.count(3)+throw.count(3))*3)
        p1ThreesButton=Button(root,textvariable=p1Threes,fg='black',bg='cyan',font=('Tempus Sans ITC',12),command=p1ThreesClick,relief=GROOVE)
        p1ThreesButton.place(x=650,y=150,width=150,height=30)
        p1ScoreAlready='yes'
    if((keptNumbers.count(4)>=1 or throw.count(4)>=1) and play.scoreList[3][0]=='x'):
        p1Fours.set((keptNumbers.count(4)+throw.count(4))*4)
        p1FoursButton=Button(root,textvariable=p1Fours,fg='black',bg='cyan',font=('Tempus Sans ITC',12),command=p1FoursClick,relief=GROOVE)
        p1FoursButton.place(x=650,y=180,width=150,height=30)
        p1ScoreAlready='yes'
    if((keptNumbers.count(5)>=1 or throw.count(5)>=1) and play.scoreList[4][0]=='x'):
        p1Fives.set((keptNumbers.count(5)+throw.count(5))*5)
        p1FivesButton=Button(root,textvariable=p1Fives,fg='black',bg='cyan',font=('Tempus Sans ITC',12),command=p1FivesClick,relief=GROOVE)
        p1FivesButton.place(x=650,y=210,width=150,height=30)
        p1ScoreAlready='yes'
    if((keptNumbers.count(6)>=1 or throw.count(6)>=1) and play.scoreList[5][0]=='x'):
        p1Sixes.set((keptNumbers.count(6)+throw.count(6))*6)
        p1SixesButton=Button(root,textvariable=p1Sixes,fg='black',bg='cyan',font=('Tempus Sans ITC',12),command=p1SixesClick,relief=GROOVE)
        p1SixesButton.place(x=650,y=240,width=150,height=30)
        p1ScoreAlready='yes'
    if(play.ofKind(keptNumbers)=='threeOfAKind' and play.scoreList[8][0]=='x'):
        p1ThreeOfAKind.set(sum(keptNumbers)+sum(throw))
        p1ThreeOfAKindButton=Button(root,textvariable=p1ThreeOfAKind,fg='black',bg='cyan',font=('Tempus Sans ITC',12),command=p1ThreeOfAKindClick,relief=GROOVE)
        p1ThreeOfAKindButton.place(x=650,y=330,width=150,height=30)
        p1ScoreAlready='yes'
    if(play.ofKind(keptNumbers)=='fourOfAKind' and play.scoreList[9][0]=='x'):
        p1FourOfAKind.set(sum(keptNumbers)+sum(throw))
        p1FourOfAKindButton=Button(root,textvariable=p1FourOfAKind,fg='black',bg='cyan',font=('Tempus Sans ITC',12),command=p1FourOfAKindClick,relief=GROOVE)
        p1FourOfAKindButton.place(x=650,y=360,width=150,height=30)
        p1ScoreAlready='yes'
    if(play.ofKind(keptNumbers)=='fullHouse'):
        if(play.scoreList[8][0]=='x'):
            p1ThreeOfAKind.set(sum(keptNumbers)+sum(throw))
            p1ThreeOfAKindButton=Button(root,textvariable=p1ThreeOfAKind,fg='black',bg='cyan',font=('Tempus Sans ITC',12),command=p1ThreeOfAKindClick,relief=GROOVE)
            p1ThreeOfAKindButton.place(x=650,y=330,width=150,height=30)
            p1ScoreAlready='yes'
        if(play.scoreList[10][0]=='x'):
            p1FullHouse.set(25)
            p1FullHouseButton=Button(root,textvariable=p1FullHouse,fg='black',bg='cyan',font=('Tempus Sans ITC',12),command=p1FullHouseClick,relief=GROOVE)
            p1FullHouseButton.place(x=650,y=390,width=150,height=30)
            p1ScoreAlready='yes'
    if(play.smallStraight(keptNumbers) and play.scoreList[11][0]=='x'):
        p1SmallStraight.set(30)
        p1SmallStraightButton=Button(root,textvariable=p1SmallStraight,fg='black',bg='cyan',font=('Tempus Sans ITC',12),command=p1SmallStraightClick,relief=GROOVE)
        p1SmallStraightButton.place(x=650,y=420,width=150,height=30)
        p1ScoreAlready='yes'
    if(play.largeStraight(keptNumbers) and play.scoreList[12][0]=='x'):
        if(play.scoreList[11][0]=='x'):
            p1SmallStraight.set(30)
            p1SmallStraightButton=Button(root,textvariable=p1SmallStraight,fg='black',bg='cyan',font=('Tempus Sans ITC',12),command=p1SmallStraightClick,relief=GROOVE)
            p1SmallStraightButton.place(x=650,y=420,width=150,height=30)
        p1LargeStraight.set(40)
        p1LargeStraightButton=Button(root,textvariable=p1LargeStraight,fg='black',bg='cyan',font=('Tempus Sans ITC',12),command=p1LargeStraightClick,relief=GROOVE)
        p1LargeStraightButton.place(x=650,y=450,width=150,height=30)
        p1ScoreAlready='yes'
    if(play.scoreList[13][0]=='x'):
        p1Chance.set(sum(keptNumbers)+sum(throw))
        p1ChanceButton=Button(root,textvariable=p1Chance,fg='black',bg='cyan',font=('Tempus Sans ITC',12),command=p1ChanceClick,relief=GROOVE)
        p1ChanceButton.place(x=650,y=480,width=150,height=30)
        p1ScoreAlready='yes'
    if(play.ofKind(keptNumbers)=='yahtzee' and play.scoreList[14][0]=='x'):
        p1Yahtzee.set(50)
        p1YahtzeeButton=Button(root,textvariable=p1Yahtzee,fg='black',bg='cyan',font=('Tempus Sans ITC',12),command=p1YahtzeeClick,relief=GROOVE)
        p1YahtzeeButton.place(x=650,y=510,width=150,height=30)
        p1ScoreAlready='yes'

    if(len(keptNumbers)==5 and p1ScoreAlready=='no' and (play.ofKind(keptNumbers)!='threeOfAKind' and play.ofKind(keptNumbers)!='fourOfAKind' and play.ofKind(keptNumbers)!='fullHouse' and play.smallStraight(keptNumbers)!=True and play.largeStraight(keptNumbers)!=True and play.ofKind(keptNumbers)!='yahtzee')):
        if((keptNumbers.count(1)==0 and throw.count(1)==0) and play.scoreList[0][0]=='x'):
            p1Ones.set(0)
            p1OnesButton=Button(root,textvariable=p1Ones,fg='black',bg='cyan',font=('Tempus Sans ITC',12),command=p1OnesClick,relief=GROOVE)
            p1OnesButton.place(x=650,y=90,width=150,height=30)
        if((keptNumbers.count(2)==0 and throw.count(2)==0) and play.scoreList[1][0]=='x'):
            p1Twos.set(0)
            p1TwosButton=Button(root,textvariable=p1Twos,fg='black',bg='cyan',font=('Tempus Sans ITC',12),command=p1TwosClick,relief=GROOVE)
            p1TwosButton.place(x=650,y=120,width=150,height=30)
        if((keptNumbers.count(3)==0 and throw.count(3)==0) and play.scoreList[2][0]=='x'):
            p1Threes.set(0)
            p1ThreesButton=Button(root,textvariable=p1Threes,fg='black',bg='cyan',font=('Tempus Sans ITC',12),command=p1ThreesClick,relief=GROOVE)
            p1ThreesButton.place(x=650,y=150,width=150,height=30)
        if((keptNumbers.count(4)==0 and throw.count(4)==0) and play.scoreList[3][0]=='x'):
            p1Fours.set(0)
            p1FoursButton=Button(root,textvariable=p1Fours,fg='black',bg='cyan',font=('Tempus Sans ITC',12),command=p1FoursClick,relief=GROOVE)
            p1FoursButton.place(x=650,y=180,width=150,height=30)
        if((keptNumbers.count(5)==0 and throw.count(5)==0) and play.scoreList[4][0]=='x'):
            p1Fives.set(0)
            p1FivesButton=Button(root,textvariable=p1Fives,fg='black',bg='cyan',font=('Tempus Sans ITC',12),command=p1FivesClick,relief=GROOVE)
            p1FivesButton.place(x=650,y=210,width=150,height=30)
        if((keptNumbers.count(6)==0 and throw.count(6)==0) and play.scoreList[5][0]=='x'):
            p1Sixes.set(0)
            p1SixesButton=Button(root,textvariable=p1Sixes,fg='black',bg='cyan',font=('Tempus Sans ITC',12),command=p1SixesClick,relief=GROOVE)
            p1SixesButton.place(x=650,y=240,width=150,height=30)
        if(play.scoreList[8][0]=='x'):
            p1ThreeOfAKind.set(0)
            p1ThreeOfAKindButton=Button(root,textvariable=p1ThreeOfAKind,fg='black',bg='cyan',font=('Tempus Sans ITC',12),command=p1ThreeOfAKindClick,relief=GROOVE)
            p1ThreeOfAKindButton.place(x=650,y=330,width=150,height=30)
        if(play.scoreList[9][0]=='x'):
            p1FourOfAKind.set(0)
            p1FourOfAKindButton=Button(root,textvariable=p1FourOfAKind,fg='black',bg='cyan',font=('Tempus Sans ITC',12),command=p1FourOfAKindClick,relief=GROOVE)
            p1FourOfAKindButton.place(x=650,y=360,width=150,height=30)
        if(play.scoreList[10][0]=='x'):
            p1FullHouse.set(0)
            p1FullHouseButton=Button(root,textvariable=p1FullHouse,fg='black',bg='cyan',font=('Tempus Sans ITC',12),command=p1FullHouseClick,relief=GROOVE)
            p1FullHouseButton.place(x=650,y=390,width=150,height=30)
        if(play.scoreList[11][0]=='x'):
            p1SmallStraight.set(0)
            p1SmallStraightButton=Button(root,textvariable=p1SmallStraight,fg='black',bg='cyan',font=('Tempus Sans ITC',12),command=p1SmallStraightClick,relief=GROOVE)
            p1SmallStraightButton.place(x=650,y=420,width=150,height=30)
        if(play.scoreList[12][0]=='x'):
            p1LargeStraight.set(0)
            p1LargeStraightButton=Button(root,textvariable=p1LargeStraight,fg='black',bg='cyan',font=('Tempus Sans ITC',12),command=p1LargeStraightClick,relief=GROOVE)
            p1LargeStraightButton.place(x=650,y=450,width=150,height=30)
        if(play.scoreList[14][0]=='x'):
            p1Yahtzee.set(0)
            p1YahtzeeButton=Button(root,textvariable=p1Yahtzee,fg='black',bg='cyan',font=('Tempus Sans ITC',12),command=p1YahtzeeClick,relief=GROOVE)
            p1YahtzeeButton.place(x=650,y=510,width=150,height=30)
        p1ScoreAlready='yes'

    if(len(keptNumbers)==5 and p1ScoreAlready=='no' and (play.ofKind(keptNumbers)=='threeOfAKind' or play.ofKind(keptNumbers)=='fourOfAKind' or play.ofKind(keptNumbers)=='fullHouse' or play.smallStraight(keptNumbers) or play.largeStraight(keptNumbers) or play.ofKind(keptNumbers)=='yahtzee')):
        if((keptNumbers.count(1)==0 and throw.count(1)==0) and play.scoreList[0][0]=='x'):
            p1Ones.set(0)
            p1OnesButton=Button(root,textvariable=p1Ones,fg='black',bg='cyan',font=('Tempus Sans ITC',12),command=p1OnesClick,relief=GROOVE)
            p1OnesButton.place(x=650,y=90,width=150,height=30)
        if((keptNumbers.count(2)==0 and throw.count(2)==0) and play.scoreList[1][0]=='x'):
            p1Twos.set(0)
            p1TwosButton=Button(root,textvariable=p1Twos,fg='black',bg='cyan',font=('Tempus Sans ITC',12),command=p1TwosClick,relief=GROOVE)
            p1TwosButton.place(x=650,y=120,width=150,height=30)
        if((keptNumbers.count(3)==0 and throw.count(3)==0) and play.scoreList[2][0]=='x'):
            p1Threes.set(0)
            p1ThreesButton=Button(root,textvariable=p1Threes,fg='black',bg='cyan',font=('Tempus Sans ITC',12),command=p1ThreesClick,relief=GROOVE)
            p1ThreesButton.place(x=650,y=150,width=150,height=30)
        if((keptNumbers.count(4)==0 and throw.count(4)==0) and play.scoreList[3][0]=='x'):
            p1Fours.set(0)
            p1FoursButton=Button(root,textvariable=p1Fours,fg='black',bg='cyan',font=('Tempus Sans ITC',12),command=p1FoursClick,relief=GROOVE)
            p1FoursButton.place(x=650,y=180,width=150,height=30)
        if((keptNumbers.count(5)==0 and throw.count(5)==0) and play.scoreList[4][0]=='x'):
            p1Fives.set(0)
            p1FivesButton=Button(root,textvariable=p1Fives,fg='black',bg='cyan',font=('Tempus Sans ITC',12),command=p1FivesClick,relief=GROOVE)
            p1FivesButton.place(x=650,y=210,width=150,height=30)
        if((keptNumbers.count(6)==0 and throw.count(6)==0) and play.scoreList[5][0]=='x'):
            p1Sixes.set(0)
            p1SixesButton=Button(root,textvariable=p1Sixes,fg='black',bg='cyan',font=('Tempus Sans ITC',12),command=p1SixesClick,relief=GROOVE)
            p1SixesButton.place(x=650,y=240,width=150,height=30)
        if(play.ofKind(keptNumbers)!='threeOfAKind' and play.scoreList[8][0]=='x'):
            p1ThreeOfAKind.set(0)
            p1ThreeOfAKindButton=Button(root,textvariable=p1ThreeOfAKind,fg='black',bg='cyan',font=('Tempus Sans ITC',12),command=p1ThreeOfAKindClick,relief=GROOVE)
            p1ThreeOfAKindButton.place(x=650,y=330,width=150,height=30)
        if(play.ofKind(keptNumbers)!='fourOfAKind' and play.scoreList[9][0]=='x'):
            p1FourOfAKind.set(0)
            p1FourOfAKindButton=Button(root,textvariable=p1FourOfAKind,fg='black',bg='cyan',font=('Tempus Sans ITC',12),command=p1FourOfAKindClick,relief=GROOVE)
            p1FourOfAKindButton.place(x=650,y=360,width=150,height=30)
        if(play.ofKind(keptNumbers)!='fullHouse' and play.scoreList[10][0]=='x'):
            p1FullHouse.set(0)
            p1FullHouseButton=Button(root,textvariable=p1FullHouse,fg='black',bg='cyan',font=('Tempus Sans ITC',12),command=p1FullHouseClick,relief=GROOVE)
            p1FullHouseButton.place(x=650,y=390,width=150,height=30)
        if(play.smallStraight(keptNumbers)!=True and play.scoreList[11][0]=='x'):
            p1SmallStraight.set(0)
            p1SmallStraightButton=Button(root,textvariable=p1SmallStraight,fg='black',bg='cyan',font=('Tempus Sans ITC',12),command=p1SmallStraightClick,relief=GROOVE)
            p1SmallStraightButton.place(x=650,y=420,width=150,height=30)
        if(play.largeStraight(keptNumbers)!=True and play.scoreList[12][0]=='x'):
            p1LargeStraight.set(0)
            p1LargeStraightButton=Button(root,textvariable=p1LargeStraight,fg='black',bg='cyan',font=('Tempus Sans ITC',12),command=p1LargeStraightClick,relief=GROOVE)
            p1LargeStraightButton.place(x=650,y=450,width=150,height=30)
        if(play.ofKind(keptNumbers)!='yahtzee' and play.scoreList[14][0]=='x'):
            p1Yahtzee.set(0)
            p1YahtzeeButton=Button(root,textvariable=p1Yahtzee,fg='black',bg='cyan',font=('Tempus Sans ITC',12),command=p1YahtzeeClick,relief=GROOVE)
            p1YahtzeeButton.place(x=650,y=510,width=150,height=30)
def player2Score():    # Detects type of score(s) of Player 2
    global play,throw,keptNumbers,p2Ones,p2Twos,p2Threes,p2Fours,p2Fives,p2Sixes,p2ThreeOfAKind,p2FourOfAKind,p2FullHouse,p2SmallStraight,p2LargeStraight,p2Chance,p2Yahtzee
    
    p2ScoreAlready='no'
    if((keptNumbers.count(1)>=1 or throw.count(1)>=1) and play.scoreList[0][1]=='x'):
        p2Ones.set(keptNumbers.count(1)+throw.count(1))
        p2OnesButton=Button(root,textvariable=p2Ones,fg='black',bg='cyan',font=('Tempus Sans ITC',12),command=p2OnesClick,relief=GROOVE)
        p2OnesButton.place(x=800,y=90,width=150,height=30)
        p2ScoreAlready='Yes'
    if((keptNumbers.count(2)>=1 or throw.count(2)>=1) and play.scoreList[1][1]=='x'):
        p2Twos.set((keptNumbers.count(2)+throw.count(2))*2)
        p2TwosButton=Button(root,textvariable=p2Twos,fg='black',bg='cyan',font=('Tempus Sans ITC',12),command=p2TwosClick,relief=GROOVE)
        p2TwosButton.place(x=800,y=120,width=150,height=30)
        p2ScoreAlready='Yes'
    if((keptNumbers.count(3)>=1 or throw.count(3)>=1) and play.scoreList[2][1]=='x'):
        p2Threes.set((keptNumbers.count(3)+throw.count(3))*3)
        p2ThreesButton=Button(root,textvariable=p2Threes,fg='black',bg='cyan',font=('Tempus Sans ITC',12),command=p2ThreesClick,relief=GROOVE)
        p2ThreesButton.place(x=800,y=150,width=150,height=30)
        p2ScoreAlready='Yes'
    if((keptNumbers.count(4)>=1 or throw.count(4)>=1) and play.scoreList[3][1]=='x'):
        p2Fours.set((keptNumbers.count(4)+throw.count(4))*4)
        p2FoursButton=Button(root,textvariable=p2Fours,fg='black',bg='cyan',font=('Tempus Sans ITC',12),command=p2FoursClick,relief=GROOVE)
        p2FoursButton.place(x=800,y=180,width=150,height=30)
        p2ScoreAlready='Yes'
    if((keptNumbers.count(5)>=1 or throw.count(5)>=1) and play.scoreList[4][1]=='x'):
        p2Fives.set((keptNumbers.count(5)+throw.count(5))*5)
        p2FivesButton=Button(root,textvariable=p2Fives,fg='black',bg='cyan',font=('Tempus Sans ITC',12),command=p2FivesClick,relief=GROOVE)
        p2FivesButton.place(x=800,y=210,width=150,height=30)
        p2ScoreAlready='Yes'
    if((keptNumbers.count(6)>=1 or throw.count(6)>=1) and play.scoreList[5][1]=='x'):
        p2Sixes.set((keptNumbers.count(6)+throw.count(6))*6)
        p2SixesButton=Button(root,textvariable=p2Sixes,fg='black',bg='cyan',font=('Tempus Sans ITC',12),command=p2SixesClick,relief=GROOVE)
        p2SixesButton.place(x=800,y=240,width=150,height=30)
        p2ScoreAlready='Yes'
    if(play.ofKind(keptNumbers)=='threeOfAKind' and play.scoreList[8][1]=='x'):
        p2ThreeOfAKind.set(sum(keptNumbers)+sum(throw))
        p2ThreeOfAKindButton=Button(root,textvariable=p2ThreeOfAKind,fg='black',bg='cyan',font=('Tempus Sans ITC',12),command=p2ThreeOfAKindClick,relief=GROOVE)
        p2ThreeOfAKindButton.place(x=800,y=330,width=150,height=30)
        p2ScoreAlready='Yes'
    if(play.ofKind(keptNumbers)=='fourOfAKind' and play.scoreList[9][1]=='x'):
        p2FourOfAKind.set(sum(keptNumbers)+sum(throw))
        p2FourOfAKindButton=Button(root,textvariable=p2FourOfAKind,fg='black',bg='cyan',font=('Tempus Sans ITC',12),command=p2FourOfAKindClick,relief=GROOVE)
        p2FourOfAKindButton.place(x=800,y=360,width=150,height=30)
        p2ScoreAlready='Yes'
    if(play.ofKind(keptNumbers)=='fullHouse'):
        if(play.scoreList[8][1]=='x'):
            p2ThreeOfAKind.set(sum(keptNumbers)+sum(throw))
            p2ThreeOfAKindButton=Button(root,textvariable=p2ThreeOfAKind,fg='black',bg='cyan',font=('Tempus Sans ITC',12),command=p2ThreeOfAKindClick,relief=GROOVE)
            p2ThreeOfAKindButton.place(x=800,y=330,width=150,height=30)
            p2ScoreAlready='Yes'
        if(play.scoreList[10][1]=='x'):
            p2FullHouse.set(25)
            p2FullHouseButton=Button(root,textvariable=p2FullHouse,fg='black',bg='cyan',font=('Tempus Sans ITC',12),command=p2FullHouseClick,relief=GROOVE)
            p2FullHouseButton.place(x=800,y=390,width=150,height=30)
            p2ScoreAlready='Yes'
    if(play.smallStraight(keptNumbers) and play.scoreList[11][1]=='x'):
        p2SmallStraight.set(30)
        p2SmallStraightButton=Button(root,textvariable=p2SmallStraight,fg='black',bg='cyan',font=('Tempus Sans ITC',12),command=p2SmallStraightClick,relief=GROOVE)
        p2SmallStraightButton.place(x=800,y=420,width=150,height=30)
        p2ScoreAlready='Yes'
    if(play.largeStraight(keptNumbers) and play.scoreList[12][1]=='x'):
        if(play.scoreList[11][1]=='x'):
            p2SmallStraight.set(30)
            p2SmallStraightButton=Button(root,textvariable=p2SmallStraight,fg='black',bg='cyan',font=('Tempus Sans ITC',12),command=p2SmallStraightClick,relief=GROOVE)
            p2SmallStraightButton.place(x=800,y=420,width=150,height=30)
        p2LargeStraight.set(40)
        p2LargeStraightButton=Button(root,textvariable=p2LargeStraight,fg='black',bg='cyan',font=('Tempus Sans ITC',12),command=p2LargeStraightClick,relief=GROOVE)
        p2LargeStraightButton.place(x=800,y=450,width=150,height=30)
        p2ScoreAlready='Yes'
    if(play.scoreList[13][1]=='x'):
        p2Chance.set(sum(keptNumbers)+sum(throw))
        p2ChanceButton=Button(root,textvariable=p2Chance,fg='black',bg='cyan',font=('Tempus Sans ITC',12),command=p2ChanceClick,relief=GROOVE)
        p2ChanceButton.place(x=800,y=480,width=150,height=30)
        p2ScoreAlready='Yes'
    if(play.ofKind(keptNumbers)=='yahtzee' and play.scoreList[14][1]=='x'):
        p2Yahtzee.set(50)
        p2YahtzeeButton=Button(root,textvariable=p2Yahtzee,fg='black',bg='cyan',font=('Tempus Sans ITC',12),command=p2YahtzeeClick,relief=GROOVE)
        p2YahtzeeButton.place(x=800,y=510,width=150,height=30)
        p2ScoreAlready='Yes'

    if(len(keptNumbers)==5 and p2ScoreAlready=='no' and (play.ofKind(keptNumbers)!='threeOfAKind' and play.ofKind(keptNumbers)!='fourOfAKind' and play.ofKind(keptNumbers)!='fullHouse' and play.smallStraight(keptNumbers)!=True and play.largeStraight(keptNumbers)!=True and play.ofKind(keptNumbers)!='yahtzee')):
        if((keptNumbers.count(1)==0 and throw.count(1)==0) and play.scoreList[0][1]=='x'):
            p2Ones.set(0)
            p2OnesButton=Button(root,textvariable=p2Ones,fg='black',bg='cyan',font=('Tempus Sans ITC',12),command=p2OnesClick,relief=GROOVE)
            p2OnesButton.place(x=800,y=90,width=150,height=30)
        if((keptNumbers.count(2)==0 and throw.count(2)==0) and play.scoreList[1][1]=='x'):
            p2Twos.set(0)
            p2TwosButton=Button(root,textvariable=p2Twos,fg='black',bg='cyan',font=('Tempus Sans ITC',12),command=p2TwosClick,relief=GROOVE)
            p2TwosButton.place(x=800,y=120,width=150,height=30)
        if((keptNumbers.count(3)==0 and throw.count(3)==0) and play.scoreList[2][1]=='x'):
            p2Threes.set(0)
            p2ThreesButton=Button(root,textvariable=p2Threes,fg='black',bg='cyan',font=('Tempus Sans ITC',12),command=p2ThreesClick,relief=GROOVE)
            p2ThreesButton.place(x=800,y=150,width=150,height=30)
        if((keptNumbers.count(4)==0 and throw.count(4)==0) and play.scoreList[3][1]=='x'):
            p2Fours.set(0)
            p2FoursButton=Button(root,textvariable=p2Fours,fg='black',bg='cyan',font=('Tempus Sans ITC',12),command=p2FoursClick,relief=GROOVE)
            p2FoursButton.place(x=800,y=180,width=150,height=30)
        if((keptNumbers.count(5)==0 and throw.count(5)==0) and play.scoreList[4][1]=='x'):
            p2Fives.set(0)
            p2FivesButton=Button(root,textvariable=p2Fives,fg='black',bg='cyan',font=('Tempus Sans ITC',12),command=p2FivesClick,relief=GROOVE)
            p2FivesButton.place(x=800,y=210,width=150,height=30)
        if((keptNumbers.count(6)==0 and throw.count(6)==0) and play.scoreList[5][1]=='x'):
            p2Sixes.set(0)
            p2SixesButton=Button(root,textvariable=p2Sixes,fg='black',bg='cyan',font=('Tempus Sans ITC',12),command=p2SixesClick,relief=GROOVE)
            p2SixesButton.place(x=800,y=240,width=150,height=30)
        if(play.scoreList[8][1]=='x'):
            p2ThreeOfAKind.set(0)
            p2ThreeOfAKindButton=Button(root,textvariable=p2ThreeOfAKind,fg='black',bg='cyan',font=('Tempus Sans ITC',12),command=p2ThreeOfAKindClick,relief=GROOVE)
            p2ThreeOfAKindButton.place(x=800,y=330,width=150,height=30)
        if(play.scoreList[9][1]=='x'):
            p2FourOfAKind.set(0)
            p2FourOfAKindButton=Button(root,textvariable=p2FourOfAKind,fg='black',bg='cyan',font=('Tempus Sans ITC',12),command=p2FourOfAKindClick,relief=GROOVE)
            p2FourOfAKindButton.place(x=800,y=360,width=150,height=30)
        if(play.scoreList[10][1]=='x'):
            p2FullHouse.set(0)
            p2FullHouseButton=Button(root,textvariable=p2FullHouse,fg='black',bg='cyan',font=('Tempus Sans ITC',12),command=p2FullHouseClick,relief=GROOVE)
            p2FullHouseButton.place(x=800,y=390,width=150,height=30)
        if(play.scoreList[11][1]=='x'):
            p2SmallStraight.set(0)
            p2SmallStraightButton=Button(root,textvariable=p2SmallStraight,fg='black',bg='cyan',font=('Tempus Sans ITC',12),command=p2SmallStraightClick,relief=GROOVE)
            p2SmallStraightButton.place(x=800,y=420,width=150,height=30)
        if(play.scoreList[12][1]=='x'):
            p2LargeStraight.set(0)
            p2LargeStraightButton=Button(root,textvariable=p2LargeStraight,fg='black',bg='cyan',font=('Tempus Sans ITC',12),command=p2LargeStraightClick,relief=GROOVE)
            p2LargeStraightButton.place(x=800,y=450,width=150,height=30)
        if(play.scoreList[14][1]=='x'):
            p2Yahtzee.set(0)
            p2YahtzeeButton=Button(root,textvariable=p2Yahtzee,fg='black',bg='cyan',font=('Tempus Sans ITC',12),command=p2YahtzeeClick,relief=GROOVE)
            p2YahtzeeButton.place(x=800,y=510,width=150,height=30)
        p2ScoreAlready='Yes'

    if(len(keptNumbers)==5 and p2ScoreAlready=='no' and (play.ofKind(keptNumbers)=='threeOfAKind' or play.ofKind(keptNumbers)=='fourOfAKind' or play.ofKind(keptNumbers)=='fullHouse' or play.smallStraight(keptNumbers) or play.largeStraight(keptNumbers) or play.ofKind(keptNumbers)=='yahtzee')):
        if((keptNumbers.count(1)==0 and throw.count(1)==0) and play.scoreList[0][1]=='x'):
            p2Ones.set(0)
            p2OnesButton=Button(root,textvariable=p2Ones,fg='black',bg='cyan',font=('Tempus Sans ITC',12),command=p2OnesClick,relief=GROOVE)
            p2OnesButton.place(x=800,y=90,width=150,height=30)
        if((keptNumbers.count(2)==0 and throw.count(2)==0) and play.scoreList[1][1]=='x'):
            p2Twos.set(0)
            p2TwosButton=Button(root,textvariable=p2Twos,fg='black',bg='cyan',font=('Tempus Sans ITC',12),command=p2TwosClick,relief=GROOVE)
            p2TwosButton.place(x=800,y=120,width=150,height=30)
        if((keptNumbers.count(3)==0 and throw.count(3)==0) and play.scoreList[2][1]=='x'):
            p2Threes.set(0)
            p2ThreesButton=Button(root,textvariable=p2Threes,fg='black',bg='cyan',font=('Tempus Sans ITC',12),command=p2ThreesClick,relief=GROOVE)
            p2ThreesButton.place(x=800,y=150,width=150,height=30)
        if((keptNumbers.count(4)==0 and throw.count(4)==0) and play.scoreList[3][1]=='x'):
            p2Fours.set(0)
            p2FoursButton=Button(root,textvariable=p2Fours,fg='black',bg='cyan',font=('Tempus Sans ITC',12),command=p2FoursClick,relief=GROOVE)
            p2FoursButton.place(x=800,y=180,width=150,height=30)
        if((keptNumbers.count(5)==0 and throw.count(5)==0) and play.scoreList[4][1]=='x'):
            p2Fives.set(0)
            p2FivesButton=Button(root,textvariable=p2Fives,fg='black',bg='cyan',font=('Tempus Sans ITC',12),command=p2FivesClick,relief=GROOVE)
            p2FivesButton.place(x=800,y=210,width=150,height=30)
        if((keptNumbers.count(6)==0 and throw.count(6)==0) and play.scoreList[5][1]=='x'):
            p2Sixes.set(0)
            p2SixesButton=Button(root,textvariable=p2Sixes,fg='black',bg='cyan',font=('Tempus Sans ITC',12),command=p2SixesClick,relief=GROOVE)
            p2SixesButton.place(x=800,y=240,width=150,height=30)
        if(play.ofKind(keptNumbers)!='threeOfAKind' and play.scoreList[8][1]=='x'):
            p2ThreeOfAKind.set(0)
            p2ThreeOfAKindButton=Button(root,textvariable=p2ThreeOfAKind,fg='black',bg='cyan',font=('Tempus Sans ITC',12),command=p2ThreeOfAKindClick,relief=GROOVE)
            p2ThreeOfAKindButton.place(x=800,y=330,width=150,height=30)
        if(play.ofKind(keptNumbers)!='fourOfAKind' and play.scoreList[9][1]=='x'):
            p2FourOfAKind.set(0)
            p2FourOfAKindButton=Button(root,textvariable=p2FourOfAKind,fg='black',bg='cyan',font=('Tempus Sans ITC',12),command=p2FourOfAKindClick,relief=GROOVE)
            p2FourOfAKindButton.place(x=800,y=360,width=150,height=30)
        if(play.ofKind(keptNumbers)!='fullHouse' and play.scoreList[10][1]=='x'):
            p2FullHouse.set(0)
            p2FullHouseButton=Button(root,textvariable=p2FullHouse,fg='black',bg='cyan',font=('Tempus Sans ITC',12),command=p2FullHouseClick,relief=GROOVE)
            p2FullHouseButton.place(x=800,y=390,width=150,height=30)
        if(play.smallStraight(keptNumbers)!=True and play.scoreList[11][1]=='x'):
            p2SmallStraight.set(0)
            p2SmallStraightButton=Button(root,textvariable=p2SmallStraight,fg='black',bg='cyan',font=('Tempus Sans ITC',12),command=p2SmallStraightClick,relief=GROOVE)
            p2SmallStraightButton.place(x=800,y=420,width=150,height=30)
        if(play.largeStraight(keptNumbers)!=True and play.scoreList[12][1]=='x'):
            p2LargeStraight.set(0)
            p2LargeStraightButton=Button(root,textvariable=p2LargeStraight,fg='black',bg='cyan',font=('Tempus Sans ITC',12),command=p2LargeStraightClick,relief=GROOVE)
            p2LargeStraightButton.place(x=800,y=450,width=150,height=30)
        if(play.ofKind(keptNumbers)!='yahtzee' and play.scoreList[14][1]=='x'):
            p2Yahtzee.set(0)
            p2YahtzeeButton=Button(root,textvariable=p2Yahtzee,fg='black',bg='cyan',font=('Tempus Sans ITC',12),command=p2YahtzeeClick,relief=GROOVE)
            p2YahtzeeButton.place(x=800,y=510,width=150,height=30)



### Game Play ###

## Score Update ##
# Player 1 Score Update #
def p1OnesClick():
    global play,throwNumber,p1Ones,p1Sum,p1Bonus,p1TotalScore
    play.scoreList[0][0]=p1Ones.get()
    if(play.scoreList[0][0]!='x' and play.scoreList[1][0]!='x' and play.scoreList[2][0]!='x' and play.scoreList[3][0]!='x' and play.scoreList[4][0]!='x' and play.scoreList[5][0]!='x'):
        p1Sum.set(int(play.scoreList[0][0])+int(play.scoreList[1][0])+int(play.scoreList[2][0])+int(play.scoreList[3][0])+int(play.scoreList[4][0])+int(play.scoreList[5][0]))
        play.scoreList[6][0]=p1Sum.get()
        if(int(p1Sum.get())>=63):
            p1Bonus.set(35)
        else:
            p1Bonus.set(0)
        play.scoreList[7][0]=p1Bonus.get()
    if(play.scoreList[6][0]!='x' and play.scoreList[7][0]!='x' and play.scoreList[8][0]!='x' and play.scoreList[9][0]!='x' and play.scoreList[10][0]!='x' and play.scoreList[11][0]!='x' and play.scoreList[12][0]!='x' and play.scoreList[13][0]!='x' and play.scoreList[14][0]!='x'):
        p1TotalScore.set(int(play.scoreList[6][0])+int(play.scoreList[7][0])+int(play.scoreList[8][0])+int(play.scoreList[9][0])+int(play.scoreList[10][0])+int(play.scoreList[11][0])+int(play.scoreList[12][0])+int(play.scoreList[13][0])+int(play.scoreList[14][0]))
        play.scoreList[15][0]=p1TotalScore.get()
    scorecard()
    throwNumber=4
    Next()
def p1TwosClick():
    global play,throwNumber,p1Twos,p1Sum,p1Bonus,p1TotalScore
    play.scoreList[1][0]=p1Twos.get()
    if(play.scoreList[0][0]!='x' and play.scoreList[1][0]!='x' and play.scoreList[2][0]!='x' and play.scoreList[3][0]!='x' and play.scoreList[4][0]!='x' and play.scoreList[5][0]!='x'):
        p1Sum.set(int(play.scoreList[0][0])+int(play.scoreList[1][0])+int(play.scoreList[2][0])+int(play.scoreList[3][0])+int(play.scoreList[4][0])+int(play.scoreList[5][0]))
        play.scoreList[6][0]=p1Sum.get()
        if(int(p1Sum.get())>=63):
            p1Bonus.set(35)
        else:
            p1Bonus.set(0)
        play.scoreList[7][0]=p1Bonus.get()
    if(play.scoreList[6][0]!='x' and play.scoreList[7][0]!='x' and play.scoreList[8][0]!='x' and play.scoreList[9][0]!='x' and play.scoreList[10][0]!='x' and play.scoreList[11][0]!='x' and play.scoreList[12][0]!='x' and play.scoreList[13][0]!='x' and play.scoreList[14][0]!='x'):
        p1TotalScore.set(int(play.scoreList[6][0])+int(play.scoreList[7][0])+int(play.scoreList[8][0])+int(play.scoreList[9][0])+int(play.scoreList[10][0])+int(play.scoreList[11][0])+int(play.scoreList[12][0])+int(play.scoreList[13][0])+int(play.scoreList[14][0]))
        play.scoreList[15][0]=p1TotalScore.get()
    scorecard()
    throwNumber=4
    Next()
def p1ThreesClick():
    global play,throwNumber,p1Threes,p1Sum,p1Bonus,p1TotalScore
    play.scoreList[2][0]=p1Threes.get()
    if(play.scoreList[0][0]!='x' and play.scoreList[1][0]!='x' and play.scoreList[2][0]!='x' and play.scoreList[3][0]!='x' and play.scoreList[4][0]!='x' and play.scoreList[5][0]!='x'):
        p1Sum.set(int(play.scoreList[0][0])+int(play.scoreList[1][0])+int(play.scoreList[2][0])+int(play.scoreList[3][0])+int(play.scoreList[4][0])+int(play.scoreList[5][0]))
        play.scoreList[6][0]=p1Sum.get()
        if(int(p1Sum.get())>=63):
            p1Bonus.set(35)
        else:
            p1Bonus.set(0)
        play.scoreList[7][0]=p1Bonus.get()
    if(play.scoreList[6][0]!='x' and play.scoreList[7][0]!='x' and play.scoreList[8][0]!='x' and play.scoreList[9][0]!='x' and play.scoreList[10][0]!='x' and play.scoreList[11][0]!='x' and play.scoreList[12][0]!='x' and play.scoreList[13][0]!='x' and play.scoreList[14][0]!='x'):
        p1TotalScore.set(int(play.scoreList[6][0])+int(play.scoreList[7][0])+int(play.scoreList[8][0])+int(play.scoreList[9][0])+int(play.scoreList[10][0])+int(play.scoreList[11][0])+int(play.scoreList[12][0])+int(play.scoreList[13][0])+int(play.scoreList[14][0]))
        play.scoreList[15][0]=p1TotalScore.get()
    scorecard()
    throwNumber=4
    Next()
def p1FoursClick():
    global play,throwNumber,p1Fours,p1Sum,p1Bonus,p1TotalScore
    play.scoreList[3][0]=p1Fours.get()
    if(play.scoreList[0][0]!='x' and play.scoreList[1][0]!='x' and play.scoreList[2][0]!='x' and play.scoreList[3][0]!='x' and play.scoreList[4][0]!='x' and play.scoreList[5][0]!='x'):
        p1Sum.set(int(play.scoreList[0][0])+int(play.scoreList[1][0])+int(play.scoreList[2][0])+int(play.scoreList[3][0])+int(play.scoreList[4][0])+int(play.scoreList[5][0]))
        play.scoreList[6][0]=p1Sum.get()
        if(int(p1Sum.get())>=63):
            p1Bonus.set(35)
        else:
            p1Bonus.set(0)
        play.scoreList[7][0]=p1Bonus.get()
    if(play.scoreList[6][0]!='x' and play.scoreList[7][0]!='x' and play.scoreList[8][0]!='x' and play.scoreList[9][0]!='x' and play.scoreList[10][0]!='x' and play.scoreList[11][0]!='x' and play.scoreList[12][0]!='x' and play.scoreList[13][0]!='x' and play.scoreList[14][0]!='x'):
        p1TotalScore.set(int(play.scoreList[6][0])+int(play.scoreList[7][0])+int(play.scoreList[8][0])+int(play.scoreList[9][0])+int(play.scoreList[10][0])+int(play.scoreList[11][0])+int(play.scoreList[12][0])+int(play.scoreList[13][0])+int(play.scoreList[14][0]))
        play.scoreList[15][0]=p1TotalScore.get()
    scorecard()
    throwNumber=4
    Next()
def p1FivesClick():
    global play,throwNumber,p1Fives,p1Sum,p1Bonus,p1TotalScore
    play.scoreList[4][0]=p1Fives.get()
    if(play.scoreList[0][0]!='x' and play.scoreList[1][0]!='x' and play.scoreList[2][0]!='x' and play.scoreList[3][0]!='x' and play.scoreList[4][0]!='x' and play.scoreList[5][0]!='x'):
        p1Sum.set(int(play.scoreList[0][0])+int(play.scoreList[1][0])+int(play.scoreList[2][0])+int(play.scoreList[3][0])+int(play.scoreList[4][0])+int(play.scoreList[5][0]))
        play.scoreList[6][0]=p1Sum.get()
        if(int(p1Sum.get())>=63):
            p1Bonus.set(35)
        else:
            p1Bonus.set(0)
        play.scoreList[7][0]=p1Bonus.get()
    if(play.scoreList[6][0]!='x' and play.scoreList[7][0]!='x' and play.scoreList[8][0]!='x' and play.scoreList[9][0]!='x' and play.scoreList[10][0]!='x' and play.scoreList[11][0]!='x' and play.scoreList[12][0]!='x' and play.scoreList[13][0]!='x' and play.scoreList[14][0]!='x'):
        p1TotalScore.set(int(play.scoreList[6][0])+int(play.scoreList[7][0])+int(play.scoreList[8][0])+int(play.scoreList[9][0])+int(play.scoreList[10][0])+int(play.scoreList[11][0])+int(play.scoreList[12][0])+int(play.scoreList[13][0])+int(play.scoreList[14][0]))
        play.scoreList[15][0]=p1TotalScore.get()
    scorecard()
    throwNumber=4
    Next()
def p1SixesClick():
    global play,throwNumber,p1Sixes,p1Sum,p1Bonus,p1TotalScore
    play.scoreList[5][0]=p1Sixes.get()
    if(play.scoreList[0][0]!='x' and play.scoreList[1][0]!='x' and play.scoreList[2][0]!='x' and play.scoreList[3][0]!='x' and play.scoreList[4][0]!='x' and play.scoreList[5][0]!='x'):
        p1Sum.set(int(play.scoreList[0][0])+int(play.scoreList[1][0])+int(play.scoreList[2][0])+int(play.scoreList[3][0])+int(play.scoreList[4][0])+int(play.scoreList[5][0]))
        play.scoreList[6][0]=p1Sum.get()
        if(int(p1Sum.get())>=63):
            p1Bonus.set(35)
        else:
            p1Bonus.set(0)
        play.scoreList[7][0]=p1Bonus.get()
    if(play.scoreList[6][0]!='x' and play.scoreList[7][0]!='x' and play.scoreList[8][0]!='x' and play.scoreList[9][0]!='x' and play.scoreList[10][0]!='x' and play.scoreList[11][0]!='x' and play.scoreList[12][0]!='x' and play.scoreList[13][0]!='x' and play.scoreList[14][0]!='x'):
        p1TotalScore.set(int(play.scoreList[6][0])+int(play.scoreList[7][0])+int(play.scoreList[8][0])+int(play.scoreList[9][0])+int(play.scoreList[10][0])+int(play.scoreList[11][0])+int(play.scoreList[12][0])+int(play.scoreList[13][0])+int(play.scoreList[14][0]))
        play.scoreList[15][0]=p1TotalScore.get()
    scorecard()
    throwNumber=4
    Next()
def p1ThreeOfAKindClick():
    global play,throwNumber,p1ThreeOfAKind,p1Sum,p1Bonus,p1TotalScore
    play.scoreList[8][0]=p1ThreeOfAKind.get()
    if(play.scoreList[6][0]!='x' and play.scoreList[7][0]!='x' and play.scoreList[8][0]!='x' and play.scoreList[9][0]!='x' and play.scoreList[10][0]!='x' and play.scoreList[11][0]!='x' and play.scoreList[12][0]!='x' and play.scoreList[13][0]!='x' and play.scoreList[14][0]!='x'):
        p1TotalScore.set(int(play.scoreList[6][0])+int(play.scoreList[7][0])+int(play.scoreList[8][0])+int(play.scoreList[9][0])+int(play.scoreList[10][0])+int(play.scoreList[11][0])+int(play.scoreList[12][0])+int(play.scoreList[13][0])+int(play.scoreList[14][0]))
        play.scoreList[15][0]=p1TotalScore.get()
    scorecard()
    throwNumber=4
    Next()
def p1FourOfAKindClick():
    global play,throwNumber,p1FourOfAKind,p1Sum,p1Bonus,p1TotalScore
    play.scoreList[9][0]=p1FourOfAKind.get()
    if(play.scoreList[6][0]!='x' and play.scoreList[7][0]!='x' and play.scoreList[8][0]!='x' and play.scoreList[9][0]!='x' and play.scoreList[10][0]!='x' and play.scoreList[11][0]!='x' and play.scoreList[12][0]!='x' and play.scoreList[13][0]!='x' and play.scoreList[14][0]!='x'):
        p1TotalScore.set(int(play.scoreList[6][0])+int(play.scoreList[7][0])+int(play.scoreList[8][0])+int(play.scoreList[9][0])+int(play.scoreList[10][0])+int(play.scoreList[11][0])+int(play.scoreList[12][0])+int(play.scoreList[13][0])+int(play.scoreList[14][0]))
        play.scoreList[15][0]=p1TotalScore.get()
    scorecard()
    throwNumber=4
    Next()
def p1FullHouseClick():
    global play,throwNumber,p1FullHouse,p1Sum,p1Bonus,p1TotalScore
    play.scoreList[10][0]=p1FullHouse.get()
    if(play.scoreList[6][0]!='x' and play.scoreList[7][0]!='x' and play.scoreList[8][0]!='x' and play.scoreList[9][0]!='x' and play.scoreList[10][0]!='x' and play.scoreList[11][0]!='x' and play.scoreList[12][0]!='x' and play.scoreList[13][0]!='x' and play.scoreList[14][0]!='x'):
        p1TotalScore.set(int(play.scoreList[6][0])+int(play.scoreList[7][0])+int(play.scoreList[8][0])+int(play.scoreList[9][0])+int(play.scoreList[10][0])+int(play.scoreList[11][0])+int(play.scoreList[12][0])+int(play.scoreList[13][0])+int(play.scoreList[14][0]))
        play.scoreList[15][0]=p1TotalScore.get()
    scorecard()
    throwNumber=4
    Next()
def p1SmallStraightClick():
    global play,throwNumber,p1SmallStraight,p1Sum,p1Bonus,p1TotalScore
    play.scoreList[11][0]=p1SmallStraight.get()
    if(play.scoreList[6][0]!='x' and play.scoreList[7][0]!='x' and play.scoreList[8][0]!='x' and play.scoreList[9][0]!='x' and play.scoreList[10][0]!='x' and play.scoreList[11][0]!='x' and play.scoreList[12][0]!='x' and play.scoreList[13][0]!='x' and play.scoreList[14][0]!='x'):
        p1TotalScore.set(int(play.scoreList[6][0])+int(play.scoreList[7][0])+int(play.scoreList[8][0])+int(play.scoreList[9][0])+int(play.scoreList[10][0])+int(play.scoreList[11][0])+int(play.scoreList[12][0])+int(play.scoreList[13][0])+int(play.scoreList[14][0]))
        play.scoreList[15][0]=p1TotalScore.get()
    scorecard()
    throwNumber=4
    Next()
def p1LargeStraightClick():
    global play,throwNumber,p1LargeStraight,p1Sum,p1Bonus,p1TotalScore
    play.scoreList[12][0]=p1LargeStraight.get()
    if(play.scoreList[6][0]!='x' and play.scoreList[7][0]!='x' and play.scoreList[8][0]!='x' and play.scoreList[9][0]!='x' and play.scoreList[10][0]!='x' and play.scoreList[11][0]!='x' and play.scoreList[12][0]!='x' and play.scoreList[13][0]!='x' and play.scoreList[14][0]!='x'):
        p1TotalScore.set(int(play.scoreList[6][0])+int(play.scoreList[7][0])+int(play.scoreList[8][0])+int(play.scoreList[9][0])+int(play.scoreList[10][0])+int(play.scoreList[11][0])+int(play.scoreList[12][0])+int(play.scoreList[13][0])+int(play.scoreList[14][0]))
        play.scoreList[15][0]=p1TotalScore.get()
    scorecard()
    throwNumber=4
    Next()
def p1ChanceClick():
    global play,throwNumber,p1Chance,p1Sum,p1Bonus,p1TotalScore
    play.scoreList[13][0]=p1Chance.get()
    if(play.scoreList[6][0]!='x' and play.scoreList[7][0]!='x' and play.scoreList[8][0]!='x' and play.scoreList[9][0]!='x' and play.scoreList[10][0]!='x' and play.scoreList[11][0]!='x' and play.scoreList[12][0]!='x' and play.scoreList[13][0]!='x' and play.scoreList[14][0]!='x'):
        p1TotalScore.set(int(play.scoreList[6][0])+int(play.scoreList[7][0])+int(play.scoreList[8][0])+int(play.scoreList[9][0])+int(play.scoreList[10][0])+int(play.scoreList[11][0])+int(play.scoreList[12][0])+int(play.scoreList[13][0])+int(play.scoreList[14][0]))
        play.scoreList[15][0]=p1TotalScore.get()
    scorecard()
    throwNumber=4
    Next()
def p1YahtzeeClick():
    global play,throwNumber,p1Yahtzee,p1Sum,p1Bonus,p1TotalScore
    play.scoreList[14][0]=p1Yahtzee.get()
    if(play.scoreList[6][0]!='x' and play.scoreList[7][0]!='x' and play.scoreList[8][0]!='x' and play.scoreList[9][0]!='x' and play.scoreList[10][0]!='x' and play.scoreList[11][0]!='x' and play.scoreList[12][0]!='x' and play.scoreList[13][0]!='x' and play.scoreList[14][0]!='x'):
        p1TotalScore.set(int(play.scoreList[6][0])+int(play.scoreList[7][0])+int(play.scoreList[8][0])+int(play.scoreList[9][0])+int(play.scoreList[10][0])+int(play.scoreList[11][0])+int(play.scoreList[12][0])+int(play.scoreList[13][0])+int(play.scoreList[14][0]))
        play.scoreList[15][0]=p1TotalScore.get()
    scorecard()
    throwNumber=4
    Next()
# Player 2 Score Update #
def p2OnesClick():
    global play,throwNumber,p2Ones,p2Sum,p2Bonus,p2TotalScore
    play.scoreList[0][1]=p2Ones.get()
    if(play.scoreList[0][1]!='x' and play.scoreList[1][1]!='x' and play.scoreList[2][1]!='x' and play.scoreList[3][1]!='x' and play.scoreList[4][1]!='x' and play.scoreList[5][1]!='x'):
        p2Sum.set(int(play.scoreList[0][1])+int(play.scoreList[1][1])+int(play.scoreList[2][1])+int(play.scoreList[3][1])+int(play.scoreList[4][1])+int(play.scoreList[5][1]))
        play.scoreList[6][1]=p2Sum.get()
        if(int(p2Sum.get())>=63):
            p2Bonus.set(35)
        else:
            p2Bonus.set(0)
        play.scoreList[7][1]=p2Bonus.get()
    if(play.scoreList[6][1]!='x' and play.scoreList[7][1]!='x' and play.scoreList[8][1]!='x' and play.scoreList[9][1]!='x' and play.scoreList[10][1]!='x' and play.scoreList[11][1]!='x' and play.scoreList[12][1]!='x' and play.scoreList[13][1]!='x' and play.scoreList[14][1]!='x'):
        p2TotalScore.set(int(play.scoreList[6][1])+int(play.scoreList[7][1])+int(play.scoreList[8][1])+int(play.scoreList[9][1])+int(play.scoreList[10][1])+int(play.scoreList[11][1])+int(play.scoreList[12][1])+int(play.scoreList[13][1])+int(play.scoreList[14][1]))
        play.scoreList[15][1]=p2TotalScore.get()
    scorecard()
    throwNumber=0
    Next()
def p2TwosClick():
    global play,throwNumber,p2Twos,p2Sum,p2Bonus,p2TotalScore
    play.scoreList[1][1]=p2Twos.get()
    if(play.scoreList[0][1]!='x' and play.scoreList[1][1]!='x' and play.scoreList[2][1]!='x' and play.scoreList[3][1]!='x' and play.scoreList[4][1]!='x' and play.scoreList[5][1]!='x'):
        p2Sum.set(int(play.scoreList[0][1])+int(play.scoreList[1][1])+int(play.scoreList[2][1])+int(play.scoreList[3][1])+int(play.scoreList[4][1])+int(play.scoreList[5][1]))
        play.scoreList[6][1]=p2Sum.get()
        if(int(p2Sum.get())>=63):
            p2Bonus.set(35)
        else:
            p2Bonus.set(0)
        play.scoreList[7][1]=p2Bonus.get()
    if(play.scoreList[6][1]!='x' and play.scoreList[7][1]!='x' and play.scoreList[8][1]!='x' and play.scoreList[9][1]!='x' and play.scoreList[10][1]!='x' and play.scoreList[11][1]!='x' and play.scoreList[12][1]!='x' and play.scoreList[13][1]!='x' and play.scoreList[14][1]!='x'):
        p2TotalScore.set(int(play.scoreList[6][1])+int(play.scoreList[7][1])+int(play.scoreList[8][1])+int(play.scoreList[9][1])+int(play.scoreList[10][1])+int(play.scoreList[11][1])+int(play.scoreList[12][1])+int(play.scoreList[13][1])+int(play.scoreList[14][1]))
        play.scoreList[15][1]=p2TotalScore.get()
    scorecard()
    throwNumber=0
    Next()
def p2ThreesClick():
    global play,throwNumber,p2Threes,p2Sum,p2Bonus,p2TotalScore
    play.scoreList[2][1]=p2Threes.get()
    if(play.scoreList[0][1]!='x' and play.scoreList[1][1]!='x' and play.scoreList[2][1]!='x' and play.scoreList[3][1]!='x' and play.scoreList[4][1]!='x' and play.scoreList[5][1]!='x'):
        p2Sum.set(int(play.scoreList[0][1])+int(play.scoreList[1][1])+int(play.scoreList[2][1])+int(play.scoreList[3][1])+int(play.scoreList[4][1])+int(play.scoreList[5][1]))
        play.scoreList[6][1]=p2Sum.get()
        if(int(p2Sum.get())>=63):
            p2Bonus.set(35)
        else:
            p2Bonus.set(0)
        play.scoreList[7][1]=p2Bonus.get()
    if(play.scoreList[6][1]!='x' and play.scoreList[7][1]!='x' and play.scoreList[8][1]!='x' and play.scoreList[9][1]!='x' and play.scoreList[10][1]!='x' and play.scoreList[11][1]!='x' and play.scoreList[12][1]!='x' and play.scoreList[13][1]!='x' and play.scoreList[14][1]!='x'):
        p2TotalScore.set(int(play.scoreList[6][1])+int(play.scoreList[7][1])+int(play.scoreList[8][1])+int(play.scoreList[9][1])+int(play.scoreList[10][1])+int(play.scoreList[11][1])+int(play.scoreList[12][1])+int(play.scoreList[13][1])+int(play.scoreList[14][1]))
        play.scoreList[15][1]=p2TotalScore.get()
    scorecard()
    throwNumber=0
    Next()
def p2FoursClick():
    global play,throwNumber,p2Fours,p2Sum,p2Bonus,p2TotalScore
    play.scoreList[3][1]=p2Fours.get()
    if(play.scoreList[0][1]!='x' and play.scoreList[1][1]!='x' and play.scoreList[2][1]!='x' and play.scoreList[3][1]!='x' and play.scoreList[4][1]!='x' and play.scoreList[5][1]!='x'):
        p2Sum.set(int(play.scoreList[0][1])+int(play.scoreList[1][1])+int(play.scoreList[2][1])+int(play.scoreList[3][1])+int(play.scoreList[4][1])+int(play.scoreList[5][1]))
        play.scoreList[6][1]=p2Sum.get()
        if(int(p2Sum.get())>=63):
            p2Bonus.set(35)
        else:
            p2Bonus.set(0)
        play.scoreList[7][1]=p2Bonus.get()
    if(play.scoreList[6][1]!='x' and play.scoreList[7][1]!='x' and play.scoreList[8][1]!='x' and play.scoreList[9][1]!='x' and play.scoreList[10][1]!='x' and play.scoreList[11][1]!='x' and play.scoreList[12][1]!='x' and play.scoreList[13][1]!='x' and play.scoreList[14][1]!='x'):
        p2TotalScore.set(int(play.scoreList[6][1])+int(play.scoreList[7][1])+int(play.scoreList[8][1])+int(play.scoreList[9][1])+int(play.scoreList[10][1])+int(play.scoreList[11][1])+int(play.scoreList[12][1])+int(play.scoreList[13][1])+int(play.scoreList[14][1]))
        play.scoreList[15][1]=p2TotalScore.get()
    scorecard()
    throwNumber=0
    Next()
def p2FivesClick():
    global play,throwNumber,p2Fives,p2Sum,p2Bonus,p2TotalScore
    play.scoreList[4][1]=p2Fives.get()
    if(play.scoreList[0][1]!='x' and play.scoreList[1][1]!='x' and play.scoreList[2][1]!='x' and play.scoreList[3][1]!='x' and play.scoreList[4][1]!='x' and play.scoreList[5][1]!='x'):
        p2Sum.set(int(play.scoreList[0][1])+int(play.scoreList[1][1])+int(play.scoreList[2][1])+int(play.scoreList[3][1])+int(play.scoreList[4][1])+int(play.scoreList[5][1]))
        play.scoreList[6][1]=p2Sum.get()
        if(int(p2Sum.get())>=63):
            p2Bonus.set(35)
        else:
            p2Bonus.set(0)
        play.scoreList[7][1]=p2Bonus.get()
    if(play.scoreList[6][1]!='x' and play.scoreList[7][1]!='x' and play.scoreList[8][1]!='x' and play.scoreList[9][1]!='x' and play.scoreList[10][1]!='x' and play.scoreList[11][1]!='x' and play.scoreList[12][1]!='x' and play.scoreList[13][1]!='x' and play.scoreList[14][1]!='x'):
        p2TotalScore.set(int(play.scoreList[6][1])+int(play.scoreList[7][1])+int(play.scoreList[8][1])+int(play.scoreList[9][1])+int(play.scoreList[10][1])+int(play.scoreList[11][1])+int(play.scoreList[12][1])+int(play.scoreList[13][1])+int(play.scoreList[14][1]))
        play.scoreList[15][1]=p2TotalScore.get()
    scorecard()
    throwNumber=0
    Next()
def p2SixesClick():
    global play,throwNumber,p2Sixes,p2Sum,p2Bonus,p2TotalScore
    play.scoreList[5][1]=p2Sixes.get()
    if(play.scoreList[0][1]!='x' and play.scoreList[1][1]!='x' and play.scoreList[2][1]!='x' and play.scoreList[3][1]!='x' and play.scoreList[4][1]!='x' and play.scoreList[5][1]!='x'):
        p2Sum.set(int(play.scoreList[0][1])+int(play.scoreList[1][1])+int(play.scoreList[2][1])+int(play.scoreList[3][1])+int(play.scoreList[4][1])+int(play.scoreList[5][1]))
        play.scoreList[6][1]=p2Sum.get()
        if(int(p2Sum.get())>=63):
            p2Bonus.set(35)
        else:
            p2Bonus.set(0)
        play.scoreList[7][1]=p2Bonus.get()
    if(play.scoreList[6][1]!='x' and play.scoreList[7][1]!='x' and play.scoreList[8][1]!='x' and play.scoreList[9][1]!='x' and play.scoreList[10][1]!='x' and play.scoreList[11][1]!='x' and play.scoreList[12][1]!='x' and play.scoreList[13][1]!='x' and play.scoreList[14][1]!='x'):
        p2TotalScore.set(int(play.scoreList[6][1])+int(play.scoreList[7][1])+int(play.scoreList[8][1])+int(play.scoreList[9][1])+int(play.scoreList[10][1])+int(play.scoreList[11][1])+int(play.scoreList[12][1])+int(play.scoreList[13][1])+int(play.scoreList[14][1]))
        play.scoreList[15][1]=p2TotalScore.get()
    scorecard()
    throwNumber=0
    Next()
def p2ThreeOfAKindClick():
    global play,throwNumber,p2ThreeOfAKind,p2Sum,p2Bonus,p2TotalScore
    play.scoreList[8][1]=p2ThreeOfAKind.get()
    if(play.scoreList[6][1]!='x' and play.scoreList[7][1]!='x' and play.scoreList[8][1]!='x' and play.scoreList[9][1]!='x' and play.scoreList[10][1]!='x' and play.scoreList[11][1]!='x' and play.scoreList[12][1]!='x' and play.scoreList[13][1]!='x' and play.scoreList[14][1]!='x'):
        p2TotalScore.set(int(play.scoreList[6][1])+int(play.scoreList[7][1])+int(play.scoreList[8][1])+int(play.scoreList[9][1])+int(play.scoreList[10][1])+int(play.scoreList[11][1])+int(play.scoreList[12][1])+int(play.scoreList[13][1])+int(play.scoreList[14][1]))
        play.scoreList[15][1]=p2TotalScore.get()
    scorecard()
    throwNumber=0
    Next()
def p2FourOfAKindClick():
    global play,throwNumber,p2FourOfAKind,p2Sum,p2Bonus,p2TotalScore
    play.scoreList[9][1]=p2FourOfAKind.get()
    if(play.scoreList[6][1]!='x' and play.scoreList[7][1]!='x' and play.scoreList[8][1]!='x' and play.scoreList[9][1]!='x' and play.scoreList[10][1]!='x' and play.scoreList[11][1]!='x' and play.scoreList[12][1]!='x' and play.scoreList[13][1]!='x' and play.scoreList[14][1]!='x'):
        p2TotalScore.set(int(play.scoreList[6][1])+int(play.scoreList[7][1])+int(play.scoreList[8][1])+int(play.scoreList[9][1])+int(play.scoreList[10][1])+int(play.scoreList[11][1])+int(play.scoreList[12][1])+int(play.scoreList[13][1])+int(play.scoreList[14][1]))
        play.scoreList[15][1]=p2TotalScore.get()
    scorecard()
    throwNumber=0
    Next()
def p2FullHouseClick():
    global play,throwNumber,p2FullHouse,p2Sum,p2Bonus,p2TotalScore
    play.scoreList[10][1]=p2FullHouse.get()
    if(play.scoreList[6][1]!='x' and play.scoreList[7][1]!='x' and play.scoreList[8][1]!='x' and play.scoreList[9][1]!='x' and play.scoreList[10][1]!='x' and play.scoreList[11][1]!='x' and play.scoreList[12][1]!='x' and play.scoreList[13][1]!='x' and play.scoreList[14][1]!='x'):
        p2TotalScore.set(int(play.scoreList[6][1])+int(play.scoreList[7][1])+int(play.scoreList[8][1])+int(play.scoreList[9][1])+int(play.scoreList[10][1])+int(play.scoreList[11][1])+int(play.scoreList[12][1])+int(play.scoreList[13][1])+int(play.scoreList[14][1]))
        play.scoreList[15][1]=p2TotalScore.get()
    scorecard()
    throwNumber=0
    Next()
def p2SmallStraightClick():
    global play,throwNumber,p2SmallStraight,p2Sum,p2Bonus,p2TotalScore
    play.scoreList[11][1]=p2SmallStraight.get()
    if(play.scoreList[6][1]!='x' and play.scoreList[7][1]!='x' and play.scoreList[8][1]!='x' and play.scoreList[9][1]!='x' and play.scoreList[10][1]!='x' and play.scoreList[11][1]!='x' and play.scoreList[12][1]!='x' and play.scoreList[13][1]!='x' and play.scoreList[14][1]!='x'):
        p2TotalScore.set(int(play.scoreList[6][1])+int(play.scoreList[7][1])+int(play.scoreList[8][1])+int(play.scoreList[9][1])+int(play.scoreList[10][1])+int(play.scoreList[11][1])+int(play.scoreList[12][1])+int(play.scoreList[13][1])+int(play.scoreList[14][1]))
        play.scoreList[15][1]=p2TotalScore.get()
    scorecard()
    throwNumber=0
    Next()
def p2LargeStraightClick():
    global play,throwNumber,p2LargeStraight,p2Sum,p2Bonus,p2TotalScore
    play.scoreList[12][1]=p2LargeStraight.get()
    if(play.scoreList[6][1]!='x' and play.scoreList[7][1]!='x' and play.scoreList[8][1]!='x' and play.scoreList[9][1]!='x' and play.scoreList[10][1]!='x' and play.scoreList[11][1]!='x' and play.scoreList[12][1]!='x' and play.scoreList[13][1]!='x' and play.scoreList[14][1]!='x'):
        p2TotalScore.set(int(play.scoreList[6][1])+int(play.scoreList[7][1])+int(play.scoreList[8][1])+int(play.scoreList[9][1])+int(play.scoreList[10][1])+int(play.scoreList[11][1])+int(play.scoreList[12][1])+int(play.scoreList[13][1])+int(play.scoreList[14][1]))
        play.scoreList[15][1]=p2TotalScore.get()
    scorecard()
    throwNumber=0
    Next()
def p2ChanceClick():
    global play,throwNumber,p2Chance,p2Sum,p2Bonus,p2TotalScore
    play.scoreList[13][1]=p2Chance.get()
    if(play.scoreList[6][1]!='x' and play.scoreList[7][1]!='x' and play.scoreList[8][1]!='x' and play.scoreList[9][1]!='x' and play.scoreList[10][1]!='x' and play.scoreList[11][1]!='x' and play.scoreList[12][1]!='x' and play.scoreList[13][1]!='x' and play.scoreList[14][1]!='x'):
        p2TotalScore.set(int(play.scoreList[6][1])+int(play.scoreList[7][1])+int(play.scoreList[8][1])+int(play.scoreList[9][1])+int(play.scoreList[10][1])+int(play.scoreList[11][1])+int(play.scoreList[12][1])+int(play.scoreList[13][1])+int(play.scoreList[14][1]))
        play.scoreList[15][1]=p2TotalScore.get()
    scorecard()
    throwNumber=0
    Next()
def p2YahtzeeClick():
    global play,throwNumber,p2Yahtzee,p2Sum,p2Bonus,p2TotalScore
    play.scoreList[14][1]=p2Yahtzee.get()
    if(play.scoreList[6][1]!='x' and play.scoreList[7][1]!='x' and play.scoreList[8][1]!='x' and play.scoreList[9][1]!='x' and play.scoreList[10][1]!='x' and play.scoreList[11][1]!='x' and play.scoreList[12][1]!='x' and play.scoreList[13][1]!='x' and play.scoreList[14][1]!='x'):
        p2TotalScore.set(int(play.scoreList[6][1])+int(play.scoreList[7][1])+int(play.scoreList[8][1])+int(play.scoreList[9][1])+int(play.scoreList[10][1])+int(play.scoreList[11][1])+int(play.scoreList[12][1])+int(play.scoreList[13][1])+int(play.scoreList[14][1]))
        play.scoreList[15][1]=p2TotalScore.get()
    scorecard()
    throwNumber=0
    Next()

## Dice Update ##
def dice():
    global play,throwNumber,throw,keptNumbers
    
    background()
    scorecard()

    if(throwNumber<=4):    # For Player 1
        player1TurnLabel=Label(root,textvariable=player1TurnName,fg='white',bg='green',font=('Tempus Sans ITC',20,'bold'))
        player1TurnLabel.place(x=50,y=50,width=350,height=50)
        player1ThrowLabel=Label(root,textvariable=player1Throw,fg='black',bg='cyan',font=('Tempus Sans ITC',10))
        player1ThrowLabel.place(x=50,y=130,width=350,height=80)
        player1Score()
    if(throwNumber>=5):    # For Player 2
        player2TurnLabel=Label(root,textvariable=player2TurnName,fg='white',bg='green',font=('Tempus Sans ITC',20,'bold'))
        player2TurnLabel.place(x=100,y=50,width=250,height=50)
        player2ThrowLabel=Label(root,textvariable=player2Throw,fg='black',bg='cyan',font=('Tempus Sans ITC',10))
        player2ThrowLabel.place(x=50,y=130,width=350,height=80)
        player2Score()
    
    rollDiceButton=Button(root,text='Roll Dice',fg='black',bg='yellow',font=('Tempus Sans ITC',13,'bold'),command=Next)
    rollDiceButton.place(x=175,y=350,width=100,height=40)
    if(len(keptNumbers)==5 or throwNumber==4 or throwNumber==8):
        rollDiceLabel=Label(root,text='Roll Dice',fg='grey',bg='yellow',font=('Tempus Sans ITC',13,'bold'))
        rollDiceLabel.place(x=175,y=350,width=100,height=40)
    keptDiceLabel=Label(root,text='Kept Dice',fg='white',bg='green',font=('Tempus Sans ITC',15,'bold'))
    keptDiceLabel.place(x=50,y=450,width=350,height=40)
    buttons()
    
    def keptDice(number):    # Kept Dice update
        global throwNumber
        keptNumbers.append(number)
        if(throwNumber<=4 and len(keptNumbers)==5):
            throwNumber=throwNumber-1
            Next()
            rollDiceLabel=Label(root,text='Roll Dice',fg='grey',bg='yellow',font=('Tempus Sans ITC',13,'bold'))
            rollDiceLabel.place(x=175,y=350,width=100,height=40)
        elif(throwNumber>=5 and throwNumber<=8 and len(keptNumbers)==5):
            throwNumber=throwNumber-1
            Next()
            rollDiceLabel=Label(root,text='Roll Dice',fg='grey',bg='yellow',font=('Tempus Sans ITC',13,'bold'))
            rollDiceLabel.place(x=175,y=350,width=100,height=40)
        else:
            throw.remove(number)
            dice()         
    def removeDice(number):    # Remove Dice update
        global throwNumber
        play.removeDie(number,throw,keptNumbers)
        dice()
        
    for i in range(len(throw)):
        if(throw[i]==1):
            dieImageButton=Button(root,image=dieOneImage,command=lambda : keptDice(1))
            dieImageButton.place(x=(100+i*50),y=275)
        if(throw[i]==2):
            dieImageButton=Button(root,image=dieTwoImage,command=lambda : keptDice(2))
            dieImageButton.place(x=(100+i*50),y=275)
        if(throw[i]==3):
            dieImageButton=Button(root,image=dieThreeImage,command=lambda : keptDice(3))
            dieImageButton.place(x=(100+i*50),y=275)
        if(throw[i]==4):
            dieImageButton=Button(root,image=dieFourImage,command=lambda : keptDice(4))
            dieImageButton.place(x=(100+i*50),y=275)
        if(throw[i]==5):
            dieImageButton=Button(root,image=dieFiveImage,command=lambda : keptDice(5))
            dieImageButton.place(x=(100+i*50),y=275)
        if(throw[i]==6):
            dieImageButton=Button(root,image=dieSixImage,command=lambda : keptDice(6))
            dieImageButton.place(x=(100+i*50),y=275)
    for j in range(len(keptNumbers)):
        if(keptNumbers[j]==1):
            keptDieImageButton=Button(root,image=dieOneImage,command=lambda : removeDice(1))
            keptDieImageButton.place(x=(100+j*50),y=520)
        if(keptNumbers[j]==2):
            keptDieImageButton=Button(root,image=dieTwoImage,command=lambda : removeDice(2))
            keptDieImageButton.place(x=(100+j*50),y=520)
        if(keptNumbers[j]==3):
            keptDieImageButton=Button(root,image=dieThreeImage,command=lambda : removeDice(3))
            keptDieImageButton.place(x=(100+j*50),y=520)
        if(keptNumbers[j]==4):
            keptDieImageButton=Button(root,image=dieFourImage,command=lambda : removeDice(4))
            keptDieImageButton.place(x=(100+j*50),y=520)
        if(keptNumbers[j]==5):
            keptDieImageButton=Button(root,image=dieFiveImage,command=lambda : removeDice(5))
            keptDieImageButton.place(x=(100+j*50),y=520)
        if(keptNumbers[j]==6):
            keptDieImageButton=Button(root,image=dieSixImage,command=lambda : removeDice(6))
            keptDieImageButton.place(x=(100+j*50),y=520)

## Play window ##
def Next():
    global play,throwNumber,throw,keptNumbers,player1Name,player2Name,player1TurnName,player2TurnName,player1Throw,player2Throw,result,recordText,turnCount
    
    if(turnCount==0):
        play=Yahtzee(player1Name.get(),player2Name.get())

    if(throwNumber==8):
        throwNumber=0
    if(throwNumber==0 or throwNumber==4):
        keptNumbers=[]
    throwNumber=throwNumber+1

    throw=play.throw(keptNumbers)

    if(throwNumber<=4):    # Player 1 Turn
        if(throwNumber==1):
            background()
            scorecard()
            ### Dice Rolls ###
            player1TurnName.set(player1Name.get()+f'\'s Turn')
            throwText=f'Click the Dice you want to keep. In the kept Dice, click the\nDice you want to remove from the kept Dice. In the\nscorecard, click the highlighted field to add as your score.\nYou have 3 throw(s) left.'
            player1Throw.set(throwText)
            player1TurnLabel=Label(root,textvariable=player1TurnName,fg='white',bg='green',font=('Tempus Sans ITC',20,'bold'))
            player1TurnLabel.place(x=50,y=50,width=350,height=50)
            player1ThrowLabel=Label(root,textvariable=player1Throw,fg='black',bg='cyan',font=('Tempus Sans ITC',10))
            player1ThrowLabel.place(x=50,y=130,width=350,height=80)
            beforeThrowDieLabels()
            rollDiceButton=Button(root,text='Roll Dice',fg='black',bg='yellow',font=('Tempus Sans ITC',13,'bold'),command=Next)
            rollDiceButton.place(x=175,y=350,width=100,height=40)
            keptDiceLabel=Label(root,text='Kept Dice',fg='white',bg='green',font=('Tempus Sans ITC',15,'bold'))
            keptDiceLabel.place(x=50,y=450,width=350,height=40)
            buttons()
        if(throwNumber>1 and throwNumber<=4):
            background()
            scorecard()
            ### Dice Rolls ###
            player1TurnName.set(player1Name.get()+f'\'s Turn')
            throwText=f'Click the Dice you want to keep. In the kept Dice, click the\nDice you want to remove from the kept Dice. In the\nscorecard, click the highlighted field to add as your score.\nYou have {4-throwNumber} throw(s) left.'
            player1Throw.set(throwText)
            player1TurnLabel=Label(root,textvariable=player1TurnName,fg='white',bg='green',font=('Tempus Sans ITC',20,'bold'))
            player1TurnLabel.place(x=50,y=50,width=350,height=50)
            player1ThrowLabel=Label(root,textvariable=player1Throw,fg='black',bg='cyan',font=('Tempus Sans ITC',10))
            player1ThrowLabel.place(x=50,y=130,width=350,height=80)
            rollDiceButton=Button(root,text='Roll Dice',fg='black',bg='yellow',font=('Tempus Sans ITC',13,'bold'),command=Next)
            rollDiceButton.place(x=175,y=350,width=100,height=40)
            if(throwNumber==4):
                rollDiceLabel=Label(root,text='Roll Dice',fg='grey',bg='yellow',font=('Tempus Sans ITC',13,'bold'))
                rollDiceLabel.place(x=175,y=350,width=100,height=40)
            keptDiceLabel=Label(root,text='Kept Dice',fg='white',bg='green',font=('Tempus Sans ITC',15,'bold'))
            keptDiceLabel.place(x=50,y=450,width=350,height=40)
            buttons()
            def keptDice(number):
                play.keepDie(number,keptNumbers,throw)
                dice()
            def removeDice(number):
                play.removeDie(number,throw,keptNumbers)
                dice()
            for i in range(len(throw)):
                if(throw[i]==1):
                    dieImageButton=Button(root,image=dieOneImage,command=lambda : keptDice(1))
                    dieImageButton.place(x=(100+i*50),y=275)
                if(throw[i]==2):
                    dieImageButton=Button(root,image=dieTwoImage,command=lambda : keptDice(2))
                    dieImageButton.place(x=(100+i*50),y=275)
                if(throw[i]==3):
                    dieImageButton=Button(root,image=dieThreeImage,command=lambda : keptDice(3))
                    dieImageButton.place(x=(100+i*50),y=275)
                if(throw[i]==4):
                    dieImageButton=Button(root,image=dieFourImage,command=lambda : keptDice(4))
                    dieImageButton.place(x=(100+i*50),y=275)
                if(throw[i]==5):
                    dieImageButton=Button(root,image=dieFiveImage,command=lambda : keptDice(5))
                    dieImageButton.place(x=(100+i*50),y=275)
                if(throw[i]==6):
                    dieImageButton=Button(root,image=dieSixImage,command=lambda : keptDice(6))
                    dieImageButton.place(x=(100+i*50),y=275)
            for j in range(len(keptNumbers)):
                if(keptNumbers[j]==1):
                    keptDieImageButton=Button(root,image=dieOneImage,command=lambda : removeDice(1))
                    keptDieImageButton.place(x=(100+j*50),y=520)
                if(keptNumbers[j]==2):
                    keptDieImageButton=Button(root,image=dieTwoImage,command=lambda : removeDice(2))
                    keptDieImageButton.place(x=(100+j*50),y=520)
                if(keptNumbers[j]==3):
                    keptDieImageButton=Button(root,image=dieThreeImage,command=lambda : removeDice(3))
                    keptDieImageButton.place(x=(100+j*50),y=520)
                if(keptNumbers[j]==4):
                    keptDieImageButton=Button(root,image=dieFourImage,command=lambda : removeDice(4))
                    keptDieImageButton.place(x=(100+j*50),y=520)
                if(keptNumbers[j]==5):
                    keptDieImageButton=Button(root,image=dieFiveImage,command=lambda : removeDice(5))
                    keptDieImageButton.place(x=(100+j*50),y=520)
                if(keptNumbers[j]==6):
                    keptDieImageButton=Button(root,image=dieSixImage,command=lambda : removeDice(6))
                    keptDieImageButton.place(x=(100+j*50),y=520)
            player1Score()
    if(throwNumber>=5):    # Player 2 Turn
        if(throwNumber==5):
            background()
            scorecard()
            ### Dice Rolls ###
            player2TurnName.set(player2Name.get()+f'\'s Turn')
            throwText=f'Click the Dice you want to keep. In the kept Dice, click the\nDice you want to remove from the kept Dice. In the\nscorecard, click the highlighted field to add as your score.\nYou have 3 throw(s) left.'
            player2Throw.set(throwText)
            player2TurnLabel=Label(root,textvariable=player2TurnName,fg='white',bg='green',font=('Tempus Sans ITC',20,'bold'))
            player2TurnLabel.place(x=100,y=50,width=250,height=50)
            player2ThrowLabel=Label(root,textvariable=player2Throw,fg='black',bg='cyan',font=('Tempus Sans ITC',10))
            player2ThrowLabel.place(x=50,y=130,width=350,height=80)
            beforeThrowDieLabels()
            rollDiceButton=Button(root,text='Roll Dice',fg='black',bg='yellow',font=('Tempus Sans ITC',13,'bold'),command=Next)
            rollDiceButton.place(x=175,y=350,width=100,height=40)
            keptDiceLabel=Label(root,text='Kept Dice',fg='white',bg='green',font=('Tempus Sans ITC',15,'bold'))
            keptDiceLabel.place(x=50,y=450,width=350,height=40)
            buttons()
        if(throwNumber>5 and throwNumber<=8):
            background()
            scorecard()
            ### Dice Rolls ###
            player2TurnName.set(player2Name.get()+f'\'s Turn')
            throwText=f'Click the Dice you want to keep. In the kept Dice, click the\nDice you want to remove from the kept Dice. In the\nscorecard, click the highlighted field to add as your score.\nYou have {8-throwNumber} throw(s) left.'
            player2Throw.set(throwText)
            player2TurnLabel=Label(root,textvariable=player2TurnName,fg='white',bg='green',font=('Tempus Sans ITC',20,'bold'))
            player2TurnLabel.place(x=100,y=50,width=250,height=50)
            player2ThrowLabel=Label(root,textvariable=player2Throw,fg='black',bg='cyan',font=('Tempus Sans ITC',10))
            player2ThrowLabel.place(x=50,y=130,width=350,height=80)
            rollDiceButton=Button(root,text='Roll Dice',fg='black',bg='yellow',font=('Tempus Sans ITC',13,'bold'),command=Next)
            rollDiceButton.place(x=175,y=350,width=100,height=40)
            if(throwNumber==8):
                rollDiceLabel=Label(root,text='Roll Dice',fg='grey',bg='yellow',font=('Tempus Sans ITC',13,'bold'))
                rollDiceLabel.place(x=175,y=350,width=100,height=40)
            keptDiceLabel=Label(root,text='Kept Dice',fg='white',bg='green',font=('Tempus Sans ITC',15,'bold'))
            keptDiceLabel.place(x=50,y=450,width=350,height=40)
            buttons()
            def keptDice(number):
                play.keepDie(number,keptNumbers,throw)
                dice()
            def removeDice(number):
                play.removeDie(number,throw,keptNumbers)
                dice()
            for i in range(len(throw)):
                if(throw[i]==1):
                    dieImageButton=Button(root,image=dieOneImage,command=lambda : keptDice(1))
                    dieImageButton.place(x=(100+i*50),y=275)
                if(throw[i]==2):
                    dieImageButton=Button(root,image=dieTwoImage,command=lambda : keptDice(2))
                    dieImageButton.place(x=(100+i*50),y=275)
                if(throw[i]==3):
                    dieImageButton=Button(root,image=dieThreeImage,command=lambda : keptDice(3))
                    dieImageButton.place(x=(100+i*50),y=275)
                if(throw[i]==4):
                    dieImageButton=Button(root,image=dieFourImage,command=lambda : keptDice(4))
                    dieImageButton.place(x=(100+i*50),y=275)
                if(throw[i]==5):
                    dieImageButton=Button(root,image=dieFiveImage,command=lambda : keptDice(5))
                    dieImageButton.place(x=(100+i*50),y=275)
                if(throw[i]==6):
                    dieImageButton=Button(root,image=dieSixImage,command=lambda : keptDice(6))
                    dieImageButton.place(x=(100+i*50),y=275)
            for j in range(len(keptNumbers)):
                if(keptNumbers[j]==1):
                    keptDieImageButton=Button(root,image=dieOneImage,command=lambda : removeDice(1))
                    keptDieImageButton.place(x=(100+j*50),y=520)
                if(keptNumbers[j]==2):
                    keptDieImageButton=Button(root,image=dieTwoImage,command=lambda : removeDice(2))
                    keptDieImageButton.place(x=(100+j*50),y=520)
                if(keptNumbers[j]==3):
                    keptDieImageButton=Button(root,image=dieThreeImage,command=lambda : removeDice(3))
                    keptDieImageButton.place(x=(100+j*50),y=520)
                if(keptNumbers[j]==4):
                    keptDieImageButton=Button(root,image=dieFourImage,command=lambda : removeDice(4))
                    keptDieImageButton.place(x=(100+j*50),y=520)
                if(keptNumbers[j]==5):
                    keptDieImageButton=Button(root,image=dieFiveImage,command=lambda : removeDice(5))
                    keptDieImageButton.place(x=(100+j*50),y=520)
                if(keptNumbers[j]==6):
                    keptDieImageButton=Button(root,image=dieSixImage,command=lambda : removeDice(6))
                    keptDieImageButton.place(x=(100+j*50),y=520)
            player2Score()

    if(play.scoreList[15][0]!='x' and play.scoreList[15][1]!='x'):    # Game finish Condition
        background()
        scorecard()
        a,b=play.__repr__()
        result.set(a)
        recordText.set(b)
        resultLabel=Label(root,textvariable=result,fg='yellow',bg='green',font=('Tempus Sans ITC',20,'bold'))
        resultLabel.place(x=25,y=150,width=400,height=200)
        recordLabel=Label(root,textvariable=recordText,fg='yellow',bg='green',font=('Tempus Sans ITC',20,'bold'))
        recordLabel.place(x=25,y=350,width=400,height=100)    
        buttons()
    turnCount=turnCount+1

## Start Game ##
def startGame():
    background()
    ### Entries ###
    player1NameLabel=Label(root,text='Player 1 Name :',fg='white',bg='green',font=('Tempus Sans ITC',14,'bold'))
    player1NameLabel.place(x=280,y=150,width=150,height=50)
    player1NameEntry=Entry(root,textvariable=player1Name,font=('Tempus Sans ITC',14),relief=GROOVE)
    player1NameEntry.place(x=450,y=150,width=250,height=50)
    player1Name.set('Player 1')
    player2NameLabel=Label(root,text='Player 2 Name :',fg='white',bg='green',font=('Tempus Sans ITC',14,'bold'))
    player2NameLabel.place(x=280,y=230,width=150,height=50)
    player2NameEntry=Entry(root,textvariable=player2Name,font=('Tempus Sans ITC',14),relief=GROOVE)
    player2NameEntry.place(x=450,y=230,width=250,height=50)
    player2Name.set('Player 2')
    ### Buttons ###
    nextButton=Button(root,text='Next',font=('Tempus Sans ITC',13,'bold'),command=Next,relief=GROOVE)
    nextButton.place(x=440,y=610,width=150,height=40)
    buttons()

## Main Menu ##
def mainMenu():
    global throwNumber,turnCount
    
    throwNumber=0
    turnCount=0

    background()

    ### Labels ###
    openLabel=Label(root,text='YAHTZEE\n\n\n',fg='white',bg='green',font=('Tempus Sans ITC',100,'bold'))
    openLabel.place(x=0,y=0,width=1000,height=700)
    openSixImageLabel=Label(root,image=openSixImage)
    openSixImageLabel.place(x=220,y=180)
    openTwoImageLabel=Label(root,image=openTwoImage)
    openTwoImageLabel.place(x=345,y=180)
    openFourImageLabel=Label(root,image=openFourImage)
    openFourImageLabel.place(x=470,y=180)
    openOneImageLabel=Label(root,image=openOneImage)
    openOneImageLabel.place(x=595,y=180)
    openThreeImageLabel=Label(root,image=openThreeImage)
    openThreeImageLabel.place(x=720,y=180)
    fullTime=StringVar()
    fullTime.set(time.asctime())
    fullTimeLabel=Label(root,textvariable=fullTime,fg='white',bg='green',font=('Tempus Sans ITC',10,'bold'))
    fullTimeLabel.place(x=25,y=625,width=200,height=40)
    # Buttons #
    startGameButton=Button(root,text='Start Game',font=('Tempus Sans ITC',13,'bold'),command=startGame,relief=GROOVE)
    startGameButton.place(x=425,y=330,width=150,height=40)
    bestScoresButton=Button(root,text='Best Scores',font=('Tempus Sans ITC',13,'bold'),command=bestScores,relief=GROOVE)
    bestScoresButton.place(x=425,y=390,width=150,height=40)
    rulesButton=Button(root,text='Rules',font=('Tempus Sans ITC',13,'bold'),command=rules,relief=GROOVE)
    rulesButton.place(x=425,y=450,width=150,height=40)
    creditsButton=Button(root,text='Credits',font=('Tempus Sans ITC',13,'bold'),command=Credits,relief=GROOVE)
    creditsButton.place(x=425,y=510,width=150,height=40)
    quitButton=Button(root,text='Quit',font=('Tempus Sans ITC',13,'bold'),command=Quit,relief=GROOVE)
    quitButton.place(x=425,y=570,width=150,height=40)



### Quit Game ###
def quitGame():
    if(messagebox.askyesno('Quit Game',message='Are you sure you want to quit the game?')):
        mainMenu()



### Best Scores ###
def bestScores():
    global name1,score1,date1,name2,score2,date2,name3,score3,date3,name4,score4,date4,name5,score5,date5
    
    background()

    ### Labels ###
    bestScoresLabel=Label(root,text='Best Scores',fg='white',bg='green',font=('Tempus Sans ITC',25,'bold'))
    bestScoresLabel.place(x=400,y=60,width=200,height=50)
    nameLabel=Label(root,text='Name',fg='black',bg='white',font=('Tempus Sans ITC',15,'bold'),relief=GROOVE)
    nameLabel.place(x=200,y=160,width=200,height=60)
    scoreLabel=Label(root,text='Score',fg='black',bg='white',font=('Tempus Sans ITC',15,'bold'),relief=GROOVE)
    scoreLabel.place(x=400,y=160,width=200,height=60)
    dateLabel=Label(root,text='Date',fg='black',bg='white',font=('Tempus Sans ITC',15,'bold'),relief=GROOVE)
    dateLabel.place(x=600,y=160,width=200,height=60)
    recordList=Record.access()
    name1.set(recordList[0][0])
    score1.set(recordList[0][1])
    date1.set(recordList[0][2])
    Name1Label=Label(root,textvariable=name1,fg='black',bg='white',font=('Tempus Sans ITC',12,'bold'),relief=GROOVE)
    Name1Label.place(x=200,y=220,width=200,height=40)
    Score1Label=Label(root,textvariable=score1,fg='black',bg='white',font=('Tempus Sans ITC',12,'bold'),relief=GROOVE)
    Score1Label.place(x=400,y=220,width=200,height=40)
    Date1Label=Label(root,textvariable=date1,fg='black',bg='white',font=('Tempus Sans ITC',12,'bold'),relief=GROOVE)
    Date1Label.place(x=600,y=220,width=200,height=40)
    name2.set(recordList[1][0])
    score2.set(recordList[1][1])
    date2.set(recordList[1][2])
    Name2Label=Label(root,textvariable=name2,fg='black',bg='white',font=('Tempus Sans ITC',12,'bold'),relief=GROOVE)
    Name2Label.place(x=200,y=260,width=200,height=40)
    Score2Label=Label(root,textvariable=score2,fg='black',bg='white',font=('Tempus Sans ITC',12,'bold'),relief=GROOVE)
    Score2Label.place(x=400,y=260,width=200,height=40)
    Date2Label=Label(root,textvariable=date2,fg='black',bg='white',font=('Tempus Sans ITC',12,'bold'),relief=GROOVE)
    Date2Label.place(x=600,y=260,width=200,height=40)
    name3.set(recordList[2][0])
    score3.set(recordList[2][1])
    date3.set(recordList[2][2])
    Name3Label=Label(root,textvariable=name3,fg='black',bg='white',font=('Tempus Sans ITC',12,'bold'),relief=GROOVE)
    Name3Label.place(x=200,y=300,width=200,height=40)
    Score3Label=Label(root,textvariable=score3,fg='black',bg='white',font=('Tempus Sans ITC',12,'bold'),relief=GROOVE)
    Score3Label.place(x=400,y=300,width=200,height=40)
    Date3Label=Label(root,textvariable=date3,fg='black',bg='white',font=('Tempus Sans ITC',12,'bold'),relief=GROOVE)
    Date3Label.place(x=600,y=300,width=200,height=40)
    name4.set(recordList[3][0])
    score4.set(recordList[3][1])
    date4.set(recordList[3][2])
    Name4Label=Label(root,textvariable=name4,fg='black',bg='white',font=('Tempus Sans ITC',12,'bold'),relief=GROOVE)
    Name4Label.place(x=200,y=340,width=200,height=40)
    Score4Label=Label(root,textvariable=score4,fg='black',bg='white',font=('Tempus Sans ITC',12,'bold'),relief=GROOVE)
    Score4Label.place(x=400,y=340,width=200,height=40)
    Date4Label=Label(root,textvariable=date4,fg='black',bg='white',font=('Tempus Sans ITC',12,'bold'),relief=GROOVE)
    Date4Label.place(x=600,y=340,width=200,height=40)
    name5.set(recordList[4][0])
    score5.set(recordList[4][1])
    date5.set(recordList[4][2])
    Name5Label=Label(root,textvariable=name5,fg='black',bg='white',font=('Tempus Sans ITC',12,'bold'),relief=GROOVE)
    Name5Label.place(x=200,y=380,width=200,height=40)
    Score5Label=Label(root,textvariable=score5,fg='black',bg='white',font=('Tempus Sans ITC',12,'bold'),relief=GROOVE)
    Score5Label.place(x=400,y=380,width=200,height=40)
    Date5Label=Label(root,textvariable=date5,fg='black',bg='white',font=('Tempus Sans ITC',12,'bold'),relief=GROOVE)
    Date5Label.place(x=600,y=380,width=200,height=40)
    ### Buttons ###
    backButton=Button(root,text='Back',font=('Tempus Sans ITC',13,'bold'),command=mainMenu,relief=GROOVE)
    backButton.place(x=620,y=610,width=150,height=40)
    quitButton=Button(root,text='Quit',font=('Tempus Sans ITC',13,'bold'),command=Quit,relief=GROOVE)
    quitButton.place(x=800,y=610,width=150,height=40)



### Rules ###
def rules():
    background()

    ### Labels ###
    rulesLabel=Label(root,text='Rules',fg='white',bg='green',font=('Tempus Sans ITC',25,'bold'))
    rulesLabel.place(x=400,y=60,width=200,height=50)
    openText=Text(root,fg='black',bg='white',font=('Tempus Sans ITC',12))
    openText.insert(END,'It is a 2-player game. During a player’s turn, there are maximum 3 throws in 1 turn. During the first throw, he rolls 5 Dice and chose the number(s), he wants to keep. If he keeps the numbers of all 5 Dice, then he does not take the remaining throws. If he keeps the numbers of less than 5 Dice, then there is a choice for him to take the further throws or not. Then, he place the numbers in any of highlighted fields in the scorecard, which will be added to his score. The other player does the same thing in his turn. Both the players keep on playing until all of their score locations are not filled. There are 6 divisions in the upper section of the table; first for “Ones”, having the sum of all 1s in the turn, second for “Twos”, having the sum of all 2s in the turn, third for “Threes”, having the sum of all 3s in the turn, fourth for “Fours”, having the sum of all 4s in the turn, fifth for “Fives” having the sum of all 5s in the turn, sixth for “Sixes”, having the sum of all 6 in the turn. The seventh division is of “Sum”. Here, the total sum of upper divisions is noted. The eighth division is of “Bonus”. It is marked as 35, if the Sum is 35 or more. The ninth division is of “Three of a Kind”. It is marked equal to total of kept numbers if the kept numbers contain at least 3 numbers of same kind. The tenth division is of “Four of a Kind”. It is marked equal to total of kept numbers if the kept numbers contain at least 4 numbers of same kind. The eleventh division is of “Full House”. It is marked as 25, if kept numbers contain a Two of a Kind and a Three of a Kind. The twelfth division is of “Small straight”. It is marked as 30, if the kept numbers contain at least 4 numbers in sequence. The thirteenth division is of “Large straight”. It is marked as 40, if the all the kept numbers are in sequence. The fourteenth division is of “Chance”. It is marked equal to total of kept numbers and remaining numbers. The fifteenth division is of “YAHTZEE”. It is marked as 50, if all the kept numbers are making Five of a Kind. The fifteenth and the last division is of “Total Score’. It is filled with the total of Sum, Bonus, Three of a Kind, Four of a Kind, Full House, Small straight, Large straight and Yahtzee. When the scorecard is completely filled, then the Player having the highest Total Score, wins the YAHTZEE. If the Total Scores of both the Players are equal, then YAHTZEE ends in Draw.')
    openText.place(x=100,y=140,width=800,height=405)
    ### Buttons ###
    backButton=Button(root,text='Back',font=('Tempus Sans ITC',13,'bold'),command=mainMenu,relief=GROOVE)
    backButton.place(x=620,y=610,width=150,height=40)
    quitButton=Button(root,text='Quit',font=('Tempus Sans ITC',13,'bold'),command=Quit,relief=GROOVE)
    quitButton.place(x=800,y=610,width=150,height=40)



### Credits ###
def Credits():
    background()
    ### Labels ###
    developedByLabel=Label(root,text='Developed by',fg='white',bg='green',font=('Tempus Sans ITC',25,'bold'))
    developedByLabel.place(x=300,y=60,width=400,height=50)
    myNameLabel=Label(root,text='Muhammad Faseeh Bin Naeem',fg='white',bg='green',font=('Tempus Sans ITC',15,'bold'))
    myNameLabel.place(x=300,y=125,width=400,height=40)
    myRegistrationNumberLabel=Label(root,text='(2018-R/2017-MC-77)',fg='white',bg='green',font=('Tempus Sans ITC',15,'bold'))
    myRegistrationNumberLabel.place(x=300,y=170,width=400,height=40)
    projectSupervisorLabel=Label(root,text='Project Supervisor',fg='white',bg='green',font=('Tempus Sans ITC',25,'bold'))
    projectSupervisorLabel.place(x=300,y=250,width=400,height=50)
    supervisorNameLabel=Label(root,text='Mr. Muhammad Ahsan Naeem',fg='white',bg='green',font=('Tempus Sans ITC',15,'bold'))
    supervisorNameLabel.place(x=300,y=315,width=400,height=40)
    supervisorNameLabel=Label(root,text='Department of Mechatronics and Control Engineering',fg='white',bg='green',font=('Tempus Sans ITC',20,'bold'))
    supervisorNameLabel.place(x=100,y=415,width=800,height=40)
    supervisorNameLabel=Label(root,text='University of Engineering and Technology, Lahore',fg='white',bg='green',font=('Tempus Sans ITC',20,'bold'))
    supervisorNameLabel.place(x=0,y=470,width=1000,height=40)
    ### Buttons ###
    backButton=Button(root,text='Back',font=('Tempus Sans ITC',13,'bold'),command=mainMenu,relief=GROOVE)
    backButton.place(x=620,y=610,width=150,height=40)
    quitButton=Button(root,text='Quit',font=('Tempus Sans ITC',13,'bold'),command=Quit,relief=GROOVE)
    quitButton.place(x=800,y=610,width=150,height=40)



### Quit ###
def Quit():
    if(messagebox.askyesno('Quit',message='Are you sure you want to quit the YAHTZEE?')):
        exit()



### Window ###

root=Tk()
root.title('YAHTZEE')
root.geometry('1000x700+30+30')

## Initialization ##
throwNumber=0
player1Name=StringVar()
player2Name=StringVar()
player1TurnName=StringVar()
player2TurnName=StringVar()
player1Throw=StringVar()
player2Throw=StringVar()
p1Ones=StringVar()
p2Ones=StringVar()
p1Twos=StringVar()
p2Twos=StringVar()
p1Threes=StringVar()
p2Threes=StringVar()
p1Fours=StringVar()
p2Fours=StringVar()
p1Fives=StringVar()
p2Fives=StringVar()
p1Sixes=StringVar()
p2Sixes=StringVar()
p1Sum=StringVar()
p2Sum=StringVar()
p1Bonus=StringVar()
p2Bonus=StringVar()
p1ThreeOfAKind=StringVar()
p2ThreeOfAKind=StringVar()
p1FourOfAKind=StringVar()
p2FourOfAKind=StringVar()
p1FullHouse=StringVar()
p2FullHouse=StringVar()
p1SmallStraight=StringVar()
p2SmallStraight=StringVar()
p1LargeStraight=StringVar()
p2LargeStraight=StringVar()
p1Chance=StringVar()
p2Chance=StringVar()
p1Yahtzee=StringVar()
p2Yahtzee=StringVar()
p1TotalScore=StringVar()
p2TotalScore=StringVar()
result=StringVar()
dieOneImage=PhotoImage(file='1.gif')
dieTwoImage=PhotoImage(file='2.gif')
dieThreeImage=PhotoImage(file='3.gif')
dieFourImage=PhotoImage(file='4.gif')
dieFiveImage=PhotoImage(file='5.gif')
dieSixImage=PhotoImage(file='6.gif')
name1=StringVar()
score1=StringVar()
date1=StringVar()
name2=StringVar()
score2=StringVar()
date2=StringVar()
name3=StringVar()
score3=StringVar()
date3=StringVar()
name4=StringVar()
score4=StringVar()
date4=StringVar()
name5=StringVar()
score5=StringVar()
date5=StringVar()
recordText=StringVar()
turnCount=0

## Main Menu ##
background()
# Labels #
openLabel=Label(root,text='YAHTZEE\n\n\n',fg='white',bg='green',font=('Tempus Sans ITC',100,'bold'))
openLabel.place(x=0,y=0,width=1000,height=700)
openSixImage=PhotoImage(file='Six.gif')
openSixImageLabel=Label(root,image=openSixImage)
openSixImageLabel.place(x=220,y=180)
openTwoImage=PhotoImage(file='Two.gif')
openTwoImageLabel=Label(root,image=openTwoImage)
openTwoImageLabel.place(x=345,y=180)
openFourImage=PhotoImage(file='Four.gif')
openFourImageLabel=Label(root,image=openFourImage)
openFourImageLabel.place(x=470,y=180)
openOneImage=PhotoImage(file='One.gif')
openOneImageLabel=Label(root,image=openOneImage)
openOneImageLabel.place(x=595,y=180)
openThreeImage=PhotoImage(file='Three.gif')
openThreeImageLabel=Label(root,image=openThreeImage)
openThreeImageLabel.place(x=720,y=180)
fullTime=StringVar()
fullTime.set(time.asctime())
fullTimeLabel=Label(root,textvariable=fullTime,fg='white',bg='green',font=('Tempus Sans ITC',10,'bold'))
fullTimeLabel.place(x=25,y=625,width=200,height=40)
# Buttons #
startGameButton=Button(root,text='Start Game',font=('Tempus Sans ITC',13,'bold'),command=startGame,relief=GROOVE)
startGameButton.place(x=425,y=330,width=150,height=40)
bestScoresButton=Button(root,text='Best Scores',font=('Tempus Sans ITC',13,'bold'),command=bestScores,relief=GROOVE)
bestScoresButton.place(x=425,y=390,width=150,height=40)
rulesButton=Button(root,text='Rules',font=('Tempus Sans ITC',13,'bold'),command=rules,relief=GROOVE)
rulesButton.place(x=425,y=450,width=150,height=40)
creditsButton=Button(root,text='Credits',font=('Tempus Sans ITC',13,'bold'),command=Credits,relief=GROOVE)
creditsButton.place(x=425,y=510,width=150,height=40)
quitButton=Button(root,text='Quit',font=('Tempus Sans ITC',13,'bold'),command=Quit,relief=GROOVE)
quitButton.place(x=425,y=570,width=150,height=40)

root.mainloop()