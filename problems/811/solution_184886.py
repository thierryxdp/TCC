def colchao(medidas:list,H,L):
    '''função que dados as dimensões do colchão no formato 
    de uma lista e as medidas da porta, altura e largura como 
    interios analise se o colchão passa pela porta e retorn True 
    caso passe pela porta ou False caso não passe.
    list.int,int->bool'''
    if medidas[0]<=L and medidas[1]<=H:
        return True
    elif medidas[0]<=H and medidas[1]<=L:
        return True
    else:
        return False