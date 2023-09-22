def conta_frases (frase):
    '''
    	essa função recebe várias frases e as conta, colocando no final de cada frase 
        um ponto final, exclamação, interrogação ou reticências
    '''
    frase = frase.split()
    return len(frase) + '.'