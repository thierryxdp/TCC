#Questão
import math

    def carros(passageiros, capacidade=5):
    '''Calcula a quantidade de carros necessarios para.
    se realizar uma viagem, caso a capacidade seja fora.
    do padrao, inserir o segundo valor.
    '''
    return math.ceil(passageiros / capacidade)