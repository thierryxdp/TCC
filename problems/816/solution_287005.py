def maiores( l , n ):
  #Para cada elemento da lista l filtra apenas os elementos maiores e iguais a n.
  return list  sorted ( filter( lambda e: e >= n , l ) )