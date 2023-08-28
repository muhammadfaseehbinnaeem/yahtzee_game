from random import randint
import time

class Yahtzee:
    def __init__(self,p1Name,p2Name):
        self.p1Name=p1Name
        self.p2Name=p2Name
        self.scoreList=[['x','x'],['x','x'],['x','x'],['x','x'],['x','x'],['x','x'],['x','x'],['x','x'],['x','x'],['x','x'],['x','x'],['x','x'],['x','x'],['x','x'],['x','x'],['x','x']]

    ### Getters & Setters ###
    @property
    def p1Name(self):
        return self._p1Name
    @p1Name.setter
    def p1Name(self,newName):
        if(newName=='Player 1'):
            self._p1Name=newName
        else: 
            self._p1Name=newName.split(' ')[0]
    @property
    def p2Name(self):
        return self._p2Name
    @p2Name.setter
    def p2Name(self,newName):
        if(newName=='Player 2'):
            self._p2Name=newName
        else: 
            self._p2Name=newName.split(' ')[0]

    ### Instance Methods ###
    def throw(self,keptNumbers):    # Throw
        return [randint(1,6) for i in range(5-(len(keptNumbers)))]
    def keepDie(self,number,keptNumbers,throw):    # Appends the number in Kept numbers and removes the number from Throw
        keptNumbers.append(number)
        throw.remove(number)
    def removeDie(self,number,throw,keptNumbers):    # Appends the number in Throw and removes the number from Kept numbers
        throw.append(number)
        keptNumbers.remove(number)
    def ofKind(self,keptNumbers):       # of a Kind (Three of a Kind, Four of a Kind, Full House, YAHTZEE)
        store=0
        kind=0
        a=0
        b=0
        for i in keptNumbers:
            kind=keptNumbers.count(i)
            if(kind==2):
                a=2
            if(kind==3):
                store=3
                b=3
            if(kind==4):
                store=4
            if(kind==5):
                store=5
        if(store==3 and a!=2):      # Three of a Kind
            return f'threeOfAKind'
        if(store==4):       # Four of a Kind
            return f'fourOfAKind'
        if(a==2 and b==3):      # Full House
            return 'fullHouse'
        if(store==5):       # YAHTZEE
            return 'yahtzee'
    def smallStraight(self,keptNumbers):        # Small staright
        keptNumbersList=list(set(keptNumbers))
        keptNumbersList.sort()
        for i in range(len(keptNumbersList)):
            if(i==0):
                store=keptNumbersList[i]
            else:
                store=store+1
                if(i==3 and keptNumbersList[i]==store):
                    return True
    def largeStraight(self,keptNumbers):        # Large staright
        keptNumbersList=list(set(keptNumbers))
        keptNumbersList.sort()
        for i in range(len(keptNumbersList)):
            if(i==0):
                store=keptNumbersList[i]
            else:
                store=store+1
                if(i==4 and keptNumbersList[i]==store):
                    return True
    
    ### Magic Methods ###
    def __repr__(self):
        recordList=Record.access()
        if(int(self.scoreList[15][0])>int(self.scoreList[15][1])):    # Player 1 Win Condition
            resultStatement=f'{self.p1Name} won the YAHTZEE.\n\nCongratulations, {self.p1Name}!'
            if(int(self.scoreList[15][0])>=int(recordList[4][1])):
                recordStatement=f'Woohoo, You set a Record!!'
                recordList.pop(4)
                recordList.append([self.p1Name,self.scoreList[15][0],time.asctime().split(' ')[1]+f' '+time.asctime().split(' ')[2]+f', '+time.asctime().split(' ')[4]])
                recordList.sort(reverse=True,key=lambda x: int(x[1]))
            else:
                recordStatement=' '
        if(int(self.scoreList[15][1])>int(self.scoreList[15][0])):    # Player 2 Win Condition
            resultStatement=f'{self.p2Name} won the YAHTZEE.\n\nCongratulations, {self.p2Name}!'
            if(int(self.scoreList[15][1])>=int(recordList[4][1])):
                recordStatement=f'Woohoo, You set a Record!!'
                recordList.pop(4)
                recordList.append([self.p2Name,self.scoreList[15][1],time.asctime().split(' ')[1]+f' '+time.asctime().split(' ')[2]+f', '+time.asctime().split(' ')[4]])
                recordList.sort(reverse=True,key=lambda x: int(x[1]))
            else:
                recordStatement=' '
        if(int(self.scoreList[15][0])==int(self.scoreList[15][1])):    # Draw Condition
            resultStatement=f'YAHTZEE ended in Draw.\n\nWell Played, both Players!'
            recordStatement=' '
        Record.update(recordList)
        return resultStatement,recordStatement

class Record:
    def access():    # Accesses the records textfile into a list
        record=open('records.txt','r')
        List=[]
        for r in record:
            r=r.strip('\n').split('\t')
            List.append(r)
        record.close()
        return List
    def update(List):    # Updates the records textfile
        recordWrite=open('records.txt','w')
        recordWrite.write(f'{List[0][0]}\t{List[0][1]}\t{List[0][2]}\n')
        recordWrite.write(f'{List[1][0]}\t{List[1][1]}\t{List[1][2]}\n')
        recordWrite.write(f'{List[2][0]}\t{List[2][1]}\t{List[2][2]}\n')
        recordWrite.write(f'{List[3][0]}\t{List[3][1]}\t{List[3][2]}\n')
        recordWrite.write(f'{List[4][0]}\t{List[4][1]}\t{List[4][2]}\n')
        recordWrite.close()