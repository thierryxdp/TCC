def eh_quadrada(m):
    j=0
    k=0
    for i in m:
        j+=1
        for e in i:
            k+=1
            if k==j:
                return True
            if k!=j:
                return False