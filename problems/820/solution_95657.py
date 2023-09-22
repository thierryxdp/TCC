def posLetra(frase, caracter, index):
    
    cont = 0
    ocorrencias = 0
    
    while(cont < len(frase)):
        if frase[cont] == caracter:
            ocorrencias += 1
            
            if ocorrencias == index:
                return cont
                
        cont += 1
                
    return -1