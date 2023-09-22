#Questao 2
def total(lista,dic):
    '''
    funcao que recebe uma lista de compras e um dicionário contendo o preço de cada produto disponível
    em uma determinada loja, e retorna o valor total dos itens da lista que estejamdisponíveis nesta loja. 
    str -> float
    '''
    soma=0
    for i in range(len(lista)):
        if lista[i] in dic.keys():
            soma=soma+dic[lista[i]]
    return round(soma,2)