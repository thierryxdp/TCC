def conta_frases(frase):
    frase1=str.replace(frase,'...','.')
    nump=str.count(frase1,'.',)
    numex= str.count(frase','!',)
    numin= str.count(frase','?',)
    
    
    return (nump)+ numex+numin