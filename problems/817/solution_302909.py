def acima_da_media(notas):

    notatotal = sum(notas)
    alunos = len(notas)
    media = notatotal/alunos

    return maiores(notas, media)

def maiores(lista, n):
    
    if n in lista:

        lista.sort()
        t = lista.index(n)
        listafinal = lista[t+1:]

        return listafinal

    if n not in lista:
    
        lista.append(n)
        lista.sort()
        t = lista.index(n)
        listafinal = lista[t+1:]

        return listafinal