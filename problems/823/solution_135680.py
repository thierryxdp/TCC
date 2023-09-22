def faltante(L):
    L_corrigida = L.sort()
    auxiliar = []
    i = 1
    
    while i<len(L_corrigida)+1:
        auxiliar.append(i)
        if L_corrigida[i]!=auxiliar[i]:
            return i