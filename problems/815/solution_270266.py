def insere(lista_numero:list,n:int)->list:
    """A funcao recebe como entrada uma lista de numeros inteiros,e um numero inteiro .E ela retorna esse numero inteiro na posicao da lista, de modo que ela continue ordenada """
    list.append(lista_numero,n)
    list.sort(lista_numero)
    return lista_numero