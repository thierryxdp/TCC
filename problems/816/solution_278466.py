def maiores(lista_inteiros,n):

    lista_nova = list.copy(lista_inteiros)

    list.sort(lista_nova)

    return lista_nova[(list.index(lista_nova,n)+1):] #encontra qual é a posição de n na lista e soma-se 1 para ler valores acima de n até o final da lista