def maiores(lista,n):
    '''funcao que dada uma lista de numeros inteiros e um numero 
    inteiro, retorna outra lista que contem todos os numeros da lista 
    original maiores que n, ordenados em ordem crescente.
    list,int->list'''
    a=([i for i in lista if i >= n])
    return sorted(a)

def acima_da_media(listanotas,media):
    '''funcao que dada uma lista com notas dos alunos de uma uma turma,
    retorna uma lista com as notas que ficaram acima da média
    list,int->list'''
    return maiores(listanotas,media)