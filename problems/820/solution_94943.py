def posLetra (frase, letra, ocorrencia):
    """funçao que recebe uma frase, uma letra e um numero que indica a ocorrencia desejada da letra na frase e retorna a posiçao onde a letra esta na str, se ocorrencia < numero de ocorrencias na str retorna -1.
    entrada: str, str, int;
    saida: int."""
    
    ocorrencias = str.count (frase, letra)
    
    if ocorrencias < ocorrencia:
        return -1
    
    elif ocorrencia == 1:
        return str.index (frase, letra)
    
    listaOcorr = [0, 1]
    i = 0
    while i < len (frase):
        if frase [i] == letra:
            listaOcorr += [i]
        else:
    i = i + 1
    return listaOcorr [ocorrencia]