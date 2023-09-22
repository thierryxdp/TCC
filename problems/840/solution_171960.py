def bolos (a, b, c):
    #para cada bolo é necessario 2a, 3b, 5c
    if a > 0 and b > 0 and c > 0 and (a+b+c)%10 == 0:
        return(a+b+c)/10
    
    if a < 2 or b < 3 or c < 5:
        return 0
    
    if a % 2 > 0 and b % 3 > 0 and c % 5 > 0:
        return (a//2 + b//3 + c//5)/10