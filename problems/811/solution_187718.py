def colchao(medidas, H, L):
    A, B, C = medidas
    if H>=A and L>=B or H>=B and L>=A or H>=C and L>=B or H>=B and L>=C or H>=A and L>=C or H>=C and L>=A:
        return True
    else:
        return False