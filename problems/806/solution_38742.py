def colisao(r1x0, r1y0, r1x1, r1y1, r2x0, r2y0, r2x1, r2y1):
    '''FunÃ§Ã£o que recebe as coordenadas de dois retÃ¢ngulos ecalcula se hÃ¡ colisÃ£o
    entre eles em um plano 2D (int, int, int, int, int, int, int, int -> bool)'''
    if r2x0 <= r1x1:
        return True
    else:
        return False