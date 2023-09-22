def primo (num):
   '''Retorna se um número é primo
      int -> bool'''
   #Verifica se o número de divsores do número é <= 2 usando função anterior
   nDivs = 0
   for div in range(1,num+1):
      if num%div == 0:
         nDivs += 1
         if nDivs > 2:
            return False

   return True