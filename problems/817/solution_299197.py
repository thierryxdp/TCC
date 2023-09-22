def acima_da_media(notas):
    n = sum(notas)/len(notas)
    list.insert(notas, 0, n)
    list.sort(notas)
    if list.count(notas, n)==1:
        return notas[list.index(notas, n)+1:]
    elif list.count(notas, n)>1:
        return notas[-1:list.index(notas, n):-1]