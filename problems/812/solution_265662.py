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
        fra=y.replace(c,' ')
    for i in d:
        fras=fra.replace(d,' ')
    for i in e:
        fras1=fras.replace(e,' ')
    for i in f:
        fras2=fras1.replace(f,' ')
    for i in g:
        fras3=fras2.replace(g,' ')
    for i in h:
        fras4=fras3.replace(h,' ')
    return fras4