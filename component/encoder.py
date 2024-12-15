import RPi.GPIO as GPIO

class Encoder:

    def __init__(self, leftPin, rightPin, callback=None):
        self.leftPin = leftPin
        self.rightPin = rightPin
        self.value = 0
        self.state = '00'   
        self.direction = None
        self.callback = callback
        GPIO.setup(self.leftPin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.setup(self.rightPin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.add_event_detect(self.leftPin, GPIO.BOTH, callback=self.transitionOccurred)  
        GPIO.add_event_detect(self.rightPin, GPIO.BOTH, callback=self.transitionOccurred)  

    def transitionOccurred(self, channel):
        p1 = GPIO.input(self.leftPin)
        p2 = GPIO.input(self.rightPin)
        newState = "{}{}".format(p1, p2)

        if self.state == "00": # Resting position
            if newState == "01": # Turned right 1
                self.value = self.value + 1
            elif newState == "10": # Turned left 1
                self.value = self.value + 1

        elif self.state == "01": # R1 or L3 position
            if newState == "11": # Turned right 1
                self.value = self.value + 1
            elif newState == "00": # Turned left 1
                self.value = self.value + 1

        elif self.state == "10": # R3 or L1
            if newState == "11": # Turned left 1
                self.value = self.value + 1
            elif newState == "00": # Turned right 1
                self.value = self.value + 1

        else: # self.state == "11"
            if newState == "01": # Turned left 1
                self.value = self.value + 1
            elif newState == "10": # Turned right 1
                self.value = self.value + 1
            elif newState == "00": # Skipped an intermediate 01 or 10 state, but if we know direction then a turn is complete
                self.value = self.value + 1
                
        self.state = newState

    def getValue(self):
        return self.value