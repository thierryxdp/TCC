def maiores(lista,n):
    """funcao que dada uma lista de numeros inteiros e um numero inteiro n, retorna
    outra lista, que contem todos os numeros da lista original maiores que n, 
    em ordem crescente
    list,int->list"""
    lista2 = []
    i = 0
    while i<len(lista):
        if lista[i] > n:
            lista2 = lista2 + [lista[i],]
            list.sort(lista2)
        i=i+1
    return lista2

def acima_da_media(lista):
    """funcao que dada uma lista com as notas dos alunos de uma turma, retorna uma lista 
    ordenada com as notas que ficaram acima da media
    list->list"""
    k = sum(lista)/len(lista)
    lista2 = maiores(lista,k)
    return lista2