def maiores(lista, n):
    numero=n
    for x in lista:
        listanova = [x for x in lista if x>numero]
 
        return listanova.sort()