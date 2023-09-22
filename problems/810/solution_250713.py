def inverte(frase):
    a='-'
    b=','
    c=':'
    d=';'
    e='.'
    f='?'
    g='!'
    yy='...'
    for i in a:
        h=frase.replace(a,' ')
    for i in b:
        fr=h.replace(b,' ')
    for i in c:
        fra=fr.replace(c,' ')
    for i in d:
        fras=fra.replace(d,' ')
    for i in e:
        fras1=fras.replace(e,' ')
    for i in f:
        fras2=fras1.replace(f,' ')
    for i in g:
        fras3=fras2.replace(g,' ')
    for i in yy:
        fras4=fras3.replace(yy,' ')
    fras4=fras4.lower()
    frash=''
    for i in fras4.split(' '):
        frash += i[::-1]+' '
    frash[::-1]    
        
    return frash