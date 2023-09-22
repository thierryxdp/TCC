def colchao(medidas,H,L):
    """Função que retorna se um colchão passa por uma porta dadas suas medidas
    list, int, int -> bool"""
    if medidas[1] <= H or medidas[2] <= L:
        return True
    else:
        return False