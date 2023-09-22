def maiores(lista_numeros,n):
    """Está função retorna uma nova lista com os números maiores que 'n'
    na lista 'lista_numeros'"""
    list.sort(lista_numeros);
    nu=list.index(lista_numeros,n);
    new_list=[lista_numeros[0:-1]];
    
    return new_list