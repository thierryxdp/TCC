def maiores( l , n ):
    '''Para cada elemento da lista l filtra apenas 
  os elementos maiores e iguais a n.'''
    lista = list( filter( lambda e: e >= n , l ) )
    return sorted(lista)