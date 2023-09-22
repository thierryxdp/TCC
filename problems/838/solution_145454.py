def num_bombons (dinheiro,preco):
    '''
    Função que retorna a quntidade de bombons que Pedrinho pode 
    comprar dado seu dinheiro e o valor do bombom, respectivamente
    int,float--->int
    '''
    return math.ceil(dinheiro/preco)