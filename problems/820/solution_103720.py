def posLetra(frase, letra, numero_ocorrencia):
    
    i = 0
    j = 0
    
    while len(frase) > i and numero_ocorrencia > j:
        if letra in frase[i]:
            
            j+=1
        
        i +=1
        
    if j == numero_ocorrencia:
        return i-1
    else:
        return -1