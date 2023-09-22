def maiores(l,n):
    '''
    Recebe uma lista l e um número n. Adiciona n nessa lista, depois
    ordena a lista de forma crescente. Pega a posição inicial de n 
    e quantas vezes ele apareceu. Depois deleta todos os números até
    n, ou seja, menores ou iguais a n.
    list, int -> list
    '''
    l.append(n); l.sort()
    k = l.index(n); c = l.count(n)
    del l[0:k+c]	
    return l