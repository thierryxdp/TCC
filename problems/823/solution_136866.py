def faltante (pecas: list[int]) -> int:
   '''Retorna a peça/numero que falta na lista de peças'''

   lista = pecas.copy()
   lista.sort()

   i = 0
   
##   if lista[-1]%2 == 0:
##      modelo = range(1,lista[-1])
##   else:
##      modelo = range(1,(lista[-1]+1))
   while i < len(lista):
      if lista[i] != (i+1):
         return i + 1
      i+=1
   return i + 1