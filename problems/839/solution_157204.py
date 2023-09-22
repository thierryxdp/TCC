import math
def carros (pessoas , veiculos = 5) :
    ''' essa função calcula o minimo do numero de veiculos que um
    determinado grupo de pessoas precisa para poder viajar. fornecendo
    o numero de pessoas e a quantidade de lugares do veiculo, todos
    do mesmo modelo'''
    return math.ceil (pessoas/veiculos)