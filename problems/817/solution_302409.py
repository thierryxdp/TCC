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

def acima_da_media(lista_notas):
    '''Funcao que dada uma lista, retorna uma lista ordenada contendo somente as notas que ficaram acima da media;
    list->list'''
    
    media=(sum(lista_notas)//len(lista_notas))+1
    lista=maiores(lista_notas,media)
    
    return lista