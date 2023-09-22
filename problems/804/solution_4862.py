def filtra_pares ( tupla4elementos):
    e1 = (int(tupla4elementos[0]),)
    e2 = (int(tupla4elementos[1]),)
    e3 = (int(tupla4elementos[2]),)
    e4 = (int(tupla4elementos[3]),)
    tupla_pares = ()
    if e1[0]%2==0:
        tupla_pares = tupla_Pares + e1
    if e1[1]%2==0:
        tupla_pares = tupla_Pares + e2
    if e1[2]%2==0:
        tupla_pares = tupla_Pares + e3
    if e1[3]%2==0:
        tupla_pares = tupla_Pares + e4
    return tupla_pares