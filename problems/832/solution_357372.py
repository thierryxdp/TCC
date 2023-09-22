def eh_quadrada(M):
    if M==[]:
        return True
    
    l=len(M)
    c=len(M[0])
    if l==c:
        return True
    else:
        return False