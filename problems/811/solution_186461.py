def colchao(medidas, H, L):
    '''Função que dada as medidas de um colchão, em uma lista, da menor para a maior, e a altura
    e largura da porta, retorna se o colchão passaria por ela ou não (todas medidas inteiras)
    list, int, int -> bool'''
    
    if H > L:
    	menor = L
        maior = H
    else:
        menor = H
        maior = L
    if (medidas[0] <= menor) and (medidas[1] <= maior):
        return True
    else:
        return False