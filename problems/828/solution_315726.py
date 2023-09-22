def qnt_divisores(num):
   '''Retorna quantos divisores num tem
      int -> int'''
   
   nDivs = 0
   for div in range(1,num+1):
      if num%div == 0:
         nDivs += 1

   return nDivs

#Exercício 3
def primo (num):
   '''Retorna se um número é primo
      int -> bool'''
   #Verifica se o número de divsores do número é <= 2 usando função anterior
   if qnt_divisores(num) <= 2 and num != 0:
      return True
   else:
      return False