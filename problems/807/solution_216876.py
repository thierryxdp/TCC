def conta_frases(texto):
    '''conta o número de frases presente em um texto, de acordo com a
    pontuaçao final presente em cada frase.
    str -> int'''
    
    
    valor = texto.count("!") + texto.count("?") + texto.count("...")+ texto.count('.')
    ret = texto.count("...")*3
    
    return valor - ret