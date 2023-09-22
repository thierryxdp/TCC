def maiores(listaint, n):
    '''Função que ordena os números de uma lista, maiores do que n, em ordem crescente
    lista, int -> lista'''
    list(listaint)
    listaint.append(n)
    listaordenada = sorted(listaint)
    entrada = listaordenada.index(n)
    
    if n not in listaordenada:
        listaint.append(n)
    return listaordenada[entrada + 1:]