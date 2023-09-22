def conta_frases(frase):
    nump= str.count(frase,'.',0:)
    numex= str.count(frase,'!',0:)
    numin= str.count(frase,'?',0:)
    numret= str.count(frase,'...',0:)
    return nump+numex+numin+numret