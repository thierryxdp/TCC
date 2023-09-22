def posLetra(frase, letra, numero):
    """Dada a frase, a letra e o numero equivalente ao numero de ocorrencia da letra fornecida
    retorna a posicao em que a ocorrencia esta;
    str, str, int -> int"""
    
    i = 0
    ocorrencia = 0
    a = str.count(frase, letra)
    
    if a < numero:
        return -1
    
    while ocorrencia < numero:
        if frase[i] == letra:
            ocorrencia += 1
    	i += 1
    return i-1