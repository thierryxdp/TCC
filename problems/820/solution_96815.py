def posLetra(frase, letra, numero):
    """Dada a frase, a letra e o numero equivalente ao numero de ocorrencia da letra fornecida
    retorna a posicao em que a ocorrencia esta;
    str, str, int -> int"""
    
    i = 0
    ocorrencia = 0
    
    while i < len(frase):
        if letra in frase[i]:
            ocorrencia += 1
        i += 1
    return ocorrencia