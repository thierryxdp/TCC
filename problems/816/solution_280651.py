def maiores( l , n ):
    '''Para cada elemento da lista l filtra apenas 
  os elementos maiores e iguais a n.'''
    if list( filter( lambda e: e >= n , l ) ):
    return list.sort(l)