def num_bombons (dinheiro,preco_de_bombom):
    '''Dado os parâmetros dinheiro e preco_de_bombom, a função
    irá retornar a quantidade máxima de bombon que é possível
    comprar com a quantidade de dinheiro dado;
    float, float -> int'''
    
    numero_de_bombons = (dinheiro/preco_de_bombom)
    return numero_de_bombons