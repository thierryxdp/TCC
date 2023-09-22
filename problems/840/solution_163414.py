def bolos(a,b,c):
#Cálculo de número de bolos possível para 3 ingredientes(a,b,c)
    a=a//2
    b=b//3
    c=c//5
    return min(a,b,c)