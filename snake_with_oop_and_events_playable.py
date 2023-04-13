from turtle import Screen, Turtle as GameObject
import random
import time

#Hey and welcome. Feel free to test the game out. It reminds me of the legendary Nokia 3310.  

class Snake:
    def __init__(self) -> None:
        self.body = []
        self.generate_snake(3)
        self.head = self.body[0]
        self.heading = 0
        self.on_eating = Event()

    def generate_snake(self, count):
        for i in range(0, count):
            snake = GameObject()
            snake.penup()
            snake.color("white")
            snake.shape("square")
            snake.speed(1)
            snake.turtlesize(0.5, 0.5)
            if self.body:
                snake.goto(self.body[-1].pos())
            self.body.append(snake)

    def slithering(self):
        for body_part in range(len(self.body) - 1, 0, -1):
            new_x = self.body[body_part - 1].xcor()
            new_y = self.body[body_part - 1].ycor()
            self.body[body_part].goto(new_x, new_y)
        self.head.forward(10)
        self.direction_changed = False

    def eat(self, delicious_snack):
        """Import a delicious snack object as a parameter for the snake to eat.

        Call this method before the snack run method, or the snack escapes!"""

        if delicious_snack.distance(self.head) < 8:
            self.generate_snake(1)
            self.eating()

    # No native eventlistening. Using a custom eventlistener, defined after the Snake class

    def eating(self):
        self.on_eating()

    def add_listeners_for_eating(self, listener):
        self.on_eating += listener

    def remove_listeners_for_eating(self, listener):
        self.on_eating -= listener

    # Controls: A bool "direction_changed" is used to make sure the current frame has been updated
    # and the snake has moved forward before it can turn again. Without the flag it's
    # possible for the snake to change heading, and hit its own body before moving forward.

    def direction(self, new_direction):
        if not self.direction_changed:
            self.head.setheading(new_direction)
            self.direction_changed = True

    def right(self):
        if self.head.heading() != LEFT:
            self.direction(RIGHT)

    def up(self):
        if self.head.heading() != DOWN:
            self.direction(UP)

    def left(self):
        if self.head.heading() != RIGHT:
            self.direction(LEFT)

    def down(self):
        if self.head.heading() != UP:
            self.direction(DOWN)


UP = 90
RIGHT = 0
LEFT = 180
DOWN = 270


class Event:
    def __init__(self) -> None:
        self.__eventhandlers = []

    def __iadd__(self, handler):
        self.__eventhandlers.append(handler)
        return self

    def __isub__(self, handler):
        self.__eventhandlers.remove(handler)

    def __call__(self, *args, **kwds):
        for eventhandler in self.__eventhandlers:
            eventhandler(*args, **kwds)


class Snack:
    def __init__(self) -> None:
        self.delicious_snack = None
        self.spawn_snack()

    def spawn_snack(self):
        if not self.delicious_snack:
            snack = GameObject()
            snack.penup()
            snack.color("white")
            snack.shape("square")
            snack.turtlesize(0.5)
            self.delicious_snack = snack
            self.__randomize_position()

    def run_or_get_eaten(self, snack_eating_snake):
        for body_parts in snack_eating_snake:
            if body_parts.distance(self.delicious_snack) < 2:
                self.__randomize_position()

    def __randomize_position(self):
        random_y = round(random.randint(-28, 28) * 10)
        random_x = round(random.randint(-28, 28) * 10)
        self.delicious_snack.goto(random_x, random_y)
        print(f"{self.delicious_snack.pos()} a delicious snack!")


class GameManager:
    def __init__(self) -> None:
        self.game_is_on = True

    def define_field(self, screen):
        """Accepts both: square and rectangular screens"""
        self.field_right_edge = (screen.window_width()) / 2
        self.field_left_edge = (screen.window_width() / 2) * -1
        self.field_top_edge = screen.window_height() / 2
        self.field_bottom_edge = (screen.window_height() / 2) * -1

    def watch_snake(self, big_snake):
        for body_part in big_snake.body[1:]:
            if (
                body_part.distance(big_snake.head) < 0.1
                or big_snake.head.ycor() > self.field_top_edge
                or big_snake.head.ycor() < self.field_bottom_edge
                or big_snake.head.xcor() < self.field_left_edge
                or big_snake.head.xcor() > self.field_right_edge
            ):
                print("Ouch!")
                game_over = GameObject()
                enter = GameObject()
                game_over.color("White")
                enter.color("White")
                game_over.turtlesize(2)
                enter.turtlesize(2)
                game_over.write(f"GAME OVER", align=ALIGN, font=FONT)
                enter.goto(0, -30)
                enter.write(f"PRESS ENTER TO RESTART", align=ALIGN, font=FONT)
                self.game_is_on = False

    def score_successful_eating(self):
        print("the snake grows")


FONT = ("ArialBlack", 16, "bold")
ALIGN = "center"


def run_game():

    screen = Screen()
    screen.reset()
    screen.setup(width=600, height=600)
    screen.bgcolor("black")
    screen.title("Snek")
    screen.tracer(0)

    big_snake = Snake()
    big_snack = Snack()
    big_bauss = GameManager()

    big_bauss.define_field(screen)
    big_snake.add_listeners_for_eating(big_bauss.score_successful_eating)

    while big_bauss.game_is_on:

        screen.update()
        screen.listen()
        time.sleep(0.05)

        big_snake.slithering()
        big_snack.spawn_snack()
        big_snake.eat(big_snack.delicious_snack)
        big_snack.run_or_get_eaten(big_snake.body)
        big_bauss.watch_snake(big_snake)

        screen.onkeypress(big_snake.right, "Right")
        screen.onkeypress(big_snake.up, "Up")
        screen.onkeypress(big_snake.left, "Left")
        screen.onkeypress(big_snake.down, "Down")

    screen.onkeypress(run_game, "Return")
    screen.exitonclick()


run_game()
