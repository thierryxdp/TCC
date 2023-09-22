def filtra_pares(tupla):
    e1,e2,e3,e4=tupla[0],tupla[1],tupla[2],tupla[3]
    tupla=()
    if e1%2==0:
        tupla+=(e1,)
    if e2%2==0:
        tupla+=(e2,)
    if e3%2==0:
        tupla+=(e3,)
    if e4%2==0:
        tupla+=(e4,)
    return tupla