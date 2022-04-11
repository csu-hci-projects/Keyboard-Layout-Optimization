import time

global startTime, endTime

def start(entry):
    global startTime
    
    entry.delete(0, 'end')
    startTime = time.time()

def end(keyboardApp):
    global endTime
    
    endTime = time.time()
    convertTime(endTime- startTime)
    
    keyboardApp.destroy()
    
def convertTime(sec):
    sec = sec % 60
    mins = sec // 60
    mins = mins % 60
    
    print("Time: {0}:{1:0.2f}".format(int(mins),sec))
