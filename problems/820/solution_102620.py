def posLetra(frase,letra,ocorrencia):
    
    
    frase2 = frase.split()
    indice = 0
    
    while indice < len(frase2):
        if list.count(frase2,letra) <= ocorrencia:
            return -1