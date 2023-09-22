def posLetra(frase, letra, ocorrencia):
    """ Dada uma frase, uma letra, e um número representando uma ocorrência,
    itera por meio da frase verificando se aquele caractere é igual a letra,
    se for, vai ser adicionado +1 ao contador, e se o contador for igual ao
    número de ocorrência passado, retorna a posição do caractere, caso contrário,
    realiza mais uma iteração realizando as mesmas operações, e retorna -1 ao final da iteração.
    str, str, int -> int
    """
    tamanhoFrase = len(frase)
    contador = 0
    i = 0
    while i != tamanhoFrase:
        if(frase[i] == letra):
            contador += 1
            if(contador == ocorrencia):
                return i
        i += 1
    return -1