# Ira retornar True ou False caso o colchao passar ou nao pelas determinadas dimensoes 
# medidas,H,L
def colchao(medida,H,L):
    """Funçao que retorna True ou False caso o colchao consiga passar,ou nao por uma porta de dimensoes H e L dado as mesmas e a lista com dimensões do colchão medidas para H: int -> int para L: int -> int return: bool -> bool"""
    [A, B, C] = medidas
    if A and B > H and L:
        return False
    else:
        return True