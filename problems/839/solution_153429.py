def carros(x,y=5):
    '''calcula o numero de veiculos de capacidade y necessrios para uma viagem de x passageiros'''
    return round(x/y+0.5)