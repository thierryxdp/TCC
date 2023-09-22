"função que ordena lista de números em ordem crescente;list,int->list"
def insere(lista_numero,n):
    lista1=lista_numero+[n]
    lista2=sorted(lista1)
    return lista2