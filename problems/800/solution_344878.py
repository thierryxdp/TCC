def total(lista, dicionario):
    """função que recebe uma lista de comprar e um dicionario com o preço dos produto e devolve
    o total dos intens da lista que estejam disponíveis ; list, dict->float"""
    chaves = list(dict.keys(dicionario))
    valores = list(dict.values(dicionario))
    preco= 0
    i = 0
    for elem in lista:
        if lista[i] in chaves:
        	preco += dict.get(dicionario,lista[i])
        else:
            preco = preco
        i = i+1
    return round(preco,2)# Coloque um comentário dizendo o que a função faz
# Escolha nomes elucidativos para suas variáveis