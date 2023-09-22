def retira_pontuacao(frase):
    x = frase.replace( '.'," ")
    y = frase.replace( '!'," ")
    z = frase.replace('?'," ")
    w = str("  ")
    if ',' in frase and '-' in frase and '.' in frase:
        return w
    elif '.' in frase:
        return x 
    elif '!' in frase:
        return y
    elif '?' in frase:
        return z