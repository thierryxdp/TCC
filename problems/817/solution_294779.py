def maiores( l , n ):
  #Para cada elemento da lista l filtra apenas os elementos maiores e iguais a n.
  return list( filter( lambda e: e >= n , l ) )

def acima_da_media(lista):
    lis=len(lista)
    tam=sum(lista)
    n = tam/lis
    n1=round(n)
    if n<n1:
        a = maiores(lista,n)
        a1 = sorted(a)
        return a1

	else:
        a = maiores(lista,n)
        a = sorted(a)
        lista=a.pop(0)
        return lista