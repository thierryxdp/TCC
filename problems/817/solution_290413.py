def acima_da_media(lista):
    """recebe uma lista com as notas dos alunos e retorna outra lista ordenada com as notas que ficaram acima da média"""
    media=sum(lista)/len(lista)
    if media in lista :
        numero=list.count(lista,media)
        list.sort(lista)
        indice=list.index(lista,media)
        return lista[int(indice)+int(numero):]
    else:
        list.append(lista,media)
        list.sort(lista)
        indice1=list.index(lista,media)
        return lista[int(indice1)+1:]