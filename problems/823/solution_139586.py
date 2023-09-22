def faltante(quebra_cabeca):
    n = len(quebra_cabeca) + 1
    faltando = n
    quebra_cabeca.sort()
    
    for i in range(1,n):
        if(quebra_cabeca[i-1] !=1):
        faltando = i
        break
    return faltando