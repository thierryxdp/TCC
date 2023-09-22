def posLetra(frase,letra,ocorrencia):
    lista=list(frase)
    contador = lista.count(letra)
    
    if contador >+ ocorrencia:
        substitui = str.replace(frase,letra,'&',ocorrencia-1)
        return str.find(substitui,letra,0,-1)
    else:
        return -1