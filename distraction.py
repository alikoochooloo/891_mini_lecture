import turtle
import random
import time
import winsound

# class to create our turtle game, duh!
class Window():
    def __init__(self,setnumber):
        super(Window, self).__init__()


        self.autotime = 0
        self.setnumber = setnumber

        # create game window
        self.win = turtle.Screen()
        self.win.title("Distraction")
        self.win.bgcolor('white')
        self.win.setup(width=500, height=500)

        # create generic turtle
        self.obj = turtle.Turtle()
        self.obj.shape('circle')
        self.obj.speed(0)
        self.obj.penup()

        # decide which specific turtle to make
        if setnumber == 1:
            self.obj.color('black')
        else:
            self.obj.color('gray')

        self.obj.goto(0, 0)
        self.obj.direction = 'stop'

        #listen to keyboard inputs based on the specific turtle
        self.win.listen()
        if setnumber == 1:
            self.win.onkey(self.go_up, 'Up')
            self.win.onkey(self.go_right, 'Right')
            self.win.onkey(self.go_down, 'Down')
            self.win.onkey(self.go_left, 'Left')
            self.win.onkey(self.setauto, 'z')
            self.open_2 = False
        else:
            self.win.onkey(self.go_up, 'w')
            self.win.onkey(self.go_right, 'd')
            self.win.onkey(self.go_down, 's')
            self.win.onkey(self.go_left, 'a')
            self.win.onkey(self.setauto, 'x')

        # probability list for the probability of moving to either side of the window
        self.probs = [0.25,0.5,0.75,1]

    # turn on autopilot
    def setauto(self):
        self.obj.goto(0, 0)
        if self.setnumber == 1:
            self.autotime = 30+round(random.random()*10)%10
        else:
            self.autotime = 12+round(random.random()*10)%10

    # turtle move up
    def go_up(self):
        if self.setnumber == 2:
            self.obj.sety(self.obj.ycor() + 15)
        else:
            self.obj.sety(self.obj.ycor() + 50)

    # turtle move down
    def go_down(self):
        if self.setnumber == 2:
            self.obj.sety(self.obj.ycor() - 15)
        else:
            self.obj.sety(self.obj.ycor() - 50)

    # turtle move right
    def go_right(self):
        if self.setnumber == 2:
            self.obj.setx(self.obj.xcor() + 15)
        else:
            self.obj.setx(self.obj.xcor() + 50)

    # turtle move left
    def go_left(self):
        if self.setnumber == 2:
            self.obj.setx(self.obj.xcor() - 15)
        else:
            self.obj.setx(self.obj.xcor() - 50)

    # turtle move command which decides based on the probability list which direction to move
    def move(self):
        r = random.random()
        if r < self.probs[0]:
            self.go_up()
        elif r < self.probs[1]:
            self.go_down()
        elif r < self.probs[2]:
            self.go_left()
        else:
            self.go_right()

    # recalculate the probability list based on the position of the turtle relative to the center of the screen
    def recalc(self):
        y = self.obj.ycor()-0
        self.probs[0] = (250+y)/1000
        x = 0 - self.obj.xcor()
        self.probs[2] = (750+x)/1000

    # check of the turtle has gone beyond any of the walls
    def bust(self):
        if self.obj.xcor() < -250 or self.obj.xcor() > 250 or self.obj.ycor() < -250 or self.obj.ycor() > 250:
            return True
        return False

    # the main run function
    def run_game(self):

        self.win.update()
        self.recalc()
        self.move()

        # check if the turtle is in autopilot if so play beep if there is less than 2 seconds left in the autopilot timer
        if self.bust():
            self.win.bye()
        if self.autotime > 0:
            self.obj.goto(0, 0)
            self.autotime -=0.25
            if self.autotime <= 2:
                if (self.autotime*4)%2:
                    winsound.Beep(600, 250)
        # if not then just sleep for 0.25 seconds
        else:    
            time.sleep(0.25)

# do I really have to put a comment on this too? come on your a masters student, I shouldn't be telling you what a main function does. god help us if you are really questioned over this. if so then just start from scratch with this: https://youtu.be/_WH6cbwZ5m8?t=20
if __name__ == '__main__':            
    human = True
    env1 = Window(1)
    env2 = Window(2)

    while 1:
        env1.run_game()
        env2.run_game()