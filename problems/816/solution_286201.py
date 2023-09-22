def insere(lista_numero,n):
    '''Função que dada uma lsta crescente de números inteiros e um número inteiro n, inclui n na posição correta;
       list->list'''
    list.append(lista_numero,n)
    list.sort(lista_numero)
    return lista_numero

def maiores(lista_numero,n):
    '''Função que dada uma lista de números inteiros e um número inteiro(n), retorna outra loista, que contenha todos os números da lista original maiores que n
       list,int->list'''
    lista = insere(lista_numero,n)
    x = (list.index(lista,n))+1
    return lista[x::]