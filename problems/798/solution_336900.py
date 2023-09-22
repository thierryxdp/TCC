def freq_palavra(frase):
    """retorna a quantidade de cada palavra aparece em cada frase
    str->dict"""
    contador = {}
    
    frase = frase.split()
    
    for palavra in frase:
        if palavra in contador:
            contador[palavra] = contador[palavra]+1
    
    return contador