import turtle
import Tkinter

class Spiral:
    def __init__(self, deg, color1, color2, color3):
        self.x = 0
        self.deg = deg
        while self.x < 360:
            self.setcolor(color1, color2, color3)
            turtle.width(self.x / 100 + 1)
            turtle.forward(self.x)
            turtle.left(self.deg)
            self.x += 1
    def setcolor(self, color1, color2, color3):
        pass

class ColorSpiral(Spiral):
    def setcolor(self, color1, color2, color3):
        turtle.colors = [color1, color2, color3]
        turtle.pencolor(turtle.colors[self.x % 3])

if __name__ == "__main__":
    go = True
    while go == True:
        print("first color?")
        color1 = raw_input()
        print("second color?")
        color2 = raw_input()
        print("third color?")
        color3 = raw_input()
        print("how many sides?")
        comm = input()
        if type(comm) == int:
            sides = (360/comm) - 1
            spiral = ColorSpiral(sides, color1, color2, color3)
        else:
            print("sorry, I don't know what that means")
