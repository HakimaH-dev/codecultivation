class Plant:
    def __init__(self , name , height, age):
        self.name = name
        self.age = age
        self.height = height


    def grow(self):
            self.height += 0.8


    def ages(self):
          self.age += 1


    def show(self):
        print(f"Created:{self.name.capitalize()}: {self.height}cm, {self.age} days old ")

        
Plant1 = Plant("rose" , 25 , 30)
Plant2 = Plant("cactus", 80 , 45 )
Plant3 = Plant("sunflower",200 ,45)
Plant4 = Plant("Fern",15 ,120)
Plant5 = Plant("oak",200 ,365)
def ft_plant_factory():
    print("=== Plant Factory Output ===")
    Plant1.show()
    Plant2.show()
    Plant3.show()
    Plant4.show()
    Plant5.show()
    
if __name__ == "__main__":
    ft_plant_factory()