# Coloque um comentário dizendo o que a função faz
def total(lista+[],dict={}):
    '''funcao que recece uma lista de compras
    e um dicionário contendo o preço dos 
    produtos disponíveis na loja e retorna
    o valor total dos itens da lista que estejam
    disponíveis na loja'''
    
    cont = 0.0
    for i in lista:
        cont+=dict[i]
    return round(cont,2)