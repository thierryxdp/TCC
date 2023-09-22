def soma_h(N):
    """dado um valor"""
    H=0
    for numero in range(N):
        H=H+(1/(numero+1))
        H=round(H,2)
    return H