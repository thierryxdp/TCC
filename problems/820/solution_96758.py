def posLetra(frase, letra, n):
    '''Acha a posição da n-ésima letra em uma frase
    str,str,int->int'''
    ocorrencias = []                 
    for c in enumerate(frase):           
        if c[1] == letra:               
            ocorrencias.append(c[0])  
    if n > len(ocorrencias):      
        return -1                   
    return ocorrencias[n - 1]