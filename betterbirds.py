import tkinter # Python graphics library
import random # for generating random numbers

class Bird:
    # define things both child classes will have: canvas, x, y, and fill_color
    def __init__(self, canvas):
        self.canvas = canvas
        self.x = random.uniform(0, self.canvas.winfo_width()) # random start
        self.y = random.uniform(0, self.canvas.winfo_height())
        self.fill_color = '#{0:0>6x}'.format(random.randint(00, 16 ** 6)) # random color
    # define what the birds look like
    def display(self):
        self.canvas.create_oval(self.x, self.y, self.x + self.size * 2,
                                self.y + self.size, fill = self.fill_color)

class SoaringBird(Bird):
    # define more specific aspects of SoaringBird
    def __init__(self, canvas):
        Bird.__init__(self, canvas) # based on parent class Bird
        self.min_x_speed = 1.0 # specific movement parameters
        self.max_x_speed = 3.0
        self.x_speed = random.uniform(self.min_x_speed, self.max_x_speed)
        self.size = 30.0 # specific size
    # define how SoaringBird moves
    # not in Bird because it's different from FlittingBird
    # and because I couldn't get it to work when they were inherited
    def move(self):
        self.x += self.x_speed
        if (self.x > self.canvas.winfo_width()): # if off to right of screen
            self.x = -self.size                  # move to just off left of screen

class FlittingBird(Bird):
    # define more specific aspects of FlittingBird
    def __init__(self, canvas):
        Bird.__init__(self, canvas) # based on parent class Bird
        self.min_x_speed = 2.0 # specific movement parameters
        self.max_x_speed = 5.0
        self.x_speed = random.uniform(self.min_x_speed, self.max_x_speed)
        self.min_y_speed = -1.0 # FlittingBird also has a y parameter
        self.max_y_speed = 1.0
        self.y_speed = random.uniform(self.min_y_speed, self.max_y_speed)
        self.size = 15.0 # specific size
    # define how FlittingBird moves
    # not in Bird because it's different from SoaringBird
    # and because I couldn't get it to work when they were inherited
    def move(self):
        self.x += self.x_speed
        self.y += self.y_speed
        if (self.x > self.canvas.winfo_width()): # if off to right of screen
            self.x = -self.size                  # move to just off left of screen
        if (self.y < - self.size or self.y > self.canvas.winfo_height()):
            self.y_speed = -self.y_speed # if on top or bottom, reverse y speed
        if (random.random() > 0.8): # about 20% of the time
            self.y_speed += random.uniform (-0.5, 0.5) # change speed a bit
            self.y_speed = max(self.min_y_speed, self.y_speed)
            self.y_speed = min(self.max_y_speed, self.y_speed)
            self.x_speed += random.uniform (-0.5, 0.5)
            self.x_speed = max(self.min_x_speed, self.x_speed)
            self.x_speed = min(self.max_x_speed, self.x_speed)

class FallingFeather:
    # define how FallingFeather works
    # I couldn't really simplify this part much
    def __init__(self, canvas):
        self.canvas = canvas
        # winfo gets us the current size of the canvas
        self.x = random.uniform(0, self.canvas.winfo_width()) # random start
        self.y = random.uniform(-self.canvas.winfo_height(), 0)
        self.x_speed = random.uniform(-1, 1) # random speeds
        self.y_speed = random.uniform(0.5, 1.5)
        self.size = 5.0
        self.fill_color = '#{0:0>6x}'.format(random.randint(00,16**6)) # random color
    # define what FallingFeather looks like
    def display(self):
        self.canvas.create_rectangle(self.x, self.y, self.x + self.size*2, self.y + self.size,
                                     fill=self.fill_color)
    # define how FallingFeather moves
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
    sb = [] # a list for instances of SoaringBird
    for i in range (0, 4):
        sb.append(SoaringBird(canvas))
    fb = [] # a list for instances of FlittingBird
    for i in range(0, 4):
        fb.append(FlittingBird(canvas))
    ff = [] # a list for instances of FallingFeather
    for i in range(0, 9):
        ff.append(FallingFeather(canvas))
    # define the delay between draw loops
    delay = 33 # milliseconds, so about 30 frames per second
    # define the draw loop
    def draw():
        canvas.delete(tkinter.ALL)
        for x in sb: # for all the instances of SoaringBird in sb
            x.move() # make the instance move
            x.display() # display the instance
        for x in fb: # for all the instances of FlittingBird in fb
            x.move() # make the instance move
            x.display() # display the instance
        for x in ff: # for all the instances of FallingFeather in ff
            x.move() # make the instance move
            x.display() # display the instance
        canvas.after(delay, draw) # call this draw function again after the delay
    # start the draw loop
    draw()
    canvas.after(delay, draw) # after 33 milliseconds, run draw again
    root.mainloop() # keep the window open
