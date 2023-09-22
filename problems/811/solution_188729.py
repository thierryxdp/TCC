def colchao (medidas: list, H: int, L: int)-> bool:
    '''dada uma lista com as medidas do colchão e dois números inteiros
    correspondetes a altura da porta H e a largura da porta L, a função 
    retorna True se o colchão passa pela porta e False caso contrário'''
    compc= medidas[1]
    if compc> H:
        return False
    elif compc<= H:
        return True