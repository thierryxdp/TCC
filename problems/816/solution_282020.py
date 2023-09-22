def maiores(lista,n):
    """ Recebe uma lista e um numero, e retorna essa lista sem
    os maiores numeros do que n em ordem
    list,int -> list """
    list.append(lista,n) # insere o elemento na lista
    list.sort(lista) # ordena a lista
    i = list.index(lista,n) # acha o indice do elemento
    qtd = list.count(lista,n)  # conta qtd de n na lista
    i2 = qtd + i + 1 # posição n, excluindo o próprio
    final = lista[i2:] # nova lista, sem o n
    return final # retorna a lista final