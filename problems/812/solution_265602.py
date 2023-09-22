def retira_pontuacao(frase):
    frase = ' '.join(frase.split('-'))
    frase = ' '.join(frase.split(';'))
    frase = ' '.join(frase.split(':'))
    frase = ' '.join(frase.split(','))
    frase = ' '.join(frase.split('.'))
    frase = ' '.join(frase.split('?'))
    frase = ' '.join(frase.split('!'))
    return frase