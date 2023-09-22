#  ira retornar se o colchao passar, caso nao passe retornara false
# m,h,l
def Colchao(m,h,l):
    """A funçao retorna True se o colchao passar pela porta caso nao passar retorna False"""
    m.sort()
    if m[0] > h:
        if m[0] > l:
            return False
        elif m[1] > l:
            return False
        else:
            return True
        elif m[1] > h:
            return False
        else:
            return True