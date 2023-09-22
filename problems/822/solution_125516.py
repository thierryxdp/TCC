def repetidos(lis):
    """Recebe uma lista de números e retorna o número de vezes que um elemento da lista é igual ao elemento anterior. List-->Int"""
    i=0
    nlis=[]
    
    
    while (i<int(len(lis))):
        if int(lis[i])==int(lis[i-1]):
            nlis= nlis+[1]
            i=i+1
        else:
            i=i+1
    return len(nlis)