def colisao(abcd,efgh):
    '''a funcao colisao recebe duas tuplas com quatro valores inteiros cada uma, representando as 
     coordenadas dos vertices inferior esquerdo e superior esquerdo do primeiro retângulo e do segundo 
     retângulo, nessa ordem, e devolve True se ha colisao entre os 2 retangulos e False, caso contrario.
     tuple, tuple --> bool'''
    a = abcd[1]
    b = abcd[3]
    c = abcd[5]
    d = abcd[7]
    e = efgh[1]
    f = efgh[3]
    g = efgh[5]
    h = efgh[7]
    if ((e<c or e==c) and (f<d or (f==d))):
        return True
    else:
        return False