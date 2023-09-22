def acima_da_media(lista):
    """função que dada uma lista com as notas dos alunos, notas acima da média
 list--->float"""
    media = sum(lista)/len(lista)
    if len(lista)==1:
        list.clear(lista)
        return(media,lista)
    else:
        inserir = list.append(lista,media)
        organizar = list.sort(lista)
        a = list.reverse(lista)
        encontre = list.index(lista,media)
        nova_lista = lista[0:encontre]
        list.reverse(nova_lista)
        return (nova_lista)