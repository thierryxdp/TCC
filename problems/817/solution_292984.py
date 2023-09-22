def maiores(lista, n):
    ''' funcao que dado os elementos de uma lista de numeros inteiros,
    retona outra lista com numeros da lista maiores que n 
    list, int ->list '''
    numeros = lista[:]
    if (n not in numeros):
        numeros.append(n)
        numeros.sort(reverse=True)
    l = numeros.index(n)
    return numeros[:l:]

def acima_da_media(notas):
    ''' funcao que calcula a media de uma turma e retorna a media e aprovados
list-> float,list'''
    media = sum(notas)/len(notas)
    aprovados = maiores(notas, media)
    return aprovados