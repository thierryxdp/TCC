def insere(x, n):
    """a funçao recebe uma lista ordenada de numeros inteiros e o numero inteiro n e inclui n na posiçao correta
    assinatura: list[int], int -> list[int]"""
    list.insert(x,1,n)
    list.sort(x)
    
    return x