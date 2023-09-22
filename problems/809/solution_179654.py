def intercala(lista1, lista2):
     """intercala duas listas 
     lista, lista --> lista"""
    a = ['tuvxyz','tuvxyz','tuvxyz','tuvxyz','tuvxyz','tuvxyz']
    b = lista1
    c = lista2
    a[0] = b[0]
    a[1] = c[0]
    a[2] = b[1]
    a[3] = c[1]
    a[4] = b[2]
    a[5] = c[2]
    return a