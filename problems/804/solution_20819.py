def filtra_pares(a,b,c,d):
    "Retorna os números pares em ordem da tupla."
  tupla1 = (a,b,c,d)
  tupla2 = (a)
  tupla3 = (b)
  tupla4 = (c)
  tupla5 = (a,b)
  tupla6 = (a,c)
  tupla7 = (a,d)
  tupla8 = (b,c)
  tupla9 = (b,d)
  tupla10= (c,d)
  if a%2 ==0 and b%2 ==0 and c%2 ==0 and d%2 ==0:
      return tupla1
  elif a%2 ==0 and not (b%2 == 0 and c%2 == 0 and d% 2 == 0):
      return tupla2
  elif b%2 ==0 and not (a%2 == 0 and c%2 == 0 and d% 2 == 0):
      return tupla3
  elif c%2 ==0 and not (b%2 == 0 and a%2 == 0 and d% 2 == 0):
      return tupla4
  elif a%2 ==0 and b%2 ==0 and not (c%2 == 0 and d% 2 == 0):
      return tupla5
  elif a%2 ==0 and c%2 ==0 and not (b%2 == 0 and d% 2 == 0):
      return tupla6
  elif a%2 ==0 and d%2 ==0 and not (b%2 == 0 and c% 2 == 0):
      return tupla7
  elif b%2 ==0 and c%2 ==0 and not (a%2 == 0 and d% 2 == 0):
      return tupla8
  elif b%2 ==0 and d%2 ==0 and not (a%2 == 0 and c% 2 == 0):
      return tupla9
  elif c%2 ==0 and d%2 ==0 and not (a%2 == 0 and d% b == 0):
      return tupla10#Start your python function here