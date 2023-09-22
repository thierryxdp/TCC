def posLetra(frase, letra, n):
    """Recebe uma string, uma letra e um número que indica a ocorrência
    e retorna em que posição da string aquela ocorrência da letra está"""
    """str,str,int -> int"""
    
    i = 0
    ocorrencia = 0
    
    while (i < len(frase)):
        if letra == frase[i]:
            ocorrencia = ocorrencia + 1
            
        if ocorrencia == n:
            return i
        
        i = i + 1
    return -1