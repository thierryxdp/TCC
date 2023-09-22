def filtra_pares(elementos):
  #Função que recebe 4 elementos inteiros e retorna apenas os elementos pares da tupla original, na mesma ordem em que se encontravam
  tupla = ()
  
  if (elementos[0] % 2 > 0) == False:
    #Se e1 for par
    tupla = (elementos[0],)
  if (elementos[1] % 2 > 0) == False:
    #Se e2 for par
    tupla += (elementos[1],)
  if (elementos[2] % 2 > 0) == False:
    #Se e3 for par
    tupla += (elementos[2],)
  if (elementos[3] % 2 > 0) == False:
    #Se e4 for par
    tupla += (elementos[3],)
  return tupla