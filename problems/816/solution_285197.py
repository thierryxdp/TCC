def maiores(lista,n):
    '''funcao que recebe uma lista com numeros e um numero 
       inteiro 'n' e retorna uma lista em ordem crescemte, 
       na qual os numeros menores que 'n' nao estao nessa 
       lista, utilizando as funcoes 'append', 'sort' e 'index'
       list, int -> list'''
    lista.append(n)
    lista.sort()
    final= lista.index(n)
    return lista[final+1:]