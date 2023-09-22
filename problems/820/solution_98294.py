def posLetra(frase: str, letra: str, n: int) -> int:
    """Dada uma frase, uma letra e um número indicando a
    enésima ocorrência da letra na frase, retorna a posição
    da string em que essa ocorrência se encontra.
    Caso a ocorrência pedida(n) seja maior do que o número de
    ocorrências existentes da letra na frase, o retorno será -1."""
    
    i = 0
    posicoes_letra =[]
    
    
    while (i < len(frase)):
        if (frase[i] == letra):
            list.append(posicoes_letra, i)
        i += 1
    if (len(posicoes_letra)  < n):
        return -1
    else:
        return posicoes_letra[n-1]