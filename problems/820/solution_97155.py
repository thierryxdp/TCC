def posLetra(string, letra, numero):
    ''' função que recebe como entrada uma string, uma letra e um número indicando a ocorrência da letra, e retorna em que posição da frase aquela ocorrência se encontra;
	str, str, int -> int '''
    x = 0
    for y in range(len(string)): 
        if (string[y] == letra): 
            x = x+1

        if (x == numero): 
            return y

    return -1