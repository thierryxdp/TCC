def num_bombons(dinheiro, preco):
    
    """ Recebe o dinheiro que Pedrinho tera e o preco de
    cada Bombom. Devolve quantas unidades de bombons ele
    consegue comprar em numero inteiro"""
    
    q = dinheiro/ preco
    
    resto = dinheiro % preco
    
    if resto < (preco/2):
        return round(q)
    elif resto >= (preco/2):
        return round(q) - 1