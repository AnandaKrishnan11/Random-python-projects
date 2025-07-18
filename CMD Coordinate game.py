import numpy as np

class Point:

    def __init__(self,x,y):
        self.__x = x
        self.__y = y
        
    def get_point(self):
        return self.__x, self.__y
        
        
class Rectangle:

    def __init__(self):
        self.x1, self.x2 = sorted(map(int,np.random.randint(1, 10, 2)))
        self.y1, self.y2 = sorted(map(int,np.random.randint(1, 10, 2)))
    
    @property
    def get_coordinates(self):
        print(f'The coordinates of the rectangle: {(self.x1,self.y1)} and {(self.x2,self.y2)}')

   
    def contains(self,point:Point):
        x,y = point.get_point()
        return self.x1 <= x <= self.x2 and self.y1 <= y <= self.y2
    

def run_game():
    while True:
        rectangle = Rectangle()
        rectangle.get_coordinates

        try:
            x = int(input("Guess x coordinate: "))
            y = int(input("Guess y coordinate: "))
        except ValueError:
            print("Please enter valid integers.")
            continue

        user_point = Point(x, y)

        if rectangle.contains(user_point):
            print("Correct! The point is inside the rectangle.")
        else:
            print(" Sorry! The point is outside the rectangle.")

        play_again = input("Play again? (y/n): ").lower()
        if play_again != 'y':
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    run_game()
