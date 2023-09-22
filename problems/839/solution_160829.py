def carros(npes,capvei=5):
    '''função que calcula o número de carros necessários para uma viagem,
    inserindo respectivamente o número de pessoas que vão viajar e a 
    capacidade de pessoas transportadas pelo veículo se esta for maior
    que 5
    int,int->int'''
    if npes%capvei!=0:
        return npes//capvei+1
    else:
        return npes//capvei