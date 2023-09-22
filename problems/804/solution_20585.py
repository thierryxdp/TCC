def filtra_pares(n1,n2,n3,n4):
    p1 = n1%2==0
    p2 = n2%2==0
    p3 = n3%2==0
    p4 = n4%2==0
    if p1 and p2 and p3 and p4:
    	return (n1,n2,n3,n4)