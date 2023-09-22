def faltante(l1):
    i=0
    inteiro=0
    while i<len(l1):
        if l1[i]!=i+1:
            inteiro=i
        else:
            inteiro=len(l1)+1
        i+=i+1
    return inteiro