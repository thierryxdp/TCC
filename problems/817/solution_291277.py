def acima_da_media(lista):
    tamanhoLista=len(lista)
    somaLista=sum(lista)
    mediaLista=somaLista/tamanhoLista
    
    if int(mediaLista) in lista:
        list.sort(lista)
        index=list.index(lista,int(mediaLista))
        resultado=lista[index+1:]
        return resultado
    else:
        list.append(lista,mediaLista)
        list.sort(lista)
        index=list.index(lista,mediaLista)
        resultado=lista[index+1:]
        return resultado