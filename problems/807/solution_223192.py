def conta_frases(frase):
    frase1=str.replace(frase,'...','.')
    nump=str.count(frase1,'.',)
    numex= str.count(frase1','!',)
    numin= str.count(frase1','?',)
    
    
    return nump+ numex+numin