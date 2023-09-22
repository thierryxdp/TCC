def num_bombons(total,custo):
    '''retorna o número de bombons possíveis de comprar dado um valor custo 
    de 1 bombom e o total possuído; float, float -> int'''
    n = (total//custo)
    return n