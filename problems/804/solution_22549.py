def filtra_pares(a1,a2,a3,a4):
  #Função que recebe 4 elementos inteiros e retorna apenas os elementos pares da tupla original, na mesma ordem em que se encontravam
  elementos = (a1,a2,a3,a4)
  tupla = ()
  
  if (elementos[0] % 2 > 0) == False:
    #Se a1 for par
    tupla = (a1,)
  if (elementos[1] % 2 > 0) == False:
    #Se a2 for par
    tupla += (a2,)
  if (elementos[2] % 2 > 0) == False:
    #Se a3 for par
    tupla += (a3,)
  if (elementos[3] % 2 > 0) == False:
    #Se a4 for par
    tupla += (a4,)
  return tupla