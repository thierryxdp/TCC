lista = []
def filtraMultiplos(L,n):
    for i in L:
        if i%n==0:
        	lista.append(i)
            return lista
        else: