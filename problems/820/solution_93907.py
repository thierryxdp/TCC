def posLetra(string, letra, numero):
    i=0
    contador=0
    posicao=0
    while i< len(string)-1:
        if string[1]==letra:
            contador+=1
        if contador==numero:
        i+=1  
        return i
        
    return -1