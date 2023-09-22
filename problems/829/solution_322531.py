def soma_h(n):
    '''Retorna o valor da soma h (indicada no texto) em que n é o denominador do último termo a ser somado
int -> float'''
    total=0
    for x in list(range(1,n+1)):
        total=total+(1/x)
    return round(total,2)