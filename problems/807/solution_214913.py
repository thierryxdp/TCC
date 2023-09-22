def conta_frases(frase):

    s=frase
    lista1=str.split(s,'...')
    s1=str.join('',lista1)
    
    

    a = int(str.count(s1,'.'))
    b = int(str.count(s1,'!'))
    c = int(str.count(s1,'?'))
    d = int(str.count(s,'...'))
      
    return a+b+c+d