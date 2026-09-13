class Plant():
    def __init__(self , name , height , age):
        self.name = name
        self.height = height
        self.age = age

    def grow(self):
            self.height += 0.8


    def ages(self):
          self.age += 1

    def show(self):
        print(f"{self.name.capitalize()}: {self.height}cm , {self.age} days old")
                   


Plant1 = Plant("Rose", -25 , 30)


def ft_plant_growth(): 
    print("=== Garden Plant Growth ===")
    Plant1.show()
    a = Plant1.height
    for day in range(1,8):
            print(f"=== Day {day} ===")
            Plant1.ages()
            Plant1.grow()
            print(f"{Plant1.name.capitalize()}: {round(Plant1.height, 2)}cm , {Plant1.age} days old")

    print(f"Growth this week: {round(Plant1.height - a, 2)} cm")



if __name__ == "__main__":
    ft_plant_growth()
    