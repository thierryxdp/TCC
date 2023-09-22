def maiores(ls, n):
    lista = []
    for e in ls:
        if e > n:
            lista.append (e)
    list.sort (lista)
    return lista

def acima_da_media (notas):
    elem = list.count (notas)
    soma = sum (notas)
    media = soma / elem
    return maiores (notas, media)