import math
def carros(numero_de_pessoas, capacidade_do_veiculo=5):
    """A função recebe como argumentos 2 inteiros, que
    são o número de pessoas e a capacidade do veículo e
    retorna quantos veículos são necessários para transportar
    esta quantidade de pessoas. Quando o usuário não informa
    a capacidade do veículo, admitimos que seja de 5 passageiros.
    """
    return math.ceil(numero_de_pessoas/capacidade_do_veiculo)