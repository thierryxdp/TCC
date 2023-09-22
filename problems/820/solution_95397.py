def posLetra(frase,letra,num):
    numero_vezes=str.count(frase,letra)
    
    if numero_vezes < num:
        return -1
    else:
        x=str.replace(frase,letra,' ',num)
        posicao=str.index(x,letra)
        return posicao