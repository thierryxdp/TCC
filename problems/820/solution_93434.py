def posLetra(string,letra,numero):
    '''Dada uma string, uma letra e um número que indica a ocorrencia desejada da letra, retorna uma posição da string que aquela letra está
    str,str,int -> int'''
    i = 0
    vezes = 0
    while i < len(string):
        if string[i] == letra:
            vezes = vezes + 1
            if vezes == numero:
                return i
        i = i+1
    return -1