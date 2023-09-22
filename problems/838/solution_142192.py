import math
#questão_1
def num_bombons(dinheiro, preco):
    '''calcula a quantidade de bombons que se pode comprar com o dinheiro que tem e o preço do bombom
    int, float -> float
    '''
    return abs(round((dinheiro/preco)-0.5, 0))#Escreva sua função aqui. Pode apagar essa linha.