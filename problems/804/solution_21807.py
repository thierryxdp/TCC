def filtra_pares (x,y,z,w):
    '''retorna um tupla contendo apenas os elementos pares da tupla original, na mesma oradem que se encontravam
    int,int,int,int->tuple'''
    tupla=()
    if x%2==0:
        return tupla+=(x,)
    if y%2==0:
        return tupla+=(y,)
    if z%2==0:
        return tupla+=(z,)
    if w%2==0:
        tupla+=(w,)