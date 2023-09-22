def maiores(lista, n):
    '''dada uma lista(lista) composta por numeros inteiros e um numero inteiro(n), retorna a lista de numeros maiores que (n) contidos na lista original(lista); list,int -> list'''
    if n in lista:
        list.sort(lista)
        N = (list.index(lista,n))
        A = lista[(N+1):]
    elif n not in lista:
        lista = lista + [n]
        list.sort(lista)
        N = (list.index(lista,n))
        A = lista[(N+1):]
    return A 

def acima_da_media(lista):
    '''dada uma lista com as notas dos alunos de uma turma, retorna as notas que estao acima da media; list-> list'''
    Q = len(lista)
    S = sum(lista)
    media = S/Q
    acima = maiores(lista,media)
    return acima