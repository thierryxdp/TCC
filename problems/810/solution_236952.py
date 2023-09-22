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

def inverte(frase):
    """Função na qual dada uma frase retorna a mesma frase de tras para frente e com todas as letras minusculas"""
    l = frase.split
    l.reverse
    return l