def maiores( l , n ):
  #Para cada elemento da lista l filtra apenas os elementos maiores e iguais a n.
  lista = list( filter( lambda e: e >= n , l ) )
  lista.sort()
  return  lista

def acima_da_media(lista):
  '''
  list --- > list
  '''
  media = sum(lista)/len(lista)
  return maiores(lista,media)