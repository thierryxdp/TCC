def maiores(lista,n):
    #Dada uma lista de números inteiros e um número inteiro, retorna nova lista com números maiores que o fornecido. list, int -> list
    list.extend(lista,[n])
    list.sort(lista)
    nova_lista = list()
    for i in lista:
        if i > n:
            list.extend(nova_lista,[i])
    return(nova_lista)