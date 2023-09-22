def carros ( pessoas, capacidade=5)
""" função que retorna o numero de carros necessarios a partir de uma quantidade de passageiros e lugares no carro"""
if pessoas// capacidade!=0:
    return pessoas// capacidade + 1
else:
    return pessoas//capacidade