def retira_pontuacao(frase):
    '''função retorna retira a pontuação existente na frase e substitue por espaços'''
    espaco = ' '
    frase = frase.split('-')
    frase = espaco.join(frase)
    frase = frase.split(',')
    frase = espaco.join(frase)
    frase = frase.split(':')
    frase = espaco.join(frase)
    frase = frase.split(';')
    frase = espaco.join(frase)
    frase = frase.split('.')
    frase = espaco.join(frase)
    frase = frase.split('!')
    frase = espaco.join(frase)
    frase = frase.split('?')
    frase = espaco.join(frase)
    return (''.join(frase))