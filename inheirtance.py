import turtle
import Tkinter

class Spiral:
    def __init__(self):
        self.x = 0
        while self.x < 360:
            self.setcolor()
            turtle.width(self.x / 100 + 1)
            turtle.forward(self.x)
            turtle.left(59)
            self.x += 1
    def setcolor(self):
        pass

class RainbowSpiral(Spiral):
    def setcolor(self):
        turtle.colors = ['red', 'purple', 'blue', 'green', 'yellow', 'orange']
        turtle.pencolor(turtle.colors[self.x % 6])

class CoolSpiral(Spiral):
    def setcolor(self):
        turtle.colors = ['purple', 'blue', 'green']
        turtle.pencolor(turtle.colors[self.x % 3])

class WarmSpiral(Spiral):
    def setcolor(self):
        turtle.colors = ['red', 'orange', 'yellow']
        turtle.pencolor(turtle.colors[self.x % 3])

if __name__ == "__main__":
    print("rainbow, cool, warm, or none?")
    comm = raw_input()
    if comm == "rainbow":
        rainbow = RainbowSpiral()
    elif comm == "cool":
        cool = CoolSpiral()
    elif comm == "warm":
        warm = WarmSpiral()
    elif comm == "none":
        spiral = Spiral()
    else:
        print("sorry, I don't know what that means")
