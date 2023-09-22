def filtraMultiplos(l,n):
	proximo = 0
    nl= []
    teste = l[proximo]%2
    teste2 = 0
    while proximo < len(l):
    	if l[proximo]%2 == 0:
       		nl = nl + [l[proximo],]
     	proximo = proximo + 1
    return teste2