def colchao(A, B, C, H, L):
    if (A <= H and B <= L) or (A <= H and C <= L) 
    or (B <= H and A <= L) or (B <= H and C <= L) 
    or (C <= H and A <= L) or (C <= H and B <= L):
        return True
    else:
        return False