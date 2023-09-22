def posLetra(s, l, n):
    '''
    Esta função recebe uma string (str), uma letra (str) e um número (int) que indique a ocorrência desejada da letra.
    Retorna a posição da string (int) em que a ocorrência informada se encontra. 
    Se houver menos ocorrências do que o número de ocorrências informado, será retornado -1
    '''
    i = 0
    c = 0
    if n > s.count(l):
        return -1
    while i <= len(s):
        if s[i] == l:
            c += 1
        if c == n:
            return i
        i += 1