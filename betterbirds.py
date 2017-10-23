import tkinter # Python graphics library
import random

class Bird:
    def __init__(self, canvas):
        self.canvas = canvas
        self.x = random.uniform(0, self.canvas.winfo_width())
        self.y = random.uniform(0, self.canvas.winfo_height())
        self.min_x_speed = int
        self.max_x_speed = int
        self.x_speed = random.uniform(self.min_x_speed, self.max_x_speed)
        self.min_y_speed = int
        self.max_y_speed = int
        self.y_speed = random.uniform(self.min_y_speed, self.max_y_speed)
        self.size = int
        self.fill_color = '#{0:0>6x}'.format(random.randint(00, 16 ** 6))
    def display(self):
        self.canvas.create_oval(self.x, self.y, self.x + self.size * 2,
                                self.y + self.size, fill = self.fill_color)
    def move(self):
        self.x += self.x_speed
        self.y += self.y_speed
        if (self.x > self.canvas.winfo_width()): # if off to right of screen
            self.x = -self.size                  # move to just off left of screen

class SoaringBird(Bird):
    def __init__(self, canvas):
        Bird.__init__(self, canvas)
        self.min_x_speed = 1.0
        self.max_x_speed = 3.0
        self.size = 30.0
        print("Soaring self.x = " + str(self.x) + " self.y = " + str(self.y))

class FlittingBird(Bird):
    def __init__(self, canvas):
        Bird.__init__(self, canvas)
        self.min_x_speed = 2.0
        self.max_x_speed = 5.0
        self.min_y_speed = -1.0
        self.max_y_speed = 1.0
        self.size = 15.0
        print("Flitting self.x = " + str(self.x) + " self.y = " + str(self.y))
    def move(self):
        if (self.y < - self.size or self.y > self.canvas.winfo_height()):
            self.y_speed = -self.y_speed
        if (random.random() > 0.8):
            self.y_speed += random.uniform (-0.5, 0.5)
            self.y_speed = max(self.min_y_speed, self.y_speed)
            self.y_speed = min(self.max_y_speed, self.y_speed)
            self.x_speed += random.uniform (-0.5, 0.5)
            self.x_speed = max(self.min_x_speed, self.x_speed)
            self.x_speed = min(self.max_x_speed, self.x_speed)

class FallingFeather:
    def __init__(self, canvas):
        self.canvas = canvas
        # winfo gets us the current size of the canvas
        self.x = random.uniform(0, self.canvas.winfo_width())
        self.y = random.uniform(-self.canvas.winfo_height(), 0)
        self.x_speed = random.uniform(-1,1)
        self.y_speed = random.uniform(0.5, 1.5)
        self.size = 5.0
        self.fill_color = '#{0:0>6x}'.format(random.randint(00,16**6))
    def display(self):
        self.canvas.create_rectangle(self.x, self.y, self.x + self.size*2, self.y + self.size,
                                     fill=self.fill_color)
    def move(self):
        self.x += self.x_speed
        self.y += self.y_speed
        # if off the bottom of the screen, move to the top
        if (self.y > self.canvas.winfo_height()):
            self.y = -self.size
            # about 5% of the time,
            # or if going off the left or right of the screen,
            # reverse x direction
        if (random.random() > 0.95 or self.x < -self.size or self.x > self.canvas.winfo_width()):
            self.x_speed = -self.x_speed

if __name__ == '__main__':
    # create the graphics root and a 400x400 canvas
    root = tkinter.Tk()
    canvas = tkinter.Canvas(root, width=600, height=400)
    canvas.pack()
    canvas.update() # need this for the canvas object to have the correct height set
    sb = []
    for i in range (0, 4):
        sb.append(SoaringBird(canvas))
    fb = []
    for i in range(0, 4):
        fb.append(FlittingBird(canvas))
    ff = []
    for i in range(0, 9):
        ff.append(FallingFeather(canvas))
    # define the draw loop
    delay = 33 # milliseconds, so about 30 frames per second
    def draw():
        canvas.delete(tkinter.ALL)
        for x in sb:
            x.move()
            x.display()
        for x in fb:
            x.move()
            x.display()
        for x in ff:
            x.move()
            x.display()
        # delay = 33 # milliseconds, so about 30 frames per second
        canvas.after(delay, draw) # call this draw function again after the delay
    # start the draw loop
    draw()
    canvas.after(delay, draw)
    root.mainloop() # keep the window open
