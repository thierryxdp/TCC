def insere(lista_numero,n):
    list.append(lista_numero,n)
    list.sort(lista_numero)
    return lista_numero
def maiores(lista_numero,n):
    ordem= insere(lista_numero,n)
    return ordem[list.index(ordem,n)+1:]