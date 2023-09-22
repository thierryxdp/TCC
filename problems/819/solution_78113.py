def filtraMultiplos(listai,n):
    """função recebe uma lista e um número e retorna uma outra lista com todos o elementos múltiplos do número dado. LIST(INT),INT->LIST(INT)"""
    listaf = ()
    i = 0
    while i<len(listai):
        if listai[i]%n == 0:
            listaf= listaf + (listai[i],)
        i = i+1
    return list(listaf)