def inverte(frase):
    '''Dada uma frase, a função retorna uma outra frase 
    contendo as mesmas palavras da frase de entrada na ordem
    inversa, sem letras maiúsculas e sem pontução.
    str -> str'''
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
    p=p.lower()
    q=p.split()
    r=' '.join(q[::-1])
    return str.strip(r)