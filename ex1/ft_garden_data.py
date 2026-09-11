class Plant:
    def __init__(self , name , height, age):
        self.name = name
        self.age = age
        self.height = height

    def show(self):
        print(f"{self.name.capitalize()}: {self.height}cm, {self.age} days old ")
        
Plant1 = Plant("rose" , 25 , 30)
Plant2 = Plant("cactus", 80 , 45 )
Plant3 = Plant("mesfesse",200 ,45)
def ft_garden_data():
    print("=== Garden Plant Registry ===")
    Plant1.show()
    Plant2.show()
    Plant3.show()
    

if __name__ == "__main__":
    ft_garden_data()

        