def filtra_pares(tpl)
    return [n for n in tpl if n%2 != 0]
tpl=(1,2,3,4)
lst= filtra_pares(tpl)
print (tpl)
print (lst)