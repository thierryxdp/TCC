def qtd_divisores(numero):
  '''Essa função retorna a quantidade de dividoires que um numero possui,
  int->int'''
  divisores=list(range(1,numero+1))
  soma=0
  for x in divisores:
     if numero%x==0:
       soma+=1
  return soma