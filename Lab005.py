#age=int(input("Enter your age:\n"))
for i in range(5):
    name=str(input("enter you name: "))
    age = int(input("Enter your age:\n"))
    if age >=18:
        print(f"{name} your are allowed")
    else:
        print(f"{name} Not allowed to enter")