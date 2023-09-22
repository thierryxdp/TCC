def encontra_impares( tupla ):
    return [ n for n in tupla if n % 2 != 0 ]

tpl = (1, 2, 3,5,5,9,7,32,1,6)
lst = encontra_impares( tpl )

print(tpl)
print(lst)