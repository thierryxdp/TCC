def posLetra(string, letra, num):
    """Função que recebe uma string, uma letra e um número que indica a ocorrência desejada da letra. Retorna em que 
    posição da string aquela letra está. Caso exista menos ocorrências da letra do que a ocorrência pedida, a função 
    deve retornar -1.
    str, str, int -> int"""
    i = 0
    ocorrencia = 0
    while (ocorrencia < num and i < len(string)):
        if letra in string[i]:
            ocorrencia = ocorrencia + 1
            pos = i
        i = i + 1
    if ocorrencia < num:
        pos = -1
    return pos