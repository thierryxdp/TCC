def filtra_pares(numeros):
    '''receba uma tupla com quatro elementos inteiros, e retorne uma nova tupla contendo apenas os elementos pares da tupla original'''
    '''int->int'''
    tupla = ()
    for n in numeros:
        if n % 2 ==0:
            appen(n)
            return (tupla)