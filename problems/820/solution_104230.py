def posLetra(frase,letter,n):
    index= 0
    ocorrencia=0
    texto= list(frase)
    
    while index < len(texto):
        if letter in texto[index]:
            
            ocorrencia+= 1
            
            if ocorrencia == n:
                return index
        index+=1
    if ocorrencia > n:
        return -1
    else:
        ocorrencia