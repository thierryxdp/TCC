def retira_pontuacao(frase):
    '''
    funcao utilizada para retornar onde  os caracteres
    de pontuacao foram substituidos por espaço
    '''
    a=str.join(' ',str.split(frase,'.'))
    b=str.join(' ',str.split(a, ','))
    c=str.join(' ',str.split(b, '?'))
    d=str.join(' ',str.split(c, '!'))
    e=str.join(' ',str.split(d, '-'))
    return e