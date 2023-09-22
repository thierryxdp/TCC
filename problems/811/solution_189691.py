def colchao (dimenses, H,L):
    '''
    função que recebe uma lista com as dimensões do menor para o maior do colchão e dois inteirios com a dimensão da porta, caso o colchão nao passe pela
    porta, função retorna False, caso passe, retorna True
    list, int, int --> bool
    '''
    if (dimensões[1]>H) and (dimensões[2]<L):
        return True
    elif (dimensões[1]<H) and (dimensões[2]<L):
        return True
    elif (dimensões[1]<H) and (dimensões[2]>L):
        return True
    else:
        return False