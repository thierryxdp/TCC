def colisao (ret1,ret2):
    """ A funcao colisao recebe duas tuplas com quatro valores inteiros cada uma,representando as coordenadas dos vertices inferior esquerdo e superior esquerdo do primeiro retângulo e do segundo retângulo, nessa ordem, e devolve True se ha colisao entre os 2 retangulos e False, caso contrario.
    Parâmetro de entrada: tupla=tupla com quatro elementos
    Parâmetro de saída:tupla com apenas elementos pares da tupla original, na mesma ordem que se encontravam
    tuple-->tuple"""
    a,b,c,d=tupla
    resultado=0,
    if a%2==0:
        a= (a,)
        resultado=resultado+a
    if b%2==0:
        b= (b,)
        resultado=resultado+b
    if c%2 ==0:
        c= (c,)
        resultad0=resultado+c
    if d%2 == 0:
        d= (d,)
        resultado= resultado+d
    return resultado [1:]