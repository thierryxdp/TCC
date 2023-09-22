def posLetra (frase, letra, n):
    """ Funcao que retorna a posicao da string em que a ocorrencia da letra esta;
    Entrada: str, str, int
    Saida: int"""
    
    fraseo = []
    indice = 0
   	ocorrencia = 0
    
    while ocorrencia <= n:
        if letra in frase[indice]:
            fraseo = fraseo + [frase[indice]]
            ocorrencia = ocorrencia + 1
        indice = indice + 1
    return len(fraseo)