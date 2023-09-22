def colchao([A,B,C],H,L):
    ''' Função que toma as variáveis de medidas de um colchao, A, B e C e
    e as de uma porta, H e L, e determinem se o colchao pode passar pela porta
    list,int,int => str'''
    x = min(A,B,C)
    y = max(H,L)
    if x>y:
        return false
    else:
        return true