def posLetra(frase, letra, numero):
    """recebe uma frase, uma letra e um numero que indica a ocorrencia desejada
    e retorna a posicao da frase em que aquela letra esta
    string, string, int -> int"""
    
    i = 0
    j = 0
    
    while j != numero:
        while i < len(frase):           
            if frase[i] == letra:
                j += 1
                  
        i += 1
        
        return i - 1
    
    return -1