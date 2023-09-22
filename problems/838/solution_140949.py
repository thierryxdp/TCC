def num_bombons(dinheiro,preço):
    '''calcula o número de bombons possíveis de comprar vide o preço
    de um bombom e o valor total possuído; float,float -> int'''
    print('Quantos bombons dá pra comprar?')
    n = input(dinheiro//preço)
    return n