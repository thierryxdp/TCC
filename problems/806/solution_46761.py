def colisao(tup,tup1):
    """ A função retorna se há colisão entre dois retângulos em R^2;
    tup, tuo -> bool """
    if tup[2] < tup1[0] or tup1[2] < tup[0] or tup[3] < tup1[1] or tup1[3] < tup[1]:
        return False
    else:
        return True