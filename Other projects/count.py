x = 100
for x in range(100, 1 - 1, -1):
    if x % 2 == 0:
        print(str(x) + " is Even")
    else:
        if x % 3 == 0:
            print(str(x) + " is multiple of 3")
        else:
            if x % 5 == 0:
                print(str(x) + " is a number of 5")
            else:
                if x % 7 == 0:
                    print("Number is probobly a prime")
print("end", end='', flush=True)
