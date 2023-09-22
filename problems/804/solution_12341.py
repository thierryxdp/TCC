def filtra_pares(tupla):
    lista = ()
    for n in tupla:
        if n % 2 == 0:
            lista.append(n)
    return lista
tpl = (1,9,22,46)