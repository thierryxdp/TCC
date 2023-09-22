def posLetra(frase,letra,num):
    
    contaLetra=0
    i=0
    
    while i < len(frase) or contaLetra < num:
        if frase[i] == letra:
            contaLetra = i
        
        i += 1
    
    if contraLetra < num:
        contraLetra = -1
    
    return contaLetra