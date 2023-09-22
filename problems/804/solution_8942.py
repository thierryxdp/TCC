def filtra_pares(a,b,c,d):
    list.remove((a,b,c,d), a%2 !=0 and b%2 !=0 and c!=0 and d!=0)
    return a,b,c,d