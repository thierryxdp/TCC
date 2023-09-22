def acima_da_media(lista):
    '''função que dada uma lista com a nota de x alunos, retorna
    uma nova lista que ordena a nota dos alunos que ficaram acima
    da média.
    entrada da função: list
    saída da função: list'''
    media= sum(lista)/ len(lista)
    if media not in lista:
        lista.append(media)
    lista.sort()
    x = lista.index(media)
    lista2 = lista[x+1:]
    y = lista2.count(media)
    return lista2[y:]