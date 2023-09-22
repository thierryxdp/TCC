def intercala(lista1, lista2):
    """
    
    
    """
             
    L1=lista1
    L2=lista2
    L1_1=[lista1[0]] + [lista2[0]] + [lista1[1]]
    L2_2=[lista2[0]] + [lista1[0]] + [lista2[1]]
    L3= L1_1+L2_2
    intercalada = L1 [::2] + L2[1::2]
      
    return intercalada