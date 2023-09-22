def filtra_pares(tupla):
    if tupla[0]%2==0:
        tupla+=(tupla[0],)
    if tupla[1]%2==0:
        tupla+=(tupla[1],)
    if tupla[2]%2==0:
        tupla+=(tupla[2],)
    if tupla[3]%2==0:
        tupla+=(tupla[3],)
        
    return tupla