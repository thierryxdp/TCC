def maiores(lista,n):
    '''Função que recebe como entrada uma lista de números inteiros e um número
    inteiro e retorna outra lista contendo todos os
    números da lista anterior maiores que o numero "n", em ordem
    crescente. Entrada - >list, int; Saída -> list'''
    list.append(lista,n)
    list.sort(lista)
    a = list.index(lista,n)
    return lista[a+1:]

def acima_media(lista):
    '''Função que recebe uma lista com as notas e retorna uma outra lista
    com as notas acima da média. Média == 7. Entrada -> list; Saida ->list'''
    media = int(sum(lista)/len(lista))
    resultado = maiores(lista,media)
    if (media in lista) and (media == resultado[0]):
        return resultado[1:]
    else:
        return resultado