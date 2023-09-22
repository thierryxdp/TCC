def conta_frases (frase):
    '''
    	essa função recebe várias frases e as conta. No final de cada frase há
        um ponto final, exclamação, interrogação ou reticências
    '''
    str.replace (frase, '!', '.')
    return frase.count(frase, '.')