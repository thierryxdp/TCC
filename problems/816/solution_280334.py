def maiores(lista,n):
    '''Funcao que calcula e retorna uma lista de numeros inteiros maiores que n.
    int->int'''
    return [i for i in lista if i > n]
lista_retorno = maiores(lista_numeros,n)
print(lista_retorno)