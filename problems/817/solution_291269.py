def acima_da_media(lista):
    tamanhoLista=len(lista)
    somaLista=sum(lista)
    mediaLista=somaLista/tamanhoLista
    list.append(lista,mediaLista)
    list.sort(lista)
    index=list.index(lista,mediaLista)
    resultado=lista[index+1:]
    return resultado