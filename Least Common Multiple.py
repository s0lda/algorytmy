def LCM(a,b):
    for i in range(1, a * b + 1):
        if i % a == 0 and i % b == 0:
            break
    print('Least Common Multiple:', i)

LCM(336,360)