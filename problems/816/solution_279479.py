def maiores(lista,n):
  '''Retorna uma lista que tenha todos os números da lista anterior maior que n;
  list,int -> list'''
  def menor(a):
    '''Diz se um numero é menor que n;
    int -> bolean'''
    if a < n:
      return True
    else:
      return False

  def maior(b):
    '''Diz se um número é maior que n;
    int -> bolean'''
    if b > n:
      return True
    else:
      return False

  lista1 = list(filter(maior,lista))#Lista com números maiores que n
  lista2 = list(filter(menor,lista))#Lista com números menores que n
  lista2[::] = list(range(n,n+lista2[-1]+1))
  return lista2