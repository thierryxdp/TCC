def intercala(lista1, lista2):
    """
    
    
    """
             
    L1=lista1
    L2=lista2
    L1_1=[lista1[0]] + [lista2[0]] + [lista1[1]]
    L2_2=[lista2[0]] + [lista1[0]] + [lista2[1]]
    L3= L1_1+L2_2
    L1_2=lista1[:1] + lista2[:1] + lista1[2]
      
    return L1_2