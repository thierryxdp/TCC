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
    hh=fras4.split()
    aa=len(hh)
    i=0
    bb=list(hh)
    cc=[]
    while i<=aa:
        cc.append(bb[i])
        i=i+1
  
  
    return cc