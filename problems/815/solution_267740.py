def insere(lista_numero,n):
    '''Função que, dada uma lista crescente de números inteiros e número inteiro n, inclua n na posição correta;list,int -> list'''
    listanova = lista_numero.append(n)
    return listanova.sort()