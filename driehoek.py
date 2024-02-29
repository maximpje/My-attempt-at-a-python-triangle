x = int(input("user input: "))

for a in range(x + 2):
    if a // 2 * 2 != a:
        b = x - a
        c = b / 2
        d = " " * int(c)
        print(d + "*" * a)