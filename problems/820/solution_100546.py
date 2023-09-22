def posLetra(texto,letra,ocorrencia):
    '''recebe uma string, uma letra e um número. O número indica a ocorrência desejada da letra. A função deve retornar em que posição da string aquela ocorrência da letra está. Caso exista menos ocorrências da letra do que a ocorrência pedida, a função deveretornar -1'''
    '''str, str, int -> int'''
    i = 0
    n = 0
    while i<len(texto) and n<ocorrencia:
        if texto[i] == letra:
            n = n +1
        i = i + 1