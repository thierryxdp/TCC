def maiores(lista, n):
    '''Calcular uma funcao que dada uma lista de numeros inteiros adicione um numero e outra lista com numeros maiores que o adicionado;
    list, int -> list'''
    
    list.append(lista, n)
    list.sort(lista)
    
    posicao = list.index(lista, n)
    
    return lista[posicao+1:]