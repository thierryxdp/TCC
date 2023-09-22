def acima_da_media (lista_numero):
    """dada como entrada uma lsita com as notas de uam turma, a função
    retorna uma lista ordenada com as notas que ficaram acima da média.
    list -> list"""
    
    lista = lista_numero
    media = sum(lista)/len(lista)
    list.append(lista, media)
    list.sort(lista)

    repeticoes = list.count(lista, media)

    if repeticoes ==1:
        
        indice = list.index(lista, media)

    else:

        indice = list.index(lista,media) + repeticoes -1
        
    return lista[indice+1:]