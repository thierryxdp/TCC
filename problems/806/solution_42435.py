def colisao(abcd,efgh):
    '''a funcao colisao recebe duas tuplas com quatro valores inteiros cada uma, representando as 
     coordenadas dos vertices inferior esquerdo e superior esquerdo do primeiro retângulo e do segundo 
     retângulo, nessa ordem, e devolve True se ha colisao entre os 2 retangulos e False, caso contrario.
     tuple, tuple --> bool'''
    a = abcd[0]
    b = abcd[2]
    c = abcd[4]
    d = abcd[6]
    e = efgh[0]
    f = efgh[2]
    g = efgh[4]
    h = efgh[6]
    if ((e<c or e==c) and (f<d or (f==d)):
        return True
    else:
        return False