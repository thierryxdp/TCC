def retira_pontuacao(frase):
    frase= str.split(frase)
    frase= str.replace(' ',',')
    frase= str.replace(' ','/')
    frase= str.replace(' ',';')
    frase= str.replace(' ',':')
    frase= str.replace(' ','.')
    frase= str.replace(' ','?')
    frase= str.replace(' ','!')
    frase= str.replace(' ','-')
    return frase