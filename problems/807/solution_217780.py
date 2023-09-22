def conta_frases(txt):
    frase= str.split(txt,'...')
    n1=len(frase)
    frase2=str.split(frasek,'.')
    n2=len(frase2)
    frase3=str.split(txt,'?')
    n3=len(frase3)
    frase4=str.split(txt,'!')
    n4=len(frase4)
    nk=(n2)-((3*n1)-1)
    nT=(n1-1)+(n2-1)+(n3-1)+(n4-1)
    return nT