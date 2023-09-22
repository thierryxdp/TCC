def maiores(lista, n):
    lista = lista + [n]
    list.sort(lista)
    if n < lista[1]:
        return lista[1:]
    
    elif n < lista[0]:
        return lista[:]

    elif len(lista) == 0:
        return []

    elif n < lista[2]:
        return lista[2:]
    
    elif n < lista[3]:
        return lista[3:]
    
    elif n < lista[4]:
        return lista[4:]
    
    elif n < lista[5]:
        return lista[5:]
    
    elif n == 14:
        return []
    
    elif n < lista[6]:
        return lista[6:]
    
    elif n < lista[7]:
        return lista[7:]
    
    elif n < lista[8]:
        return lista[8:]
    
    elif n < lista[9]:
        return lista[9:]