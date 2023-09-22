def retira_pontuacao(frase):
    """Função na qual dada uma frase, retorna a mesma frase substintuindo sua pontuacao por espacos vazios"""
    txt = frase.split(',')
    frase = ' '.join(txt)
    txt = frase.split('.')
    frase = ' '.join(txt)
    txt = frase.split('-')
    frase = ' '.join(txt)
    txt = frase.split(':')
    frase = ' '.join(txt)
    txt = frase.split(';')
    frase = ' '.join(txt)
    txt = frase.split('!')
    frase = ' '.join(txt)
    txt = frase.split('?')
    frase = ' '.join(txt)
    return frase