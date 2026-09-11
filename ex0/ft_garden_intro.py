def ft_garden_intro(name : str, height:  int, age: int )-> None:
    print(f"=== Welcome to My Garden ===")
    print(f"Plant: {name.capitalize()}")
    print(f"Height: {height}cm")
    print(f"Age: {age} days")

    print("=== End of Program ===")

if __name__ == "__main__":
    ft_garden_intro("rose", 25, 30)