from .component.wheel import *


class RobotControl:
    """
    motor PWM PINS
    motor ENB PINS
    as dict

    {
        "pwm1" : 12,
        "pwm2" : 18,
        "enb1" : 14,
        "enb2" : 15,
    }

    """

    left_right_ratio = 23/25

    def __init__(self, left, right):
        self.left_wheel = MotorDriver(
            left["pwm1"], left["pwm2"], left["enb1"], left["enb2"]
        )
        self.right_wheel = MotorDriver(
            right["pwm1"], right["pwm2"], right["enb1"], right["enb2"]
        )
        self.left_speed = 0
        self.right_speed = 0

    def robot_forward(self, mode: str, speed=20):
        self.right_speed = speed * self.left_right_ratio
        self.left_speed = speed
        self.left_wheel.move_reverse(speed=self.left_speed)
        self.right_wheel.move_forward(speed=self.right_speed)

    def robot_backward(self, speed=25):
        self.right_speed = speed * self.left_right_ratio
        self.left_speed = speed
        self.left_wheel.move_forward(speed=self.left_speed)
        self.right_wheel.move_reverse(speed=self.right_speed)

    def robot_turn_right(self, speed=25):
        self.right_speed = (speed / 2) * self.left_right_ratio
        self.left_speed = speed
        self.left_wheel.move_reverse(speed=self.left_speed)
        self.right_wheel.move_forward(speed=self.right_speed)

    def robot_turn_left(self, speed=25):
        self.right_speed = speed
        self.left_speed = (speed / 2) * self.left_right_ratio
        self.left_wheel.move_forward(speed=self.left_speed)
        self.right_wheel.move_reverse(speed=self.right_speed)

    def robot_pivot_right(self, speed=25):
        self.right_speed = speed * self.left_right_ratio
        self.left_speed = speed
        self.left_wheel.move_reverse(speed=self.left_speed)
        self.right_wheel.move_reverse(speed=self.right_speed)

    def robot_pivot_left(self, speed=25):
        self.right_speed = speed * self.left_right_ratio
        self.left_speed = speed
        self.left_wheel.move_forward(speed=self.left_speed)
        self.right_wheel.move_forward(speed=self.right_speed)

    def robot_left_forward(self, speed=25):
        self.left_speed = speed
        self.left_wheel.move_forward(speed=self.left_speed)

    def robot_left_backward(self, speed=25):
        self.left_speed = speed
        self.left_wheel.move_backward(speed=self.left_speed)

    def robot_right_forward(self, speed=25):    
        self.right_speed = speed
        self.right_wheel.move_forward(speed=self.right_speed)

    def robot_right_backward(self, speed=25):
        self.right_speed = speed
        self.right_wheel.move_backward(speed=self.right_speed)

    # def corection_left(self, offset):
    #     self

    def robot_stop(self):
        self.left_speed = 0
        self.right_speed = 0
        self.left_wheel.stop_moving()
        self.right_wheel.stop_moving()

    def disconnect(self):
        self.left_wheel.disconnect()
        self.right_wheel.disconnect()
