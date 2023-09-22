def filtraMultiplos(lista,num):
    div = ()
    prox = 0
    if (lista[prox]%num)==0:
        div+=(lista[prox])
    prox+=1
    if (lista[prox]%num)==0:
        div+=(lista[prox])
    prox+=(lista[prox])