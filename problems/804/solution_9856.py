def filtra_pares(x):
    n1,n2,n3,n4 = x
    a = 0
    b = 0
    c = 0
    d = 0
    if n1 % 2 == 0:
        n1 = a
    else:
        a = None
    if n2 % 2 == 0:
    	n2 = b
    else:
        b = None
  	if n3 % 2 == 0:
        n3 = c
   	else:
        c = None
    if n4 % 2 == 0:
        n4 = d
    else: 
        n4 = None
   	return a,b,c,d