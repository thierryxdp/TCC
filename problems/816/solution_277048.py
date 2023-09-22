def maiores(lista,n):
    '''função que recebe uma lista formada por números inteiros(lista)
       e um número(n), tendo como retorno uma nova lista formada por
       todos os números pertecentes a lista inicial que forem numericamente
       maiores que 'n'
       [list, int-->list]'''
    
    if n not in lista:
        lista = lista + [n]
        list.sort(lista)
        M = list.index(lista,n)
        return lista[M+1:]
    
    if n in lista:
        list.sort(lista)
        
        if list.count(lista, n) == 1:
            M = list.index(lista,n)
            return lista[M+1:]
        
        if list.count(lista,n) > 1:
            P = list.count(lista,n)
            M = list.index(lista,n)
            return lista[M+P:]