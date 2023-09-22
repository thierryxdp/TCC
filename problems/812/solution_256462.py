def retira_pontuacao(frase):
    x = frase.replace( '.'," ")
    y = frase.replace( '!'," ")
    z = frase.replace('?'," ")
    w = frase.replace(',' and '-' ," ")
                      
    
  
    if '.' in frase:
        return x 
    elif '!' in frase:
        return y
    elif '?' in frase:
        return z
    elif ',' and '-' in frase:
        return