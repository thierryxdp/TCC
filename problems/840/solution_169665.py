def bolos (a=2, b=3, c=5):
    '''Quantidade de bolos que Joao consegue fazer'''
    import math
    if a <= 1 or b <= 2 or c <= 5:
        print (0)
    if (a == 2, b == 3, c == 5):
        print (2)
    if a * 2 or b * 2 or c * 2:
        print (2)
    if a * 3 or b * 3 or c * 3:
        print (3)
    if all(num%i!=0 for i in range(2,int(math.sqrt(c))+1)):
        print (4)