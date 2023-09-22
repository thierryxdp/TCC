#  ira retornar se o colchao passar, caso nao passe retornara false
# m,h,l
def Colchao(m,h,l):
    """A funçao retorna True se o colchao passar pela porta caso nao passar retorna False"""
    if m[1] <= h:
        return True
    else:
        return False