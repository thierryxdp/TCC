def posLetra(texto,letra,num_ocorrencia):
    lista=[]
    while texto.count(letra)<num_ocorrencia:
        if letra in texto:
            if texto[indice]!=letra:
                lista.append(' ')
            else:
                lista.append(letra)
        else:
            return -1
         
    return len(lista)-1