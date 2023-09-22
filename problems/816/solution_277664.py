def maiores (nuns, n):
    'dada uma lista de números e o inteiro n, retorna uma nova lista, contendo apenas os numeros da lista inserida que são maiores que n. str, int -. str'
    if n in nuns:
        list.sort(nuns)
        a = list.index(nuns, n)
        return nuns[a+1:]
    elif n not in nuns:
        list.append(nuns, n)
        list.sort(nuns)
        a1 = list.index(nuns, n)
        return nuns[a1+1:]