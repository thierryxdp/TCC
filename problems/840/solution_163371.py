#Bolos
#Int Int Int -> Int
def bolos(a,b,c):
    '''Essa função rece a quantidade de cada ingrediente e retorna
    o número de bolos que é possível fazer com eles'''
    return min(a//2, b//3, c//5)