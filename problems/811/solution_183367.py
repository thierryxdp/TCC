def colchao(medidas, H, L):
    tamanho_porta = [H, L]

    if medidas[0] <= tamanho_porta[0] and medidas[1] <= tamanho_porta[1]:
        return True
    else:
        return False