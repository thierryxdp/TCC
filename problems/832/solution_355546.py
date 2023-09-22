def eh_quadrada(M):
    if len(M)==1 and len(M[0])==0:
        return True
    elif len(M)!=len(M[0]):
        return False
    else:
        return True