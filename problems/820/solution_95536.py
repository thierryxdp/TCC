def posLetra(frase,letra,num):
    
    contaLetra=0
    marcaLetra = 0
    i=0
    
    while i < len(frase):
        if frase[i] == letra:
            marcaLetra = i
            contaLetra += 1

        if contaLetra == num:
            return marcaLetra

        i += 1
    
    return -1