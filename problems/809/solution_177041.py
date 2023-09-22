def intercala(n1,n2,n3,n4,n5,n6):
    """Duas listas: l1 e l2 geram uma lista l3, intercalando os elementos de l1 e l2;
    list, list -> list"""
    
    l1 = [n1,n2,n3]
	l2 = [n4,n5,n6]
    
    return [l1[0],l2[0],l1[1],l2[1],l1[2],l2[2]]