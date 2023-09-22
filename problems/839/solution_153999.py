def carros (np, cc=5):
    '''calcula e retorna o numero exato de carros necessarios para a viagem
       : int, int -> int'''
    return (np/cc)+1-(np%cc)