def insere(lista_numero, n):
    '''Funcao que, dada uma lista ordenada (crescente) como entrada e um numero inteiro chamado n, retorna uma nova lista onde n esteja na posicao correta e a lista continue ordenada;
    list,int->list'''
    
    list.append(lista_numero,n)
    list.sort(lista_numero)
    
    return lista_numero

def maiores(lista_numeros,n):
    '''Funcao que, dada uma lista ordenada (crescente) como entrada e um número inteiro chamado n, retorna uma nova lista onde n esteja na posicao correta e a lista continue ordenada;
list,int->list'''
    
    lista=insere(lista_numeros,n)
    x=(list.index(lista,n))+1
    
    return lista[x:]