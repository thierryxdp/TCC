def qtd_divisores(numero):
  '''Essa função retorna a quantidade de dividoires que um numero possui,
  int->int'''
  divisores=(1,2,3,4,5,6,7,8,9,numero)
  soma=0
  for x in divisores:
     if numero%x==0:
       soma+=1
  return soma