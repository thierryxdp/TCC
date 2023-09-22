def posLetra(frase,letra,num):
    """
    Dada uma frase e uma letra, o numero diz qual a ocorrencia dessa
    letra na frase (ex: se num = 3, trata-se da terceira vez que 'letra'
    aparece) e retorna-se a posicao na string em que essa ocorrencia se
    encontra
    Entradas:
    	frase, letra: strings
        num: int
    Returns:
    	int
    """
    i = 0
    indice = []
    while i<len(frase):
        if frase[i] == letra:
            indice = indice + [i]
            i = i + 1
        return int(indice[num-1])