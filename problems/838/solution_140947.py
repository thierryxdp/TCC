def num_bombons(preço,dinheiro):
    '''calcula o número de bombons possíveis de comprar vide o preço
    de um bombom e o valor total possuído; float,float -> int'''
    bombons = dinheiro//preço
    return bombons