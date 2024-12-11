from fastapi import FastAPI
import time
from robot import *

app = FastAPI()

left = {
    "pwm1" : 12,
    "pwm2" : 13,
    "enb1" : 5,
    "enb2" : 6,
}

right = {
    "pwm1" : 18,
    "pwm2" : 19,
    "enb1" : 20,
    "enb2" : 21,
}

robot = RobotControl(left, right)

@app.get("/move-forward/{speed}")
def move_forward(speed: int):
    robot.robot_forward(speed)

@app.get("/move-forward-a-moment/{second}/{speed}")
def move_forward_a_moment(second: int, speed: int):
    robot.robot_forward(speed)
    time.sleep(second)
    robot.robot_stop()

@app.get("/move-backward/{speed}")
def move_backward(speed: int):
    robot.robot_backward(speed)

@app.get("/move-backward-a-moment/{second}/{speed}")
def move_backward_a_moment(second: int, speed: int):
    robot.robot_backward(speed)
    time.sleep(second)
    robot.robot_stop()

@app.get("/turn-left/{speed}")
def turn_left(speed: int):
    robot.robot_turn_left(speed)

@app.get("/turn-left-a-moment/{second}/{speed}")
def turn_left_a_moment(second:int, speed:int):
    robot.robot_turn_left(speed)
    time.sleep(second)
    robot.robot_stop()

@app.get("/turn-right/{speed}")
def turn_right(speed: int):
    robot.robot_turn_right(speed)

@app.get("/turn-right-a-moment/{second}/{speed}")
def turn_right_a_moment(second:int, speed:int):
    robot.robot_turn_right(speed)
    time.sleep(second)
    robot.robot_stop()

@app.get("/pivot-left/{speed}")
def pivot_left(speed: int):
    robot.robot_pivot_left(speed)

@app.get("/pivot-right/{speed}")
def pivot_right(speed: int):
    robot.robot_pivot_right(speed)

@app.get("/left-forward/{speed}")
def left_forward(speed: int):
    robot.robot_left_forward(speed=speed)

@app.get("/left-backward/{speed}")
def left_backward(speed: int):
    robot.robot_left_backward(speed=speed)

@app.get("/right-forward/{speed}")
def right_forward(speed: int):
    robot.robot_right_forward(speed=speed)

@app.get("/right-backward/{speed}")
def right_backward(speed: int):
    robot.robot_right_backward(speed=speed)

@app.get("/stop")
def stop():
    robot.robot_stop()