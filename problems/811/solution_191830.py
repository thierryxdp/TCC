def colchao(medidas,H,L):
    '''funçao que dada uma lista de medidas com 3 dimensões de um colchão
    (da menor para a menor) e dois numeros inteiros(correspondentes a altura e largura
    retorna se o colchão consegue passar ou não pela porta
    list, int, int -> bool'''
    P=medidas[0]
    l=medidas[1]
    A=medidas[2]
    if P<=H and l<=L:
        return True
    elif P<=H and A<=L:
        return True
    elif l<=H and A<=L:
        return True
    elif A<=H and l<=L:
        return True
    elif P<=L and A<=H:
        return True
    elif P<=L and l<=H:
        return True
    else:
        return False