def posLetra(string,letra,numero):
    
    vezes=[]
    posicao=0
    
    while posicao<len(string) and len(vezes)<numero:
        if letra in string:
            indice=str.find(string,letra,posicao+1)
            list.append(vezes,indice)
        posicao=posicao+1
        
    elif numero>len(vezes):
        return -1
    return vezes[-1:][0]