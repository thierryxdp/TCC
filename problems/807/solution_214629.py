def conta_frases(texto):
    '''função que dado um texto em string, retorna a quantidade de frases
       contidas neste texto. str -> int'''
    return len(str.split(texto,'.','...','!','?'))