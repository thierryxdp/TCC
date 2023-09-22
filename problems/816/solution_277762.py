def maiores(lista_de_numeros, n):
    '''Função que calcula o maior de uma lista de número inteiro e um numero inteiro n e retorna uma outra lista.
       list, int ---> list'''
    nova_lista = lista_de_numeros[-1:]
    list.append(nova_lista,n)
    list.sort(nova_lista)
    return nova_lista