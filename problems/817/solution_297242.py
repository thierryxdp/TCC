def maiores(numeros, n):
    '''funcao que, dada uma lista de numeros inteiros e um numero n de entrada, retorna
    uma nova lista que contem apenas os numeros maiores que n, os quais estarao ordenados
    de maneira crescente;
    list(int),int->list(int)'''
    lista=numeros+[n]
    list.sort(lista)
    indice_n=list.index(lista,n)
    return lista[indice_n+1:]

def acima_da_media(notas):
    '''funcao que, dada uma lista de notas, retorna uma nova lista ordenada de forma
    crescente apenas com as notas que estiverem acima da media;
    list(int)->list(int)'''
    media=sum(notas)/len(notas)
    list.sort(notas)
    if media in notas:
        list.remove(notas,media)
        return maiores(notas,media)
    else:
        return maiores(notas,media)