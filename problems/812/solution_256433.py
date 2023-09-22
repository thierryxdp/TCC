def retira_pontuacao(frase):
    x = frase.replace( '.'," " )
    y = frase.replace( '!'," " )
    
    if frase in ".":
        return x