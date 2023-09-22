def carros (pessoas, capac=5):
    ''' determina a quantidade de carros que é preciso para viajar com
        x pessoas, int, int, --> int '''
    if pessoas%capac <= 5:
        return pessoas//capac + 1
    else:
        return pessoas//capac