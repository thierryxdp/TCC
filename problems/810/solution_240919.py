def inverte(frase):
    '''funcao que inverte um frase dada como
    parametro.
    entrada: string
    saida: string
    '''
    remove_pont= frase.split(',')
    string= " ".join(remove_pont)
    return string[::-1]