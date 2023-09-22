def posLetra(string,letra,n):
    '''Função que recebe uma string, uma letra e um número que indica a ocorrência da letra desejada e retorna em que posição da string aquela ocorrência da letra está, caso existo menos occências da letra do que a ocorrência pedida, a função retorna -1. str,str,int -> int'''
    i = 0
    cnt = 0
    while i < len(string):
        if string[i] == letra:
            cnt += 1
            if cnt == n:
                return i
        i += 1
        if n > cnt:
                return -1
    return i