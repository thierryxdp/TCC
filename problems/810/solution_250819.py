def retira_pontuacao(frase):
    """"Função que dada uma frase, retorna uma nova frase com toda a pontuação subistituida por " ".
    casos de teste:
    entrada:"Era uma vez, e assim se fez." saida:"Era uma vez  e assim se fez "
    entrada:"Vá embora, agora!" saida:"Va embora  agora "
    entrada:"Vou-lhe dar uma segunda chance, mas será a última." saida "Vou lhe dar uma segunda chance  mas sera a última "
    assinatura: str -> str"""
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
    """Função que dada uma frase, retornara outra fase com as mesmas palavras da frase original de forma invertida, sem letra maiúsculas, e sem a pontuação.
    casos de teste:
    entrada:"Era uma vez, e assim se fez." saida:"fez se assim e vez uma era" "
    entrada:"Vá embora, agora!" saida:"agora embora vá"
    entrada:"Vou-lhe dar uma segunda chance, mas será a última." saida: "última a será mas chance segunda uma dar lhe vou"
    assinatura: str -> str"""
    l = retira_pontuacao(frase)
    l = l.lower() 
    r = l.split()
    q = len(r)
    p = 0
    o = list(r)
    n =[]
    while p < q:
        n.append(o[(q - 1) - p])
        p=p+1
    m =' '.join(n)    
    return m