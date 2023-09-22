"""Retorna a quantidade de carros:
int, int -> int"""
def carros(pessoas,capacidade):
    if capacidade==5:
        return max(pessoas/5)
    else:
        return max(pessoas/capacidade)