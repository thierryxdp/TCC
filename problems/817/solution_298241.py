def maiores(lista,n):
    '''funcao que dada uma lista de numeros inteiros e um numero 
    inteiro, retorna outra lista que contem todos os numeros da lista 
    original maiores que n, ordenados em ordem crescente.
    list,int->list'''
    a=([i for i in lista if i > n])
    return sorted(a)
def acima_da_media(lista):
    '''Recebe uma lista de notas de alunos e retorna uma lista ordenada das que ficaram acima da média'''
    soma=sum(lista)
    total=len(lista)
    media=soma/total
    return maiores(lista,media)