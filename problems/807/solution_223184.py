def conta_frases(frase):
    
    numex= str.count(frase,'!',)
    numin= str.count(frase,'?',)
    numret= str.count(frase,'...',)
    return +numex+numin+numret