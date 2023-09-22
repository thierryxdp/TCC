def colchao(m, H, L):
    if (m[0] <= H) and (m[1] <= L ):
        return True
    elif (m[0] <= L) and (m[1] <= H):
        return True
    elif (m[0] <= H) and (m[2] <= L):
        return True
    elif (m[0] <= L) and (m[2] <= H):
        return True
    elif (m[1] <= H) and (m[2] <= L):
        return True
    elif (m[1] <= L) and (m[2] <= H):
        return True
    else:
        return False