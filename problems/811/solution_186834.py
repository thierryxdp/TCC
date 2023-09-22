def colchao(medidas, H, L):
    """"Recebe as dimensoes de um colchão, ordenadas do menor para a maior,
    e descobre se ele passsa por uma porta com H de altura e L de largura;
    list, int, int -> bool"""

    dimensoes_porta = [H, L]
    if medidas[0] <= min(dimensoes_porta) and medidas[1] <= max(dimensoes_porta):
        return True
    else:
        return False