def conta_frases(frase):
    
    return str.count(str.strip(frase),'.')+str.count(str.strip(frase),'?')+str.count(str.strip(frase),'!')+str.count(str.strip(frase),'...')