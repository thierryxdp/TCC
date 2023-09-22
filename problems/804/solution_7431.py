def filtra_pares( tupla ):
    '''retorna apenas os pares da tupla
    tuple -> tuple'''
    a,b,c,d = tuplade4elementosinteiros
   return [ n for n in tupla if n % 2 != 0 ]

tpl = (1, 2, 3,5,5,9,7,32,1,6)
lst = encontra_impares( tpl )