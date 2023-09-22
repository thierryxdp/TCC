def posLetra(frase, letra, n):
    ocorrencias = []                 
    for c in enumerate(frase):           
        if c[1] == letra:               
            ocorrencias.append(c[0])  
    if n > len(ocorrencias):      
        return -1                   
    return ocorrencias[n - 1]