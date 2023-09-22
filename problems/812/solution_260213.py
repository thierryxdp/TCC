def retira_pontuacao(frase):
    """Função onde dada uma frase, retira todas as pontuações que nela existe"""
    """str -> str"""
    frase = frase.split('-')
    frase = ' '.join(frase)
    frase = frase.split(',')
    frase = ' '.join(frase)
    frase = frase.split(':')
    frase = ' '.join(frase)
    frase = frase.split(';')
    frase = ' '.join(frase)
    frase = frase.split('.')
    frase = ' '.join(frase)
    return frase