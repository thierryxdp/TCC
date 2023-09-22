def posLetra(string, letra, numero):
    '''dada uma string, uma letra e um numero retorna em que posição da string aquela ocorrência da letra está
    string, string, int -> int'''
    x = str.index(string, letra, numero)
    return x