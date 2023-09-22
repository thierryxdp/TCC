def maiores(lista_numero,n):
    '''dada uma lista ordenada (crescente) de números inteiros e um número inteiro n,
    inclua n na posição correta.
    list,int -> list'''
    # ex. maiores([1,2,4,5],3)=>[4,5]
    #insere(lista_numero,n)
    lista_numero.append(n)
    lista_numero.sort()
    pos=lista_numero.index(n)
    return lista_numero[pos+1:]