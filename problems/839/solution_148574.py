def carros (a):
    ''' é dividir o número de pessoas por 5 que é a capacidade de cada carro, mas precisamos de uma
divisão exata porque não tem como levar 1 pessoa e meia '''
    return  math.ceil(a//5)