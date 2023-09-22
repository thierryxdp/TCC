def filtra_pares(t):
    """ retorna uma nova tupla com valore pares de entrada da tupla original na ordem que se encontram
    tuple->tuple"""
    if t == ():
      return 0
   else:
      return t[0] + conta_pares(t[1:])