def carros (pessoas,lugares = 5) :
    ''' Essa função calcula o número de veículos que um determinado grupo
    de pessoas utilizaria para viajar, dando o número de pessoas e 
    o número de lugares de um mesmo modelo de veiuculo'''
    return math.ceil (pessoas//lugares)