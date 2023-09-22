def retira_pontuacao(frase):
    frase = ' '.join(frase.split('-'))
    frase = ' '.join(frase.split(';'))
    frase = ' '.join(frase.split(':'))
    frase = ' '.join(frase.split(','))
    frase = ' '.join(frase.split('.'))
    frase = ' '.join(frase.split('?'))
    frase = ' '.join(frase.split('!'))
    return frase

def inverte(frase):
    frase = retira_pontuacao(frase).strip()
    return ' '.join(frase.split(' ')[::-1])