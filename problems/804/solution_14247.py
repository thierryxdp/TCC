def filtra_pares (a):
    ''' entradas: a (tupla)
    a função retorna uma nova Tupla com apenas os elementos pares da
    Tupla original, na mesma ordem inicial'''
    
    tupla = ()
    if a[0]%2 == 0:
        tupla = tupla + (a[0],)
        if a[1]%2 == 0:
            tupa = tupla + (a[1],)
            if a[2]%2 == 0:
                tupla = tupla + (a[2],)
                if a[3]%2 == 0:
                    tupla = tupla + (a[3],)
                    return tupla