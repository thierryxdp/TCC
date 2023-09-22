from math import ceil
def carros(P,C=5):
    """Retorna o numeros de carros necessarios para transportar o numero de pessoas pela quantidade de assentos por carro. Sendo o parametro P o número total de pessoas e C a quantidade de vagas por carro, sendo 5 o número padrao de assentos por carro.
Portanto é possivel calcular somente com uma entrada se tratarmos de carros com limite de 5 pessoas. As entradas devem ser números inteiros, e o retorno será um número inteiro""" 
    a=(P/C)
    num=ceil(a)
    return num