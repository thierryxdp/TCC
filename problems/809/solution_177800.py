def intercala(lista1, lista2):
    '''Função que intercala duas listas em uma única.
    int,int ->int'''
    lista=lista1+lista2
    return lista.sort(((lista1[0]+lista2[0])+lista1[1]+lista2[1])+lista1[2]+lista2[2])