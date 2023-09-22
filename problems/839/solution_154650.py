"""Retorna a quantidade de carros:
int, int -> int"""
def carros(pessoas,capacidade):
    if capacidade==5:
        return pessoas/capacidade
    else:
        return (pessoas/capacidade)