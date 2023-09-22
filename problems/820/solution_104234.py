def posLetra(frase,letter,n):
    index= 0
    ocorrencia=0
    texto= list(frase)
    
    while index < len(texto):
        if letter in texto[index]:
            index+=1
            ocorrencia+= 1
            
            if ocorrencia == n:
                
                return index
        
    if ocorrencia < n:
        return -1