"""Retorna a quantidade de veiculos necessario para viagem:
int, int -> int"""
def carros(pessoas,capacidade):
    if pessoas<=5:
        return int(pessoas/capacidade)