def insere(lista_numero,n):
    '''funcao que recebe uma lista de numeros inteiros ordenados em ordem crescente e retorna uma lista inserindo o inteiro n de forma que continue ordenada em ordem crescente
    list -> list'''
    nova_lista=list.append(lista_numero,n)
    nova_lista_2=list.sort(nova_lista)
    return nova_lista_2