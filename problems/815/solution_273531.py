def insere(lista_numero,n):
    n=[n,]
    list= [[lista_numero]+ [n]]
    return sorted(lista_numero+ n,reverse=False)