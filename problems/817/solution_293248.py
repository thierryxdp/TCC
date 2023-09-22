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
  list.sort(lista1)
  return lista1  

def acima_da_media (notas):
  '''Retorna uma lista com as notas que ficaram acima da média em uma turma;
  list -> list'''
  def media (lista):
    '''Calcula a média da lista;
    list -> int'''
    return sum(lista)//len(lista)
  media = media(lista)

  return maiores(notas,media)