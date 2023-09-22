def intercala(lista1,lista2):
   lista3 = lista1 +  lista2
   lista3[0] = lista1[0]
   lista3[1] = lista2[0]
   lista3[2] = lista1[1]
   lista3[3] = lista2[1]
   lista3[4] = lista1[2]
   lista3[5] = lista2[2]
   return lista3