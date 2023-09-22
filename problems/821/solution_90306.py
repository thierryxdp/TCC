def fatorial(n):
    '''Faça uma função chamada fatorial que dado um número, calcule o fatorial deste número. (Não usar a função factorial do módulo math)
    int->int'''
    
    fatoria=0
    i=0
    multi=1
    while i<n:
        fatoria=n-i
        i+=1
        multi=multi*fatoria
    return multi