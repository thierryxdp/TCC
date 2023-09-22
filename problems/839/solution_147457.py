def carros(x,y=5):
    '''calcula e retorna o numero de carros de y assentos utilizados por x pessoas'''
    return (x//y)+((x%y)*(y%x))