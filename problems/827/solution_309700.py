def qtd_divisores(n):
    '''funcao que dado um numero, conta quantos divisores ele tem int->int'''
  x = len([i for i in range(1,n+1) if not n % i])
  return x