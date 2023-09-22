def inverte(frase):
    '''funcao que inverte um frase dada como
    parametro.
    entrada: string
    saida: string
    '''
    p= string.punctuation
    s= frase.replace(p, " ")
    m= s.lower()
    return m[::-1]