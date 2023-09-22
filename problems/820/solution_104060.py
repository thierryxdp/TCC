def posLetra(string="",letra="", num=0):
    '''função que recebe uma string, uma letra
    e um número e indica a ocorrência desejada da letra, e
    retorna a posição da ocorrência da letra na string
    str -> int'''
    if (string.count(letra)>=num):
        lista = list(string)
        for i in range(num-1):
            numb = int(lista.index(letra))
            lista[numb] = " "
        string = "".join(lista)
        return string.index(letra)

    return -1