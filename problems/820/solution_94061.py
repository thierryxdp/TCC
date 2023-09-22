def posLetra (frase, letra, numero):
    i=0
    posicao=0
    x=0
    if frase.count(letra)>=numero:
        while i<numero:
            posicao=str.find(frase[posicao:],letra)+1
            x+=posicao
            i+=1
        return posicao-1
    
    else:
        return -1