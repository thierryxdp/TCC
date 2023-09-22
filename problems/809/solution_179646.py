def intercala(lista1, lista2):
     """intercala duas listas 
     lista, lista --> lista"""
        L3 = ['abc','abc','abc','abc','abc','abc']
        L1 = lista1
        L2 = lista2
        L3[0] = L1[0]
        L3[1] = L2[0]
        L3[2] = L1[1]
        
        return L3