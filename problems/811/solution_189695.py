def colchao (dimensoes, H,L):
    '''
    função que recebe uma lista com as dimensões do menor para o maior do colchão e dois inteirios com a dimensão da porta, caso o colchão nao passe pela
    porta, função retorna False, caso passe, retorna True
    list, int, int --> bool
    '''
    if (dimensoes[1]>=H) and (dimensoes[2]<=L):
        return True
    elif (dimensoes[1]<=H) and (dimensoes[2]<=L):
        return True
    elif (dimensoes[1]<=H) and (dimensoes[2]>=L):
        return True
    else:
        return False