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



def acima_da_media(notas):
   """essa função serve para indicar os números maiores que a media da lista
   list->list"""
   media = sum(notas)/len(notas)
   media = int(media)
   return maiores(notas,media)

   #casos de teste
   #acima_da_media([1,2,3,4,5]) == [4, 5]
   #acima_da_media([10,30,50,90,8]) == [50, 90]
   #acima_da_media([12,13,41,15,14,46,47,66,97]) == [41, 46, 47, 66, 97]