#Bolos
Número Número Número -> Int
def bolos(a,b,c):
    '''Essa função rece a quantidade de cada ingrediente e retorna
    o número de bolos que é possível fazer com eles'''
    trigo = a//2
    ovos = b//3
    leite = c//5
    return min(a//2, b//3, c//5,0)