def soma_h(n):
   '''Retorna a soma de 1 + 1/2 + ... 1/n
      int -> float'''
   h = 1
   for ele in range (2, n+1):
      h += 1/ele

   return round(h,2)