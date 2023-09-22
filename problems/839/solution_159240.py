def carros (npessoas,cveiculos=5):
    '''calcula o número exato de carros para viagem, tendo como entrada o numero de pessoas e eventualmente a capacidade do veículo; int,int->float'''
    return math.ceil(npessoas/cveiculos)