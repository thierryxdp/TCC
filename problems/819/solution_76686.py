lista = []
def filtraMultiplos(L,n):
    for i in L:
        if n%i==0:
        	lista.append(i)
            return lista