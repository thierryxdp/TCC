def carros(p,c=5):
    '''retorna o número de carros nessessários para a viagem
    de um grupo de pessoas(p), todos os carros tem a mesma
    capacidade(c), se não informada, opadrão é 5 pessoas'''
    return round(p/c)