#a função insere um numero n na posiçao correta.
#list->list
def insere(lista_numero,n):
    lista_numero.append(n)
    lista_numero.sort()
    return(lista_numero)