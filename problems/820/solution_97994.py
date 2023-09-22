def posLetra(string,letra,numero):
    
    lista = list(string)
    contagem = 0
    posicao = 0
    
    if list.count(lista, letra)  >= numero:
        while contagem != numero:
            if lista[posicao] == letra:
                contagem += 1
            posicao += 1
        return posicao -1
        
    else:
        return -1