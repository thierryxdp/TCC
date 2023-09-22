def filtra_pares(tupla):
    """retorna os elementos pares. int -> int"""
 	
    lista = []

    for n in tupla:
        if n % 2 != 0:
            lista.append(n)

    return lista


tpl = ''
lst = filtra_pares(tpl)

print(tpl)
print(lst)