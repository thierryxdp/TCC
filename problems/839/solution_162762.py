def carros(pessoas, capacidade=5):
    """ divide o numero de pessoas dentro das capacidades do carro"""
    if capacidade > 5:
        return pessoas/ capacidade + 5
    return pessoas / capacidade