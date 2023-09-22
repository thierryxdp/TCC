def conta_frases(texto):
    frase=str.split(texto,'...')
    n1=len(frase)
    frase2=str.split(texto,'.')
    n2=len(frase2)
    frase3=str.split(texto,'?')
    n3=len(frase3)
    frase4=str.split(texto,'!')
    n4=len(frase4)
    np=((n2)-(3*(n1-1)))
    nt=(n1-1)+(np-1)+(n3-1)+(n4-1)
    return nt