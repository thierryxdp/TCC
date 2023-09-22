def carros():
    '''Esta função calcula o número de carros necessários para transportar um determinado número de pessoas'''
   
    carro = int(input('Contando com o banco do motorista, quantos assentos o carro tem?  '))
    pessoas = int(input('Quantas pessoas vão viajar?  '))

    return (carro//pessoas)