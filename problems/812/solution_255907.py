def retira_pontuacao (frase):
    """ utilizando a funçao replace para substituir a 
    pontuação que eu não quero por espaço"""
    frase = frase.replace('!', ' ')
    frase = frase.replace('...', ' ')
    frase = frase.replace('.', ' ')
    frase = frase.replace('?', ' ')
    frase = frase.replace('_', ' ')
    frase = frase.replace(':', ' ')
    frase = frase.replace('-', ' ')
    frase = frase.replace(',' , ' ')
    return frase