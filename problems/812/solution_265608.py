def retira_pontuacao(frase):
    a='-'
    b=','
    c=':'
    d=';'
    e='.'
    f='?'
    g='!'
    h='...'
    for i in range(0,len(frase)):
        a=a.replace(frase[i],' ')
    for i in range(0,len(frase)):
        b=b.replace(frase[i],' ')
    for i in range(0,len(frase)):
        c=c.replace(frase[i],' ')
    for i in range(0,len(frase)):
        d=d.replace(frase[i],' ')
    for i in range(0,len(frase)):
        e=e.replace(frase[i],' ')
    for i in range(0,len(frase)):
        f=f.replace(frase[i],' ')
    for i in range(0,len(frase)):
        g=g.replace(frase[i],' ') 
    for i in range(0,len(frase)):
        h=h.replace(frase[i],' ')    

    return frase