def intercala[x1,x2,x3],[x4,x5,x6]:
    """Duas listas: l1 e l2 geram uma lista l3, intercalando os elementos de l1 e l2;
    list, list -> list"""
    
    l1 = [x1,x2,x3]
	l2 = [x4,x5,x6]
    
    return [l1[0],l2[0],l1[1],l2[1],l1[2],l2[2]]