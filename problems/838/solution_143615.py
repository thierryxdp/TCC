#Calcula o número de bombons que podem ser adquiridos  
def num_bombons(dinheiro,preco):
    return  int(dinheiro/preco), dinheiro % preco
"""retorna o número de bombons dado um preço e dinheiro"""