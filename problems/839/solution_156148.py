def carros(p,c=5):
    '''calcula e retorna o numero exato de carros necessarios para ocupar a quantidade de pessoas''''
    return p//c+1 if p<c