def conta_frases(f):
    c1=str.count(f,"!")
    c2=str.count(f,"?")
    c3=str.count(f,"...")   
    c4=str.count(f,".")
    soma=c1+c2+c3+c4
    return soma