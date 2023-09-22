def faltante(lista):
    tamLista = len(lista) + 1
    n = 1
    pecas = [n]
    total_observado = sum(lista)
    while n < tamLista:
        pecas += [(n+1),]
        n = n+1
    total_esp = sum(pecas)
    total_obs = sum(lista)
    return total_esp - total_obs