def eh_quadrada(M):
    if len(M)==len(M[0]):
        return True
    if len(M)==1 and len(M[1])==0:
        return True
    else:
        return False