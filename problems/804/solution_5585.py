def filtra_pares(t1,t2,t3,t4):
    tuplas=t1,t2,t3,t4
    filter(lambda x: x%2==0,tuplas)
    return tuplas