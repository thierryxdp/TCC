# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveisdef total(lista,dicionario):
    ''' dada uma lista de compras e um dicionario contendo o preço de cada produto.
calcula e retorna o valor total dos itens da lista presentes no dicionario.
list,dict->int'''
    j=0
    for x in lista:
        if x in dicionario:
            j= j+dicionario[x]
    return round(j,2)