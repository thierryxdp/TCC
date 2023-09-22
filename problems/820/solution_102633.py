def posLetra(frase,letra,ocorrencia):
    
    
    frase2 = list(frase)
    indice = 0
    
    while indice < len(frase2):
    if ocorrencia == 1:
        return list.index(frase2,letra)
    if list.count(frase2,letra) < ocorrencia:
        return -1