def eh_quadrada(M):
    lin = len (M)
    if lin == 0:
            resp = True
    if lin != 0 and lin == len(M[0]):
            resp =  True
    else:
        resp = False
    return resp