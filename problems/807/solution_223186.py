def conta_frases(frase):
    nump=str.count(frase,'.',)
    numex= str.count(frase,'!',)
    numin= str.count(frase,'?',)
    numret= str.count(frase,'...',)
    return (nump-3)+ numex+numin+numret