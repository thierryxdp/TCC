def posLetra (string, letra, numero):
    """Função que, dada uma string, uma letra e um número que indica a ocorrência desejada para a letra, retorna a posição da string que aquela ocorrência da letra está
    entrada: str, str, int
    saída: int"""
    
    proximo = 0
    ocorrencia = 0
    
    while proximo < len(string):
        if string[proximo] != letra:
            proximo = proximo + 1
            
        if string[proximo] == letra and ocorrencia < numero:
            ocorrencia = ocorrencia + 1
            proximo = proximo + 1
            
        if ocorrencia == numero:
            return (proximo-1)
        
        if proximo == len(string) and ocorrencia < numero:
            return -1