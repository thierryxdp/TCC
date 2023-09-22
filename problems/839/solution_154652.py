"""Retorna a quantidade de carros:
int, int -> int"""
def carros(pessoas,capacidade):
    if capacidade==5:
        return max(pessoas/capacidade)
    else:
        return max(pessoas/capacidade)