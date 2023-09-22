def posLetra(string, let, num):
    '''
    Funcao que recebe uma string, uma letra e um numero que indica a ocorrencia. A funcao retorna a posicao da string em que aquela
    ocorrencia esta.
    str, str, int -> int
    '''
    frase_lista = string.split(let)
    num_car = len(frase_lista) - 1
    if num_car >= num:
        fr = ''.join(frase_lista[0:num])
        return len(fr) + num - 1
    else:
        return -1