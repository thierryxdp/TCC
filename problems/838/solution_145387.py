def num_bombons(dinheiro, preco):
    '''função que calcula a quantidade maxima de bombons que Pedrinho pode comprar
    	tendo como entrada o dinheiro que ele tem (dinheiro) e o preço de cada bombom
        (preco)
        float, float -> int'''
    if preco<=dinheiro:
        return dinheiro//preco
    else:
        if preco>dinheiro:
            return 0.0
        
    
#Escreva sua função aqui. Pode apagar essa linha.