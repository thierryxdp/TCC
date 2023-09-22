def maiores(lista,n):
    """
    Função que recebe uma lista de números, um número inteiro 'n'
    e retorna uma lista contendo todos os inteiros maiores que
    n presentes na lista recebida
    
    list, int ---> list
    """
    lista.append(n+1)
    lista.sort()
    i = lista.index(n+1)
    return lista[i+1:]