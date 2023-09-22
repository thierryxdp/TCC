def num_bombons (dinheiro,preco):
    ''calcula quantos bombons se pode comprar,
    dados o dinheiro e preco de bombom
    float,float -> int,float'''
    return int(dinheiro/preco),float(dinheiro%preco)