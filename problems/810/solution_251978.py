def inverte(s):
    a=str.replace(s,"-"," ")
    b=str.replace(a,","," ")
    c=str.replace(b,":"," ")
    d=str.replace(c,";"," ")
    e=str.replace(d,"."," ")
    f=str.replace(e,"?"," ")
    g=str.replace(f,"!"," ")
    h=str.lower(g)
    i=str.split(h)
    j=list.reverse(i)
    
    
    return j