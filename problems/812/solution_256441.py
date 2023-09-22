def retira_pontuacao(frase):
    x = frase.replace( '.'," " )
    y = frase.replace( '!'," " )
    z = frase.replace( "  " )
    
    if ',' and '-' in frase:
        return
    if '.' in frase:
        return x 
    elif '!' in frase:
        return y
    elif "," in frase:
        return w