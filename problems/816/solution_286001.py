def maiores(lista,n):
    '''Função que pega a lista de entrada verifica se os elementos da lista são maiores que o valor de entrada
    n, se forem eles serão encaixados na lista de retorno em ordem crescente
    list,list→list'''
    lista_ordenada=[]
    for i in lista:
        if i > n:
            lista_ordenada.append(i)
            lista_ordenada.sort()
    return lista_ordenada