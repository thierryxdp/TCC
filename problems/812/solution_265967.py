def retira_pontuacao(frase):
    ''' Retorna a frase onde todos os caracteres de pontuação são substituidos
        por espaço.
        str-> str'''
    f=frase.split('!')
    f=' '.join(f)
    f=f.split('?')
    f=" ".join(f)
    f=f.split(',')
    f=" ".join(f)
    f=f.split('.')
    f=" ".join(f)
    f=f.split(';')
    f=" ".join(f)
    f=f.split(':')
    f=" ".join(f)
    f=f.split('-')
    f=" ".join(f)

    return f