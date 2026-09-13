class Plant():
    def __init__(self , name , height , age):
        self._name = name
        self._height = height
        self._age = age


    def show(self):
        print(f"Plant Created: {self._name.capitalize()}: {self._height}cm, {self._age} days old")

                   
    def set_height(self, newheight):
        if newheight < 0:
            print("Error, height can't be negative")
        else:
             self._height = newheight



    def set_ages(self, newage):
        if newage < 0:
              print(f"{self._name.capitalize()}: Error, age can't be negative")
        else :
          self._age = newage 


    def get_height(self):
         return self._height


    def get_ages(self):
         return self._age


Plant1 = Plant("Rose", 15, 50)

def ft_garden_security():
    print("=== Garden Security System ===")
    Plant1.show()
    Plant1.set_height(24)
    Plant1.set_ages(30)
    print(f"Height updated: {Plant1._height}")
    print(f"Age updated: {Plant1._age}")
    Plant1.set_height(-4)
    

    
    
    



if __name__ == "__main__":
     ft_garden_security()