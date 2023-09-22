def intercala(L1, L2):
    'Função que intercala duas listas e devolve a terceira lista em ordem crescente'
    n1 =len(L1)
    n2 =len(L2)
    i= 0
    j= 0
    L3 =list([])
    while i<n1 and j<n2:
        if L1[i]<L2[j]:
            L3.append(L1[i])
            i=i+1
        else:
            L3.append(L2[j])
            j=j+1
    while i<n1:
        L3.append(L1[i])
        i=i+1
    while j<n2:
        L3.append(L2[j])
        j=j+1
    return L3