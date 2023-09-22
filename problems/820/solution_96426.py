def posLetra(string, letra, ocorrencia):
    '''Função que recebe uma string, uma letra e um número indicando
a ocorrência desejada da letra na string e retorna o índice da 
ocorrência da letra. Caso não haja ocorrências suficientes da letra,
retorna -1.
Entradas:
    string, letra: str
    ocorrencia: int
Saída:
    int'''
    n = 0
    i = 1
    while i < ocorrencia:
        if letra in string[n:]:
            n = string.index(letra, n)
            i += 1
        else:
            i = ocorrencia
            n += 1
    return string.find(letra, n)