def maiores(lista,n):
 list.sort(lista)
 lista = [e for e in lista if e <= n]
 return lista