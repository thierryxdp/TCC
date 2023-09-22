def conta_frases(texto):
    '''funcao que dada um texto retona 
    a quantidade de frases.
    entrada: string
    saida: inteiro
    '''
    split= texto.split(',')
    return len(split)