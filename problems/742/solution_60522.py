def substitui(s,x,i):
    """ dada uma string, um caractere e um inteiro(entre 0 e o tamanho da str)
        vamos substituir o elemento da posição i pelo caractere dado
        entrada -->str, int
        saida --> str """
    return s[0:i] + x + s[i + 1:]