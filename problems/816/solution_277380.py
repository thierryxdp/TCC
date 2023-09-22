def maiores(lista_numero,n):
    """ retorna uma nova lista com os números maiores que n presentes na lista_numero; list,int -> list """
    list.append(lista_numero,n);
    list.sort(lista_numero);
    if (list.count(lista_numero,n)==1):
        return lista_numero[list.index(lista_numero,n)+1:];
    else:
        if(list.count(lista_numero,n)>=2):
            return lista_numero[list.index(lista_numero,n)+list.count(lista_numero,n):];