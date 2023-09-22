def posLetra(string,letra,numero):
    
    
    contagem = 0 #acumulador
    posicao = 0  #indice
    
    if str.count(string, letra)  >= numero:
        while contagem != numero:
            if string[posicao] == letra:
                contagem += 1
            posicao += 1
        return posicao -1
        
    else:
        return -1