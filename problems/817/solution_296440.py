def maiores(lista,n):
    '''funcao que recebe uma lista de numeros inteiros e um inteiro n e retorna outra lista contendo os numeros da lista original que sao maiores do que n ordenados dem ordem crescente 
list, int -> list'''
    list.append(lista,n)
    list.sort(lista)
    i=list.index(lista,n)
    return lista[i+1:]
def acima_da_media(lista_notas):
    '''funcao que recebe uma lista com a nota dos alunos e retorna uma nova lista ordenada com as notas dos alunos que ficaram acima da media
list -> list'''
    media=sum(lista_notas)/len(lista_notas)
    notas_acima_da_media=maiores(lista_notas,media)
    notas_acima_da_media=notas_acima_da_media-[media]
    return notas_acima_da_media