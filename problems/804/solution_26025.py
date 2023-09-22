#Start your python function here
def filtra_pares(t):
    lista = []
    if type(t) == tuple and len(t) == 4:
        for i in t:
            if type(i) != int:
                lista = []
                return ("Todos os valores são inteiros")
                else:
                    if i%2 == 0:
                    lista.append(i)
                    return (tuple(lista))
                    else:
                        return lista