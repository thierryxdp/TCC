def fatorial (num: int)-> int:
   '''Retorna o fatorial de um número'''
   i = 1
   resultado = 1

   while i <= num:
      resultado = resultado * i
      i += 1

   return resultado