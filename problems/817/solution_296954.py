def maiores(lista,n):
    '''funcao que dada uma lista de numeros inteiros e um numero 
    inteiro, retorna outra lista que contem todos os numeros da lista 
    original maiores que n, ordenados em ordem crescente.
    list,int->list'''
    a=([i for i in lista if i > n])
    list.sort(a)
    return a
def acima_da_media(lista):
    '''recebe uma lista com as notas dos alunos e retorna quais das notas estao acima da media
    list->list'''
    x= sum(lista)/len(lista)
    return maiores(lista,x)