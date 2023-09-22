def posLetra(frase, letra, num):

    i = 0
    cont = 0
       
    if str.count(frase, letra) < (num):
        return -1
    
    while i < len(frase):
        if frase[i] == letra:
                cont += 1
        i += 1
                
    return cont