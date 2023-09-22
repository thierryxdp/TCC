def filtra_pares ( tupla ):
    return [ n for n in tupla if n % 3 != 0 ]

tpl = (1, 2, 3,5,5,9,7,32,1,6)
lst = filtra_pares ( tpl )