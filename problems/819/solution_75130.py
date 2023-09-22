def filtraMultiplos(lista,num):
    div = ()
    prox = 0
    while prox <len(div):
        if (lista[prox]%num)==0:
            div = div+(lista[prox],)
        prox = prox+1
    return div