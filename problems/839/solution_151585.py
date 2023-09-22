from math import ceil
def carros (numero_pessoas, capacidade_veiculo = 5):
    '''Função cacula quantidade de carros necessário para um número x de pessoas viajarem num número y de carros recebendo do usuário a quantidade de pessoas e a capacidade de veículos (caso a capacidade de veículos não seja forceida, será, então tomada a capacidade convencional de veículos)'''
    return ceil(numero_pessoas/ capacidade_veiculo)