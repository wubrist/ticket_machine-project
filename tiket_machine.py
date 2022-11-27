c = 0
m = 0
p = 0


def darug_stor():
    if order == "cosmetic":
        global c
        c += 1
        print(f"c_{c}")

    if order == "perfumes":
        global p
        p += 1
        print(f"p_{p}")
    if order == "medicine":
        global m
        m += 1
        print(f"m_{m}")


def message(user):
    return user


user1 = message("your number is ")
user2 = message("please wait and some one will assist yuo shortly. ")
order = input("please choose your product option:")
while order != "":
    print(user1)
    darug_stor()
    print(user2)
    permission = input("do yuo want to continue ?Y/N")
if permission == "y":
    order = input("please choose your product option:")
