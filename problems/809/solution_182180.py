def intercala(lista1, lista2):
    L1 = [2,5,8]
    L2 = [4,9,7]
    L3 = L1[:1] + L2[:1] + L1[1:2] + L2[1:2] + L1[1:3] + L2[1:3] + L1[2:3] + L2[2:3]
    """"""
    return L3