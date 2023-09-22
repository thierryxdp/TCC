def insere(lista,n):
    '''Função que dada uma lista de números em ordem crescente, inclua um número 'n' na posição correta; list,int->list'''
    i = 0
    while i < len(lista):
        if lista[i] > n:
            list.insert(lista, i, n)
            return lista
        
        if n > lista[-1]:
            lista.append(n)
            return lista
        i = i + 1