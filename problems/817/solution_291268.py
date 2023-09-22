def acima_da_media(lista):
    tamanhoLista=len(lista)
    somaLista=sum(lista)
    mediaLista=somaLista/tamanhoLista
    mediaListaInt=int(mediaLista)
    list.append(lista,mediaListaInt)
    list.sort(lista)
    index=list.index(lista,mediaListaInt)
    resultado=lista[index+1:]
    return resultado