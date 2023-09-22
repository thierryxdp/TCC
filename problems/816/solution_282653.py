def insere(lista_numero,n):
    nova_lista_numero=lista_numero+[n]
    list.sort(nova_lista_numero)
    return nova_lista_numero

def maiores(lista_numero,n):
    return insere(lista_numero,n)[list.index(insere(lista_numero,n)+1,]