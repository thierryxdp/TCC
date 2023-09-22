def conta_frases(frase):
    """A função contará o número de frases a partir da string
    escolhida como parametro para tal função. Considerando que
    cada frase no texto é terminada com um ponto final, um 
    ponto de exclamação, um ponto de interrogação ou 
    reticências.
    Entrada: String
    Saída: Int"""
    
    frase = (frase.partition(frase.replace('.', ' ')))
    frase = (frase.partition(frase.replace('!', ' ')))
    frase = (frase.partition(frase.replace('?', ' ')))
    frase = (frase.partition(frase.replace('...', ' ')))
    frase = (frase.partition(frase.replace('-', ' ')))
    frase = (frase.partition(frase.replace(',', ' ')))
    frase = (frase.partition(frase.replace(';', ' ')))
    frase = (frase.partition(frase.replace(':', ' ')))
    
    return frase