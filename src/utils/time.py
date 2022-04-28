import time

global startTime, endTime, user
enable = False

def start(entry):
    global startTime, enable
    
    if (enable == False):
        enable = True
        entry.delete(0, 'end')
        startTime = time.time()

def setUser(newuser):
    global user 
    user = newuser


def end(keyboardApp, keyboardLayout, inputTxt, testTxt):
    global startTime
    global endTime
    
    endTime = time.time()
    
    statistics(endTime-startTime, keyboardLayout, inputTxt, testTxt)
    closeApp(keyboardApp)
    
    
def closeApp(keyboardApp):
    global startTime
    global endTime
    global enable
    
    enable = False
    startTime=0
    endTime=0
    keyboardApp.destroy()
    
def statistics(recordedTime, keyboardLayout, inputTxt, testTxt):
    print('-----{}-----'.format(keyboardLayout))
    print('Error Rate', textData(inputTxt, testTxt))
    convertTime(recordedTime)

def convertTime(sec):
    sec = sec % 60
    print("Time: {0} Sec".format(sec))
    
def textData(inputTxt, testTxt):
    global user
    print('User:{}'.format(user))
    print('Text:{}'.format(testTxt))
    print('Input:{}'.format(inputTxt))
    
    return errorRate(inputTxt, testTxt)

def errorRate(inputTxt, testTxt):
    correct = 0
    mismatch = 0

    if (len(inputTxt) <= len(testTxt)):
        mismatch = len(testTxt)
        inputTxt = inputTxt[0:len(testTxt)]
        for i, char in enumerate(inputTxt):
            if (char == testTxt[i]):
                correct += 1
                mismatch -= 1
              
        print('Correct: ', correct)
        print('In-correct: ', mismatch)
        
        return (1 - correct/len(testTxt)) * 100
    else:
        mismatch = len(testTxt)
        for i, char in enumerate(testTxt):
            if (char == inputTxt[i]):
                correct += 1
                mismatch -= 1
        
        print('Correct: ', correct)
        print('In-correct: ', mismatch)
        
        return (1 - correct/len(testTxt)) * 100