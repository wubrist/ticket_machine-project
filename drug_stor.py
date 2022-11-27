c = 0
m = 0
p = 0


def darug_stor(order):
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
