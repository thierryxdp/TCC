def maiores(Lista, n):
  lista = [0, 1, 2, 3]
  n = 1
  lista_final = []
  for elemento in lista:
    if elemento > n:
      lista_final.append(elemento)
      return[i for i in lista if i > n]