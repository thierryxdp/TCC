import math
def num_bombons(dinheiro,preco):
    '''calcula a quantidade de bombons que conseguem ser comprada dado o dinheiro e o preco unitario do bombom.
    float, float->int'''
    return math.floor(dinheiro/preco)