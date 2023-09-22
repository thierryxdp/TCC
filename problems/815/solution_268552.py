def insere(lista_numero,n):
    """
    Função que recebe uma lista de números ordenada de forma crescente, 
   	adiciona um número 'n' de forma que a lista continue ordenada
    e retorna a lista
    
    list, int ---> list
    """
    lista_numero.append(n).sort()
    return lista_numero