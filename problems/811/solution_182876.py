def colchao(medidas, H, L):
    menor = medidas[0] # A
    medio = medidas[1] # B
    maior = medidas[2] # C
    if menor <= H:
        if medio <= L:
            return True
        if medio > H:
            pass
    if medio <= H and menor <= L:
        return True