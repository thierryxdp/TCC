def maiores(lista,n):
    '''Função que, dados uma lista de números inteiros e um número inteiro n, retorna uma lista com todos os elementos da primeira lista maiores que n;list,int -> list'''
    list.sort(lista)
    posicaon= list.index(lista,n)
    if n in lista:
        return lista[posicaon+1:]
    else: 
        return