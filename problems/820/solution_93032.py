def posLetra(string,letra,numero):
    
    vezes=[]
    posicao=0
    
    while posicao<len(string) and len(vezes)<numero:
        if letra==string[posicao] and letra in string:
            indice=str.find(string,letra,posicao)
            list.append(vezes,indice)
        posicao=posicao+1
       
            
    return vezes[-1:][0]