def filtra_pares(a,b,c,d):
    "Retorne"
    if a%2!=1 and b%2!=1 and c%2!=1 and d%2!=1:
     return a,b,c,d
    elif a%2!=1 and b%2!=1 and c%2!=1 and d%2==1:
     return a,b,c
    elif a%2!=1 and b%2!=1 and c%2==1 and d%2==1:
     return a,b
    elif a%2!=1 and b%2==1 and c%2==1 and d%2==1:
     return a
    else:
     return ()