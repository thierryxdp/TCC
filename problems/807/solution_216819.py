def conta_frases(texto):
    '''conta o número de frases presente em um texto, de acordo com a
    pontuaçao final presente em cada frase.
    str -> int'''
    
    frases = str.partition(texto, "!", "?", ".", "...")
    
    quantidade = str.count(frases)
    
    return quantidade