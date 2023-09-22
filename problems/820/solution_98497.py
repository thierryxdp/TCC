def posLetra(frase: str, letra:str, ocorrencias:int)-> int:
    """Essa função, dada uma string, uma letra e um número que indica
    ocorrência, retorna em que posição da string aquela ocorrência da 
    letra está""""
    i = 0
    posicao = 0
    while i < len(frase):
        if frase[i] == letra:
            posicao = posicao + 1
            if posicao == ocorrencias:
                ocorre = frase.index(frase[i], i)
                return ocorre
        i += 1
    else:
        return -1