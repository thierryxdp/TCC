def maiores( l , n ):
    'Funçao que retorna os numeros maiores que n em ordem crescente'
    return list( filter( lambda e: e >= n , l ) )