import time

global startTime, endTime
enable = False

def start(entry):
    global startTime, enable
    
    if (enable == False):
        enable = True
        entry.delete(0, 'end')
        startTime = time.time()

def end(keyboardApp, keyboardLayout, inputTxt, testTxt):
    global endTime
    
    endTime = time.time()
    statistics(endTime-startTime, keyboardLayout, inputTxt, testTxt)
    
    keyboardApp.destroy()
    
    
def statistics(recordedTime, keyboardLayout, inputTxt, testTxt):
    print('-----{}-----'.format(keyboardLayout))
    print('Error Rate', textData(inputTxt, testTxt))
    convertTime(recordedTime)

def convertTime(sec):
    sec = sec % 60
    mins = sec // 60
    mins = mins % 60
    
    print("Time: {0}:{1:0.2f}".format(int(mins),sec))
    
def textData(inputTxt, testTxt):
    print('Text: {}'.format(testTxt))
    print('Input: {}'.format(inputTxt))
    
    return errorRate(inputTxt, testTxt)

def errorRate(inputTxt, testTxt):
    correct = 0
    mismatch = 0
    
    if (len(inputTxt) <= len(testTxt)):
        mismatch = len(testTxt)
        for i, char in enumerate(inputTxt):
            if (char == testTxt[i]):
                correct += 1
                mismatch -= 1
            # else:
                
        print('Correct: ', correct)
        print('In-correct: ', mismatch)
        
        return correct/len(testTxt)
    else:
        mismatch = len(inputTxt)
        for i, char in enumerate(testTxt):
            if (char == inputTxt[i]):
                correct += 1
                mismatch -= 1
            # else:
                
        print('Correct: ', correct)
        print('In-correct: ', mismatch)
        
        return correct/len(testTxt)