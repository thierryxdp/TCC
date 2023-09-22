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

def acima_da_media(notas):
    '''função que retorna uma lista com as notas dos alunos que ficaram
    acima da média
    assinatura: list.int > list.int
    casos de teste: acima_da_media([8,3,4,5,6,0,1,2,9]) ==[5, 6, 8, 9]
    acima_da_media([8,3,4,5,6,0,1,2,9,9]) ==[5, 6, 8, 9, 9]'''
    notatotal = sum(notas)
    alunos = len(notas)
    media = notatotal/alunos
    return maiores(notas, media)