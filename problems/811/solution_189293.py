def colchao(medidas,H,L):
    """Função que recebe na ordem dimensões das medidas AxBxC e altura H e largura L e retorna se os valores de medidas satisfazem a altura e largura;
    list, int, int -> bool"""
    if medidas[1]<=H and medidas[2]<=L:
        return True
    else:
        return False