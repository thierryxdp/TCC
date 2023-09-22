def filtra_pares(tupla):
    nova_tupla = []
    if type(tupla) == tuple and len(tupla) == 4:
        for item in tupla:
            if i%2 == 0:
                nova_tupla.append(item)
                return (tuple(nova_tupla))