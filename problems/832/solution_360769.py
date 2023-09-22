def eh_quadrada(matriz):
   quant_ele=[]
   acumu=0
   u=0
   for i in matriz:
      list.append(quant_ele,len(i))
      u=u+1
   for j in range(len(matriz)):
      print(j)
      print(len(i))
      print(quant_ele)
      if quant_ele[0]!=quant_ele[j]:
         acumu=acumu+1
         print(acumu)
   if acumu==0:
      return True
   else:
      return False