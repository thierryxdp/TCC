def filtra_pares(x):
    '''calcula e filtra os pares de uma função; tupla -> tupla'''
    def par1(x):
        '''calcula e retorna o segundo numero da tupla caso seja par; tupla -> float'''
        if x[1]%2==0:
            return x[1],
        else:
            return 
    def par2(x):
        '''calcula e retorna o terceiro numero da tupla caso seja par; tupla -> float'''
        if x[2]%2==0:
            return x[2],
        else:
            return 
    def par3(x):
        '''calcula e retorna o quarto numero da tupla caso seja par; tupla -> float'''
        if x[3]%2==0:
            return x[3],
        else:
            return 
    if x[0]%2==0:
        return (x[0],par1(x),par2(x),par3(x))
    else:
        return (par1(x)par2(x)par3(x))