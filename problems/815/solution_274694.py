def insere(lista_numero,n):
    '''
    Funçao que dada uma lista ordenada-crescente de numeros interiros
    e um numero inteiro n, inclua n na posiçao correta
    list-> list
    '''
    list.append(lista_numero, n)
    ordem= list.sort(lista_numero)
    return ordem