def maiores_que(lista,n):
    '''dada uma lista e um inteiro n, retorna uma nova lista ordenada com apenas os numeros da lista original que sao maiores que n; list,int -> list'''
    i = 0
    novalista = []
    while i < len(lista):
        if lista[i] > n:
            novalista = novalista + [lista[i],]
        else:
            novalista = novalista
        i = i + 1
    list.sort(novalista)
    return novalista



def acima_da_media(lista_notas):
    '''dada a lista com as notas dos alunos, retorna outra lista com as notas acima da media; list -> list'''
    return maiores_que(lista_notas,(sum(lista_notas))/(len(lista_notas)))