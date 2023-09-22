import math

def carros(p,l=5):

    """Retorna o numeros de carros necessarios para transportar o num de pessoas pela quantidade de lugares por carro. Sendo p o número total de passageiros e l a quantidade de lugares por carro, tendo 5 como o número padrao de assentos por carro.
 A entradas devem ser números inteiros, pois nao existe meia pessoa e o retorno será um número inteiro""" 

    a=(p/l)

    num=math.ceil(a)

    return num