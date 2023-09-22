import math

def limite():
  '''void -> (float, int)'''
  condition = True
  contador = 0

  while condition:
    calculo = (-1 ** contador) / (2 * contador + 1)
    contador = contador + 1
    parada = math.fabs(calculo) < 0.01
    if parada:
      condition = False
      return (math.fabs(calculo), contador)

print(limite())

def F(c1,c2):
    c3 = []
    for i in c1:
        if i in c2:
            list.append(c3,1)
    return c3