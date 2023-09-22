def filtra_pares(tupla):
    tupla2=tuple()
    if tupla[0]%2==0:
        tupla2+=(tupla[0],)
    if tupla[1]%2==0:
        tupla2+=(tupla[1],)
    if tupla[2]%2==0:
        tupla2+=(tupla[2],)
    if tupla[3]%2==0:
        tupla2+=(tupla[3],)
        
    return tupla2