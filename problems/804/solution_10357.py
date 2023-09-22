def filtra_pares(x):
    '''calcula e retorna apenas os numeros pares do conjunto; tupla -. tupla'''
    def par(x):
        '''calcula se a função é par ou n'''
        return x/2==int(x/2)
    x(filter(par,x))
    return str(x)