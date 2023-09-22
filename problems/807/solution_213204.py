def conta_frases(texto):
   x=str.replace(str.replace(str.replace(str.replace(texto,'...','#'),'.','#'),'!','#'),'?','#)
   return str.count(x,'#')
                 
 def conta_frases(texto):
 s=texto
    for x in ['...']:
        a=str.replace(s,x,'#')
    for x in ['!']:
        b=str.replace(s,x,'#')
    for x in ['?']:
        c=str.replace(s,x,'#')
    for x in ['.']: 
        d=str.replace(s,x,'#")
        return str.count(a+b+c+d,'#')