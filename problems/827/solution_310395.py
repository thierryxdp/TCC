def qtd_divisores(n):
  '''...'''
  soma = 0
  i = 1
  while i<=n:
    if n%i == 0:
        soma = soma + 1
    i = i+1 
return soma