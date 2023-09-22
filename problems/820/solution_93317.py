def posLetra(string, letra, num):
    '''funçãoque recebe uma string, uma letra e um número que indica a 
    ocorrência desejada da letra. A função retorna em que posição da string
    aquela ocorrência da letra está. Caso exista menos ocorrências da letra
    do que a ocorrência pedida, a função retorna -1; str, str, int -> int'''
    ocorrencias = str.count(string,letra)
    if ocorrencias < num:
        return -1
    else:
        nova_string = str.replace(string,letra,'#',num-1)
        indice = str.index(nova_string,letra)
        return indice