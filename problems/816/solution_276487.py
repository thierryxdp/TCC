def maiores(lista,n):
    '''Função que, dados uma lista de números inteiros e um número inteiro n, retorna uma lista com todos os elementos da primeira lista maiores que n;list,int -> list'''
    list.sort(lista)
    if n in lista:
        posicaon= list.index(lista,n)
        return lista[posicaon+1:]
    else: 
        return True