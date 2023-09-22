def filtra_pares(t):
   '''filtra_pares : tuplo -> inteiro
   recebe tuplo de inteiros e devolve o numero de elementos pares no tuplo'''
   if t == ():
      return 0
   else:
      #t = (t[1:])
      #if a % 2 == 0:
      return t[0] + filtra_pares(t[1:])