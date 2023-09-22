from math import * 
def maiores(lista,numero):
    """Função que, dada uma lista e um número, retorna outra 
    lista, porém, escolhendo somente os números da lista 
    original maiores que n 
    list,int -> list"""
    list.append(lista,numero)
    list.sort(lista)
    x=list.index(lista,numero)
    return lista[x:]

def acima_da_media(lista):
    '''funçao que, fornecida uma lista com as notas dos alunos 
    de uma turma, retorna uma lista ordenada com as notas que
    estao acima da media 
    list -> list'''
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