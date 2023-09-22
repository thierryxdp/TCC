def colchao_passa(dimensoes_colchao, H, L):
    """"Recebe as dimensoes de um colchão, ordenadas do menor para a maior,
    e descobre se ele passsa por uma porta com H de altura e L de largura;
    list, int, int -> bool"""

    dimensoes_porta = [H, L]
    if dimensoes_colchao[0] <= min(dimensoes_porta) and dimensoes_colchao[1] <= max(dimensoes_porta):
        return True
    else:
        return False