def carros(p,capacidade=5):
    '''Calcula a quantidade de carros para uma viagem,
    dados a quantidade de pessoas p e a capacidade dos carros.
    se nenhum valor for inserido para capacidade, será considerado
    que o valor será 5'''
    return ceil(p//capacidade +1)