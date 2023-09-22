from math import * 
def maiores(lista,numero):
	"""dada uma lista de números inteiros e um numero inteiro n
    retorna outra lista que contenha todos os números da lista original
    maiores que n em ordem crescente
    list,int->list"""
    list.append(lista,numero)
    list.sort(lista)
    x=list.index(lista,numero)
    return lista[x:]

def acima_da_media(lista):
    """função que recebe uma lista com as notas de alunos de uma turma
    retorna uma lista ordenada com as notasque ficaram acima da média
    list -> list"""
    s = sum(lista)
    d = len(lista)
    numero=s/d
    copia=list.copy(lista)
    a=maiores(copia,numero)
    list.pop(a,0)
    if numero in a:
        b=list.index(a,numero)
        list.pop(a,b)
    return a