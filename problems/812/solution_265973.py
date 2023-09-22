def retira_pontuacao(frase):
    '''Dada uma frase, a função substitui todos os caracteres
    de pontuação por espaço. str -> str'''
    a=frase.split('!')
    b=' '.join(a)
    c=b.split('?')
    d=' '.join(c)
    e=d.split('...')
    f=' '.join(e)
    g=f.split('.')
    h=' '.join(g)
    i=h.split(':')
    j=' '.join(i)
    k=j.split(';')
    l=' '.join(k)
    m=l.split(',')
    n=' '.join(m)
    o=n.split('-')
    p=' '.join(o)
    return p