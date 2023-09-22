def retira_pontuacao(frase):
    x = frase.replace( '.'," " )
    y = frase.replace( '!'," " )
    return (x,y)