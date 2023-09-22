def inverte(s):
    a=str.replace(s,"-"," ")
    b=str.replace(a,","," ")
    c=str.replace(b,":"," ")
    d=str.replace(c,";"," ")
    e=str.replace(d,"."," ")
    f=str.replace(e,"?"," ")
    g=str.replace(f,"!"," ")
    h=str.lower(g)
    i=h.split()
    j=list.reverse(i)
    
    for palavras in j:
        u+= palavras
    
    
    return u