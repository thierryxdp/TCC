def posLetra(string,letra,ocorrencia):
    
    i=1

    
    while letra in string[i]:
        x=str.index(string,letra)
        i+=1
        
    if i=ocorrencia:
         return ocorrencia
        
    else:
         return (-1)