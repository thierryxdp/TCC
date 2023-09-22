def posLetra(string, letra, numero):
    '''dada uma string, uma letra e um numero retorna em que posição da string aquela ocorrência da letra está
    string, string, int -> int'''
    lista = str.split(string, " ")
    if letra in lista[numero -1]:
        return str.index(lista[numero], letra)
    else: 
        return -1