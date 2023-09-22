def conta_frases(texto):
    '''conta o número de frases presente em um texto, de acordo com a
    pontuaçao final presente em cada frase.
    str -> int'''
    
    pontuacao = ["!", "?", ".", "..."]
    
    frases = str.partition(texto, pontuacao)
    
    quantidade = str.count(frases)
    
    return quantidade