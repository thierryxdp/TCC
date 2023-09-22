def maiores(lista,n):
    '''função que recebe uma lista e um numero inteiro(n), e retorna
    uma outra lista contendo os numeros maiores que n. list, inte -> list)'''
    lista.append(n)
        lista.sort()
        l = lista.index(n)
        lista2 = lista[l+1:]
        rep = lista2.count(n)
        return lista2[rep:]
    
def acima_da_media(notas):
    ''' função que, dada uma lista com as notas dos alunos, retorna uma lista com as notas
    que ficaram acima da media em ordem crescente. list -> list'''
    media = sum(notas)/len(notas)
    return maiores(notas,media)