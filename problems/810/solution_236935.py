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
    nova_frase = frase.lower()
    nova_frase_2 = retira_pontuacao(nova_frase)
    l = nova_frase_2.split(' ')
    l.reverse()
    del(l[0])
    return ' '.join(l)