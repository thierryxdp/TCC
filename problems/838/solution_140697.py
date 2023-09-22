#Escreva sua função aqui. Pode apagar essa linha.
from math import floor
def num_bombons(dinheiro,preco):
    "Função que calcula o maior número de bombons que se consegue comprar, dados o dinheiro e o preço do bombom para realização da compra."
    return floor(dinheiro/preco)