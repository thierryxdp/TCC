def retira_pontuacao(frase):
    frase= frase.str.replace(' ',',')
    frase= farse.str.replace(' ','/')
    frase= frase.str.replace(' ',';')
    frase= frase.str.replace(' ',':')
    frase= frase.str.replace(' ','.')
    frase= frase.str.replace(' ','?')
    frase= frase.str.replace(' ','!')
    frase= frase.str.replace(' ','-')
    return frase