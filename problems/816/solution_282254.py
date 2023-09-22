def maiores( l , n ):
    'Funçao que retorna os numeros maiores que n em ordem crescente'
    list( filter( lambda e: e >= n , l ) )
    return sorted(maiores)