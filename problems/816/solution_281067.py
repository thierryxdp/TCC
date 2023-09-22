def maiores( l , n ):
  lista = list( filter( lambda e: e >= n , l ) )
  lista.sort()
  return list( filter( lambda e: e >= n , l ) )