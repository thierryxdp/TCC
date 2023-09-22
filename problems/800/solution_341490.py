def total (compras, mercado):
    '''dado um número inteiro positivo N retorna
    o valor o valor de H com N termos.'''
    valor = 0
    for i in compras:
        if i in mercado:
            valor = valor + mercado[i]
    return round(valor,2)