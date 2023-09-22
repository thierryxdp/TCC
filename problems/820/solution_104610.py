posLetra(string, letra, numero):
    """Calcula e retorna a posição da string que contém a
    ocorrência requisitada de uma determinada letra"""

    lista = list(string)
    
    if lista.count(letra) >= numero:
        
        contagem = 0
        
        proximo = 0
        
        while (contagem != numero):
            
            if lista[proximo] == letra:
                
                contagem = contagem + 1
                
            proximo = proximo + 1
            
        return proximo - 1
    
    else:
        
        return -1