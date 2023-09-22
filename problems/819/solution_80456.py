def filtraMultiplos (lista,n):
    lista=()
    prox= 0
    while prox <len(n):
        if t[prox]%n==0:
            lista=lista + (n[prox],)
            prox = prox +1
            return lista