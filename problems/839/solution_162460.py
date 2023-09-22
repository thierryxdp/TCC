def carros(pessoas,assentos=5):
"""funcao que calcula o numero de carros dado o numero de pessoas"""
if pessoas % assentos > 0:
    return pessoas//assentos + 1
if pessoas % assentos = 0:
    return pessoas//assentos