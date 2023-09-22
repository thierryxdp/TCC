# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis
def total(lc, d):
    '''A função total recebe uma lista de compras e um dicionario
    que possui o preço de um produto, e calcula e retorna o valor total
    da lista de compras'''
    
    r = []
    for i in lc:
        if i in d:
            list.append(r, (dict.get(d,i)))
    r = sum(r)
    r = round(r,2)
    
    return r