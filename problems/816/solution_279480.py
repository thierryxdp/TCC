def maiores(lista,n):
  '''Retorna uma lista que tenha todos os números da lista anterior maior que n;
  list,int -> list'''
  
  def maior(b):
    '''Diz se um número é maior que n;
    int -> bolean'''
    if b > n:
      return True
    else:
      return False

  lista1 = list(filter(maior,lista))#Lista com números maiores que n
  return lista1