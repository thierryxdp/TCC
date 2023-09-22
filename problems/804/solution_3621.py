def filtra_pares( tupla ):

    lista = []

    for valor in tupla:
    	if valor % 2 == 0:
        	lista.append(valor)

	return (lista) 

tpl = (lista)
lst = filtra_pares ( tpl )

print(lst)