def maiores(lista_de_numeros,n):
    """Função que dada uma lista de entrada retorna uma outra lista que contém os números
    maiores do que a entrada n"""
    """lista_de_numeros e n(um número qualquer"""
    """list,int->list"""
    lista_de_numeros.append(n)
    lista_de_numeros.sort()
    return lista_de_numeros[lista_de_numeros.index(n)+1:]