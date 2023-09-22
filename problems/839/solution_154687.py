"""Retorna a quantidade de carros:
int, int -> int"""
def carros(pessoas,capacidade=5):
    if pessoas/capacidade == int(pessoas/capacidade):
        return int(pessoas/capacidade)
    else:
        return int(pessoas/capacidade) + 1