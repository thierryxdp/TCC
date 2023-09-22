def greatlist(lista,n):
""" A função retornar uma lista modificada com elementos maiores que n;
    list, int -> list """
    list.sort(lista)
    lista1= [i for i in lista if i>n]
    return lista1