def faltante(L):
    i=0
    jota=0
    while i<len(L):
        if L[i]==L[i+1]:
            jota=jota+2
            i=i+1
        return jota