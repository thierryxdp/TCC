def retira_pontuacao(frase):
    x = frase.replace( '.'," " )
    y = frase.replace( '!'," " )
    
  
    if '.' in frase:
        return x 
    elif '!' in frase:
        return y
    elif frase == str('!') and frase ==(',') and frase ==('.') :
        return str('')