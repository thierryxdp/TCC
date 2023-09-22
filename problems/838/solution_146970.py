def num_bombons(preco,dinheiro):
    '''Recebe o preco do bombom e o dinheiro, e retorna a quantidade de bombons que é possivel comprar;
    float,float->int'''
    
    qtd = preco//dinheiro
    return qtd