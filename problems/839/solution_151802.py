from math import ceil
def carros(pessoas,capacidade=5):
    '''calcula e retorna o numero necessario de carros
    para transportar um grupo de pessoas dado o numero total
    de pessoas que compoem o grupo e a capacidade do veiculo
    utilizado
    int, int -> int'''
    return ceil(pessoas/capacidade)