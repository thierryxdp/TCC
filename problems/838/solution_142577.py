#Escreva sua função aqui. Pode apagar essa linha.
import builtins
num_bombons(dinheiro,preço):
    """dado os valores do preço e do dinheiro,
    a função retorna a quantidade de bombons que é possível comprar"""
    return round((dinheiro/preço)-0.5)