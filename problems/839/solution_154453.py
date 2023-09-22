"""Retorna a quantidade de veiculos necessario para viagem:
int, int -> int"""
def carros(pessoas,capacidade=5):
    if pessoas>0:
        return int(pessoas/capacidade)