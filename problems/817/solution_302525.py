def acima_da_media(notas):
    """Função que dada uma lista com as notas dos alunos, retorna uma lista ordenada
com as notas que ficaram acima da média; list -> list"""   
    media=sum(notas)/len(notas)
    lista=notas+[media]
    list.sort(lista)
    indice=lista.index(media)
    return lista[indice+1:]