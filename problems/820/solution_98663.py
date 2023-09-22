def posLetra(string,letra,n):
    '''Recebe uma string, uma letra e um número n e indica o índice da aparação número n
    da letra escolhida, caso existam menos ocorrencias da letra do que a posição pedida
    retorna -1;  str, str, int -> int'''
    i = 0
    a = ''
    b = ''
    while i < len(string):
        if string[i] == letra:
            a = a + letra
            b = b + str(i)
        i += 1
    if len(a) < n:
        return -1
    elif len(a) >= n:
        return int(b[-1])