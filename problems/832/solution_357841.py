def eh_quadrada(M):
    if len(M)==len(M[0]):
        return True
    elif M[1][1]==0:
        return True
    else:
        return False