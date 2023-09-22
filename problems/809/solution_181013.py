def intercala(lista1, lista2):
    '''calcula intercalada dos elementos da lista1 e lista2
    list[float,float,float],list[float,float,float]->
    list[float,float,float,float,float,float]'''
    
    len(lista1)==3
    L1=lista1
    
    len(lista2)==3
    L2=lista2
    
    L3=L1[0]+L2[0]+L1[1]+L2[1]+L1[2]+L2[2]
    
    return L3