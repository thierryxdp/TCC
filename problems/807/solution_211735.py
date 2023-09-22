def conta_frases(texto):
    '''Retorna a quantidade de frases presentes no texto entregue
    strins -> int'''
    n1=0
    n2=0
    n3=0
    n4=0
    n1=str.count(texto,".")
    n2=str.count(texto,"...")
    n3=str.count(texto,"!")
    n4=str.count(texto,"?")
    n=n1+n3+n4+n2+(-3*n2)
    return n