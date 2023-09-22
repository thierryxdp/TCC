def maiores( l , n ):
  '''
  list, int ---> list
  '''
  #Para cada elemento da lista l filtra apenas os elementos maiores e iguais a n.
 lista = list( filter( lambda e: e >= n , l ) )
 lista.sort()
 return lista