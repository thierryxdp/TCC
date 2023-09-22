def filtra_pares(n1,n2,n3,n4):
    list1=(n1,n2,n3,n4)
    
    par=list(lambda(x%2==0, list1))
    return list1