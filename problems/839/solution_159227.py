import math
def carros (numero_pessoas, capacidade_veiculo=5):
    '''funnção que calcula e retorna o número exato de carros necessários para viagem de um grupo de amigos, considerando que seja dado o número de pessoas e a capacidade do carro. Caso a capacidade do veículo não seja informada, será aplicado o argumento default como entrada, considerando a regra rodoviária para um veículo convencional com capacidade de transportar até 5 passageiros. Para executar esse cálculo usaremos a função math.ceil do módulo math'''
    return math.ceil (numero_pessoas/capacidade_veiculo)