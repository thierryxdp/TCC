def retira_pontuacao(frase):
    """ função recebe frase com entrada retira as pontuações com metodo replace e devolve a frase"""
    frase = frase.replace('!',' ')
    frase = frase.replace('?',' ')
    frase = frase.replace(',',' ')
    frase = frase.replace('.', ' ')
    frase = frase.replace('-', ' ')
    return frase