def num_bombons(total,preco):
    '''retorna quantos bombons são possíveis comprar a partir do preço de
    1 bombom e o valor total possuído; float,float -> int'''
    n = (total//preço)
    return n