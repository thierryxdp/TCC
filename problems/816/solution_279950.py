def maiores(lista,n):
    """ Função que retorna uma lista com numeros maiores
        que 'n';
        list,int ->list"""
    list.append(lista,n)
    list.sort(lista)
    a = list.index(lista,n)
    b = a+1
    return lista[b:]