import RPi.GPIO as GPIO

class MotorDriver:
    def __init__(self, pwm1, pwm2, freq = 100):
        # set up the pin 
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(pwm1, GPIO.OUT)
        GPIO.setup(pwm2, GPIO.OUT)

        self.pwm1_pin = pwm1
        self.pwm2_pin = pwm2

        self.pwm_r = GPIO.PWM(pwm1, freq)
        self.pwm_l = GPIO.PWM(pwm2, freq)

        self.pwm_r.start(0)
        self.pwm_l.start(0)


    def move_forward(self, speed):
        self.pwm_r.ChangeDutyCycle(speed)
        self.pwm_l.ChangeDutyCycle(0)

    def move_reverse(self, speed):
        self.pwm_r.ChangeDutyCycle(0)
        self.pwm_l.ChangeDutyCycle(speed)

    def stop_moving(self):
        self.pwm_r.ChangeDutyCycle(0)
        self.pwm_l.ChangeDutyCycle(0)

    def disconnect(self):
        GPIO.cleanup()

