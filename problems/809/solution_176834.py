def intercala(L1,L2):
    """Coloque um comentário dizendo o que a função faz e quais são os parâmetros de entrada e saída"""
    n1 =len(L1)
    n2 =len(L2)
    i = 0
    j = 0
    L3 =list([])
    while i<n1 and j<n2:
        if L1[i]<L2[j]:
            L3.append(L1[i])
            i=i+i
            return L3