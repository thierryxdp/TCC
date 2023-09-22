def colchao(medidas,H,L):
    """Calcula e retorna se um colchao e capaz de atravessar uma porta.
    list, int, int -> bool""" 
   if medidas[0]> L:
        return False
   if (medidas[1]**2 - medidas[0]**2)**0.5 > H:
        return False
   else:
        return True