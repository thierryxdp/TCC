def maiores(lista_inteiros,n):
    '''Função que dada uma lista de números inteiros e um inteiro n, retorna uma lista dos números da lista original maiores que n
    list[int,...],int -> list[int,...]'''
    list.append(lista_inteiros,n)
    list.sort(lista_inteiros)
    return lista_inteiros[list.index(lista_inteiros,n)+1:]

def acima_da_media(notas):
    '''Função que dada uma lista de notas, retorna uma lista ordenada com as notas acima da média
    list[int,...] -> list[int,...]'''
    media=sum(notas)/len(notas)
    if media in notas:
        list.remove(notas,media)
        return maiores(notas,media)
    else:
        return maiores(notas,media)