def maiores (numeros,n):
    '''dada uma lista de números inteiros  e um número inteiro (n) retorna outra lista, que contenha todos os números da lista original maiores que n ordenados em ordem crescente;
    list, int -> list'''
    if n in numeros: 
        list.sort(numeros)
        l1=list.index(numeros,n)
        return numeros[l1+1:]
    else:
        list.append(numeros,n)
        list.sort(numeros)
        l1=list.index(numeros,n)
        return numeros[l1+1:]
    
def acima_da_media (lista):
    '''dada uma lista com as notas dos alunos de uma turma, retorna uma lista ordenada com as notas que ficaram acimada média;
    list -> list'''
    media=(sum(lista))/(len(lista))
    return maiores(lista,media)