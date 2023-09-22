def posLetra (frase, letra, n):
    """ Funcao que retorna a posicao da string em que a ocorrencia da letra esta;
    Entrada: str, str, int
    Saida: int"""
    
    fraseo = []
    indice = 0
   	oco = 0
    
    while oco <= n:
        if letra in frase[indice]:
            fraseo = fraseo + [frase[indice]]
            oco = oco + 1
        indice = indice + 1
    return len(fraseo)