def carros (pessoas):
    '''retorna o numero de carros para uma viagem, dado o numero de pessoas'''
    if pessoas > 0 and pessoas <= 5:
        return 1
    else:
        return (pessoas//5)+1