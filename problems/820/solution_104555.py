def posLetra(string,letra,n):
    '''Recebe uma string, uma letra e um número que indica a enésima ocorrência da letra inserida na string inserida e retorna o índice da string em que essa letra aparece. Caso a letra não apareça, a função deve retornar -1;
    str, str, int -> int'''

    i = 0
    oc = 0

    while i < len(string):
        if string[i] != letra:
            oc = 0
            i = i + 1
        elif string[i] == letra:
            oc = oc + 1
            i = i + 1
        if oc == n:
            return i - 1
    else:
        return -1