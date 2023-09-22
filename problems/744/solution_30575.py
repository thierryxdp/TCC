import math
def hastag(s):
    """função que recebe uma string e insere o caractere # no inicio, no meio e no final dela"""
    tamanho = len(s)
    meio = math.floor(tamanho/2)
    inicio = s[:meio]
    final = s[meio:]

    return '#'+inicio+'#'-final+'#'