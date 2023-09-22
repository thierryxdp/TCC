def carros(capacidade=5 , pessoas):
    '''calcula o numero de carros para levar determinada quantidade de pessoas.'''
   
    return math.ceil(pessoas / capacidade)