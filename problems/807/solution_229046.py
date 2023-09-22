def conta_frases(texto):
    
    texto1=str.join('*',str.split(texto,'...')) 

    return str.count(texto1,'.')+str.count(texto1,'?')+str.count(texto1,'!')+str.count(texto1,'*')