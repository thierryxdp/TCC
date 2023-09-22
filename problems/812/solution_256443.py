def retira_pontuacao(frase):
    x = frase.replace( '.'," " )
    y = frase.replace( '!'," " )
    z = frase.replace( "  " )
    
   
    if '.' in frase:
        return x 
    elif '!' in frase: