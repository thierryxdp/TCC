def maiores(numeros,n):
   """essa função serve para indicar os números maiores que n
   list,int->list"""
   list.append(numeros, n)
   list.sort(numeros)
   return numeros[numeros.index(n)+numeros.count(n):]

   #casos de teste
   #maiores([1,2,3,4,5],3) == [4, 5]
   #maiores([6,7,8,9,10],3) == [6, 7, 8, 9, 10]
   #maiores([11,12,13,14,15],14) == [15]