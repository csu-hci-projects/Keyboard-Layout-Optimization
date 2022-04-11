import time

global startTime, endTime

def start(entry):
    global startTime
    
    entry.delete(0, 'end')
    startTime = time.time()

def end(keyboardApp, keyboardLayout, inputTxt, testTxt):
    global endTime
    
    endTime = time.time()
    statistics(endTime- startTime, keyboardLayout, inputTxt, testTxt)
    
    keyboardApp.destroy()
    
    
def statistics(recordedTime, keyboardLayout, inputTxt, testTxt):
    print('-----{}-----'.format(keyboardLayout))
    convertTime(recordedTime)
    textData(inputTxt, testTxt)



def convertTime(sec):
    sec = sec % 60
    mins = sec // 60
    mins = mins % 60
    
    print("Time: {0}:{1:0.2f}".format(int(mins),sec))
    
def textData(inputTxt, testTxt):
    print('Text: {}'.format(testTxt))
    print('Input: {}'.format(inputTxt))
    
    ER = errorRate(inputTxt, testTxt)

def errorRate(inputTxt, testTxt):
    correct = 0
    for x,y in inputTxt, testTxt:
        if (x == y):
            correct += 1
        