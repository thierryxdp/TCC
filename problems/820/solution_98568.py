def posLetra(string, letra, numero):
    contador = 0
    posicao = 0
    while contador != numero:
        if posicao != 0 or contador > 0:
           posicao = str.find(string, letra, posicao+1, len(string))
        else:
            posicao = str.find(string, letra, posicao, len(string))  
        if posicao == -1:
            return posicao
        
        contador = contador + 1
    return posicao