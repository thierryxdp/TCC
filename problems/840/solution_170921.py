#Recebe a quantidade de xícaras de farinha de trigo, ovos e colheres de sopa de leite
def bolos(a, b, c):
    '''int,int,int=>int'''
    a=a//2
    b=b//3
    c=c//5
    if (a<=b and a<=c):
        return a
    if (b<=a and b<=c):
        return b
    else:
        return c