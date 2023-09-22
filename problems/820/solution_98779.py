def posLetra(string, letra, num):
    '''Recebe uma string, uma letra e um número que
    indica a ocorrência desejada da letra e retorna 
    a posição da string em que aquela ocorrência está
    str, str, int -> int'''
    pos = -1
    i = 0
    j = 1
    while i < len(string) and j<= num:
        if string[i] == letra:
            if j == num:
                pos = i
            j += 1            
        i += 1
    return pos