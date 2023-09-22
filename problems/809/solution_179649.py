def intercala(lista1, lista2):
     """intercala duas listas 
     lista, lista --> lista"""
	L3=['abcde','abcde','abcde','abcde','abcde','abcde']
    L1 = lista1
    L2 = lista2
    L3[0] = L1[0]
    L3[1] = L2[0]
    L3[2] = L1[1]
    L3[3] = L2[1]
    L3[4] = L2[2]
    L3[5] = L2[2]
        return L3