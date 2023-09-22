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
    c=str.replace(b,'E','e')
    d=str.replace(c,'I','i')
    e=str.replace(d,'O','o')
    f=str.replace(e,'U','u')
    
    
    x= f.capitalize()
    
    
    
    
    
    
    return x