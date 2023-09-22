def conta_frases(texto):
    """Função que conta o número de frases que aparecem no texto. Cada frase no texto
    ́e terminada com um ponto final, um ponto de exclamação, um ponto de interrogação
    ou reticências. Pontos de exclamação ou de interrogação não
    aparecem ̃repetidos em sequência no texto e esses símbolos só aparecem no
    texto terminando uma frase.
    str -> int
    """
    
    invert_txt= str.replace(str.replace((texto.replace('?','.')),'!','.'),'...','.')

    return len(invert_txt.split('.'))-1