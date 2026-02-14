from turtle import Turtle
STARTING_POSITIONS = [(0,0),(-20,0),(-40,0)]
MOVE_DISTANCE = 20
UP = 90
DOWN  = 270 
LEFT = 180
RIGHT = 0

class Snake: 
    
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0] # snake head
        
    #this function creates a three segments snake's body
    def create_snake(self):
        for position in STARTING_POSITIONS: 
            self.add_segment(position) # looping through position
            
    #this function create movement for the snake
    def move(self):
        for seg_num in range(len(self.segments) -1, 0, -1):
            new_x = self.segments[seg_num -1].xcor()
            new_y = self.segments[seg_num -1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def add_segment(self, position):
        new_segment = Turtle("square")
        # Ocean-themed gradient colors - teal/green like web version
        if len(self.segments) == 0:
            new_segment.color("#4ecdc4")  # Head - bright teal
        else:
            new_segment.color("#2d8b75")  # Body - darker green
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)
    
    # def extend to add a new segment to the snake when it hits the food
    def extend(self):                      #.position method came from Turtle class
        self.add_segment(self.segments[-1].position()) # add another new segment to last the segment when the snake hit the food
        
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)