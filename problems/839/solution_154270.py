from math import ceil
def carros(numPessoas, capacidade=5):
    # Função que pega o número de pessoas e a capacidade do carro, e retorna o número de carros que eles irão precisar
    # int, int -> int
    return ceil(numPessoas/capacidade)