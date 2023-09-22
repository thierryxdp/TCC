def num_bombons(dinheiro, preco):
    
    """ Recebe o dinheiro que Pedrinho tera e o preco de
    cada Bombom. Devolve quantas unidades de bombons ele
    consegue comprar em numero inteiro"""
    
    q = dinheiro/ preco
    
    return round(q)