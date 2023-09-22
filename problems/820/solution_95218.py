def posLetra (frase, letra, n):
    """ Funcao que retorna a posicao da string em que a ocorrencia da letra esta;
    Entrada: str, str, int
    Saida: int"""
    
    fraseo = []
    ind = 0
    oco = 0
    
    while oco <= n and ind < len(frase):
        if frase[ind] == letra:
            fraseo = fraseo + [frase[ind]]
            oco = oco + 1
        ind = ind + 1
       

    if oco > n:
        return len(fraseo)
    else:
        return -1