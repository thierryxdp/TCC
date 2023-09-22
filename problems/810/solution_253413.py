def retira_pontuacao(frase):
    a='-'
    b=','
    c=':'
    d=';'
    e='.'
    f='?'
    g='!'
    h='...'
    for i in a:
        z=frase.replace(a,' ')
    for i in b:
        y=z.replace(b,' ')
    for i in c:
        x=y.replace(c,' ')
    for i in d:
        w=x.replace(d,' ')
    for i in e:
        v=w.replace(e,' ')
    for i in f:
        u=v.replace(f,' ')
    for i in g:
        t=u.replace(g,' ')
    for i in h:
        s=t.replace(h,' ')
    return s

def inverte(frase):
    retira_pontuacao(frase) = l
    l = l.lower() 
    r = frase.split()
    q = len(r)
    p = 0
    o = list(r)
    n =[]
    while p < q:
        n.append(o[(q - 1) - p])
        p=p+1
    m =' '.join(n)    
    return m