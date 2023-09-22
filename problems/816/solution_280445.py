def maiores(lista,n):
    '''Funcao que calcula e retorna uma nova lista apartir do numero inteiro n
    list,int-> list,int'''
    return [i for i in lista if i > n]
lista_retorno = maiores(lista_numeros,n)
print(lista_retorno)