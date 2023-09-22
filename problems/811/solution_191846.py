def colchao (medidas,H,L):
    '''essa funçao diz se um colchao de medidas A,B, e C consegue passar por uma porta de medidas H
    e L
    list, int, int -> bool '''
    if medidas<= H:
        return True
    else:
        return False
    if medidas <= L:
        return True
    else:
        return False