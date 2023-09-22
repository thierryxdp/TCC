def maiores(lista, n):

    ''' lista int > int
    Dada uma lista, retorna outra lista, ordenada de forma crescente, apenas com os números maiores que n'''

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

    ''' lista > lista
    Dada uma lista com as notas dos alunos de uma turma, retorna aquelas que ficaram acima da média'''

    notatotal = sum(notas)
    alunos = len(notas)
    media = notatotal/alunos

    return maiores(notas, media)