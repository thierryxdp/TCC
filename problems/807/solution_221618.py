def conta_frase(texto):
    '''Recebe um texto e retorna a quantidade de frases nele
       str -> int
    '''
    return len(texto.split([".", "!", "?", "..."]))