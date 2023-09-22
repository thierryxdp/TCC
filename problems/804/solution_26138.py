def filtra_pares(tupla):
    nova_tupla = []
    if type(tupla) == tuple and len(tupla) == 4:
        for i in tupla:
            if type(i) != int:
                nova_tupla = []                
                break
            elif i%2 == 0:
                nova_tupla.append(i)
                return (tuple(nova_tupla))