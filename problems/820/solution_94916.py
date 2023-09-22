def posLetra (frase, letra, ocorrencia):
    """funçao que recebe uma frase, uma letra e um numero que indica a ocorrencia desejada da letra na frase e retorna a posiçao onde a letra esta na str, se ocorrencia < numero de ocorrencias na str retorna -1.
    entrada: str, str, int;
    saida: int."""
    
    ocorrencias = str.count (frase, letra)
    
    if ocorrencias < ocorrencia:
        return -1
    
    if ocorrencia == 1:
        return str.index (frase, letra)
    
    else:
        return nada