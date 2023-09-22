def posLetra(frase, l, x):
    """ recebe como entrada uma string, uma letra e um numero que indica a a ocorrencia desejada, retorna a posicao daquela ocorencia que a letra está
str,str,int -> int"""
    y = 0
    z = 0
    a = list(frase)
    if list.count(a, l) < x:
        return -1
    else:
        while y < x:
            if frase[z] == l:
                y = y + 1
            else:
                None
            z = z + 1
        return z - 1