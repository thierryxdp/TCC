def insere(lista_numero,n):
    '''Função que, dada uma lista ordenada (crescente) como entrada e um número inteiro chamado n,
    retorna uma nova lista onde n esteja na posição correta e a lista continue ordenada;
    list,int->list'''
    list.append(lista_numero, n)
    list.sort(lista_numero)
    return lista_numero

def maiores(lista_numero,n):
    '''Função que, dada uma lista de números inteiros e um número inteiro n, retorna outra lista contendo
    os números originais que sejam maiores que n e ordenados de maneira crescente;
    list,int->list'''
    
    lista=insere(lista_numero,n)
    x=(list.index(lista,n))+1 
    return lista[x::]