def faltante(l1):
    i=2
    inteiro=0
    while i<len(l1):
        if l1[i]!=i:
            return i
        else:
            return len(l1)+1
        i+=i+1