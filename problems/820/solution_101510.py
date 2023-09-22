def posLetra(string, letra, ocorrencia):
    """funcao que recebe uma string uma letra e um numero que indica a ocorrencia desejada da letra e retorna a posição da string em que a letra se encontra
	str, str, int -> int"""
    
    i = 0
    j = 0
    
    while len(string) > i and ocorrencia > j:
        if string[i] == letra:
            j = j + 1
        
        i = i + 1
    
    if ocorrencia > j:
        return -1 
    
    else: 
        return i - 1