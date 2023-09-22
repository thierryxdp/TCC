def maiores(lista_numeros,n):
    '''Funcao que recebe de entrada uma lista de numeros inteiros e um numero
    inteiro n e retorna uma outra lista com todos os numeros da lista original
    maiores do que n em ordem crescente.
    list, int -> list'''
    lista_maiores = lista_numeros + [n]
    if n in lista_numeros:
        lista_maiores = lista_numeros
    list.sort(lista_maiores)
    return lista_maiores[list.index(lista_maiores,n)+1:]

def acima_da_media(notas):
    '''Funcao que recebe de entrada as notas, que variam de 0.0 a 10.0, dos
    alunos de uma turma, e retorna apenas as maiores notas que a média das notas dos
    alunos.
    list -> list'''
    media = round(sum(notas)/len(notas),1)
    return maiores(notas,media)

#casos de teste
#acima_da_media([1,5,6,9,10]) == [9, 10]
#acima_da_media([5,10,6.5,3.5,5,6]) == [6.5,10]
#acima_da_media([2.5,4.6,8,6.8,7,9.5]) == [6.8,7,8,9.5]