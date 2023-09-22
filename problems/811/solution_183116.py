def colchao(medidas,H,L):
    """Função que verifica se um colchão de medidas 'medidas' pode passar por uma 
    porta de altura 'H' e largura 'L'
    list, int, int -> bool"""
    list.sort(medidas)
    menor,media,maior = medidas
    if maior <= H or maior <= L:
        return True
    else:
        return False