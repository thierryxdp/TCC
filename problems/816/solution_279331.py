def maiores(lista,n):
    """Função que retorna uma lista com todos os elementos de uma lista
dada que forem maiores no que o inteiro n"""
    list.sort(lista)
    x = list.count(lista,n)
    if x > 0:
       z = list.index(lista,n)
       if z == 0:
           return lista[1:]
       elif z == len(lista):
            return []
       else:
           return lista[n:]
    if x == 0:
        list.append(lista,n)
        list.sort(lista)
        z = list.index(lista,n)
        if z == 0:
           return lista[1:]
       elif z == len(lista):
            return []
       else:
           return lista[n+1:]