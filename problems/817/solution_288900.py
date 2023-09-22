def acima_da_media (lista):
    '''funcao que dado uma lista com as medias dos
    alunos retorna uma nova lista com as notas
    que ficaram acima da media; list -> list'''
    
    media = sum(lista)/len(lista)
    
    if media not in lista:
        list.append(lista,media)
        list.sort(lista)
        a = list.index(lista,media)
        return lista[a+1:]
    
    else:
        list.sort(lista)
        a = list.index(lista,media)
        return lista[a+1:]