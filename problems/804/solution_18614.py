def filtra_pares(elem):
    lit=()
    if elem[0] &2 ==0:
        lit = lit +(elem[0],)
    if elem[1] %2==0:
        lit = lit+(elem[1],)
    if elem[2]%2==0:
        lit= lit +(elem[2],)
    if elem[3]%2==0:
        lit= lit + (elem[3],)
    return lit