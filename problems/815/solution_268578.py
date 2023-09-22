def insere(lista_numero,n):
    """calculo e retorno que inclua n na posiçao correta para que a lista continue ordenada."""
    a=lista_numero.append(n)
    b=list.sort(lista_numero)
    return lista_numero