def insere(x, n):
    '''a funçao recebe uma lista ordenada de numeros inteiros e o numero inteiro n e inclui n na posiçao correta
    assinatura: list[int], int -> list[int]
    casos de teste:
    insere([7, 17], 13) == [7, 13, 17]
    insere([23, 34], 12) == [12, 23, 34]
    '''
    list.insert(x,1,n)
    list.sort(x)
    
    return x