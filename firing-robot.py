class Robot(object):
# ''' Class to create a Robot with initial attributes and some methods to perform '''
    def __init__(self):
    # ''' Initialize the object with initial attributes values '''
        self.x_coord = 10
        self.y_coord = 10
        self.fuel = 100

    def move_left(self):
    # ''' Method to perform a movement and fuel spending '''
        if self.fuel >= 5:
            self.fuel -= 5
            self.x_coord -= 1
        else:
            print("Insufficient fuel to perform action")

    def move_right(self):
    # ''' Method to perform a movement and fuel spending '''
        if self.fuel >= 5:
            self.fuel -= 5
            self.x_coord += 1
        else:
            print("Insufficient fuel to perform action")

    def move_up(self):
    # ''' Method to perform a movement and fuel spending '''
        if self.fuel >= 5:
            self.fuel -= 5
            self.y_coord -= 1
        else:
            print("Insufficient fuel to perform action")

    def move_down(self):
    # ''' Method to perform a movement and fuel spending '''
        if self.fuel >= 5:
            self.fuel -= 5
            self.y_coord += 1
        else:
            print("Insufficient fuel to perform action")

    def fire(self):
    # ''' This method fires the laser '''
        if self.fuel >= 15:
            self.fuel -= 15
            print("Pew! Pew!")
        else:
            print("Insufficient fuel to perform action")

    def status(self):
    # ''' This method outputs to the user the current status of the robot '''
       print ("({}, {}) - Fuel: {}".format(self.x_coord, self.y_coord, self.fuel))


def main():
    my_robot = Robot()
    end_prog = False

    while end_prog == False:
    # ''' This loops checks for the end of the program action whether is True or False '''
        command = input("Enter command: ")
        command = command.lower()
        if command == "left":
        # ''' This function checks for the input commands to perform the robot actions '''
           my_robot.move_left()
        elif command == "right":
            my_robot.move_right()
        elif command == "up":
            my_robot.move_up()
        elif command == "down":
            my_robot.move_down()
        elif command == "fire":
            my_robot.fire()
        elif command == "status":
            my_robot.status()
        elif command == "quit":
            print("Goodbye.")
            end_prog = True


if __name__ == "__main__":
    main()