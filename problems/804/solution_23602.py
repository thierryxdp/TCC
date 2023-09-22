def filtra_pares (tupla):
    ''' função que retorna uma nova tupla contendo apenas elementos pares
    da tupla original'''
    if tupla[0]%2==0:
        return tupla [0]
    if tupla[1]%2==0:
        return tupla [0]+tupla [1]
    if tupla[2]%2==0:
        return tupla [0]+tupla [1]+tupla [2]
    if tupla[3]%2==0:
        return tupla [0]+tupla [1]+tupla [2]++tupla [3]