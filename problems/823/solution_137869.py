def faltante(n):
    i=0
    inteiro=0
    while i <len(n):
        if n[i] == i+1:
            inteiro = len(n)+1
        elif n[i]!=i+1:
            inteiro = i+1
        i=i
    return inteiro