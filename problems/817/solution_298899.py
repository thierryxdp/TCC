def maiores(lista_numeros, n):
    '''Função que, dada uma lista de números inteiros e um número (n)
    como entrada, retorna outra lista contendo todos os números da
    lista original maiores que n ordenados em ordem crescente;
    lista,int->lista'''
    list.append(lista_numeros,n)
    list.sort(lista_numeros)
    indice_n=list.index(lista_numeros,n)
    if list.count(lista_numeros,n)> 1:
        return lista_numeros[indice_n+list.count(lista_numeros,n):]
    else:
        return lista_numeros[indice_n+1:]

def acima_da_media(notas):
    '''Função que, dada uma lista contendo as notas dos aluno de uma turma
    como entrada, retorna uma lista ordenada com as notas que ficaram acima
    da média; lista->lista'''
    media= sum(notas)/len(notas)
    return maiores(notas,media)