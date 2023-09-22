def carros(pessoas,lugares=5):
    """calcula e retorna a quantidade de carros necessários para uma determinada quantidade de pessoas"""
    resto=(pessoas%lugares)
    lugares - resto= sobra
    
    return (pessoas//lugares)+1