def maiores(lista,n):
    '''Função que, dada uma lista de números inteiros e um número inteiro n, retorna outra lista contendo
    os números originais que sejam maiores que n e ordenados de maneira crescente;
    list,int->list'''
    
    list.append(lista,n)
    list.sort(lista)
    x=(list.index(lista,n))+1 
    return lista[x::]

def acima_da_media(lista_notas):
    '''Funcao que, dada uma lista com todas as notas dos alunos, retorna uma
    lista com todas as notas acima da média de forma ordenada;
    list->list'''
    
    lista_notas=lista
    n=(sum(lista))/2
    lista_ordenada=maiores(lista,n)
    return lista_ordenada