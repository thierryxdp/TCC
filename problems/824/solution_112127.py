def uppCons(frase):
    b=[]
    c=[]
    d=[]
    e=[]
    
    a=str.upper(frase)
    subV=['A','E','I','O','U']
    subN=['a','e','i','o','u']
    fpartida= str.split(a)
    b=str.replace(a,'A','a')
    c=str.replace(b,'B','b')
    d=str.replace(c,'C','c')
    e=str.replace(d,'D','d')
    f=str.replace(e,'E','e')
    
    
    
    return f