def insere(lista,n):
    """
    Função que recebe uma lista de números ordenada de forma crescente, 
   	adiciona um número 'n' de forma que a lista continue ordenada
    e retorna a lista
    
    list, int ---> list
    """
    lista.append(n)
    lista.sort()
    return lista