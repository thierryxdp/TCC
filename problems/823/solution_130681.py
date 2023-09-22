def faltante(L):
    N=len(L)+1
    todos= range(1,N+1)
    i=0
    while i<N:
        if todos[i] not in L:
            return todos[i]
        i+=1