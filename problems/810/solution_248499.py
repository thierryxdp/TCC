def retira_pontuacao(texto):
    '''função que substitui as pontuações por espaços
    str->str'''
    a=' '.join(texto.split(','))
    b=' '.join(a.split('-'))
    c=' '.join(b.split(':'))
    d=' '.join(c.split(';'))
    e=' '.join(d.split('.'))
    f=' '.join(e.split('!'))
    g=' '.join(f.split('?'))
    
    return g

def inverte(texto):
    a=retira_pontuacao(texto).split(' ')
    a=a.reverse()
    texto_f=(' '.join(a)).replace('  ',' ')
    return texto_f.lower()[1:]