def maiores(lista_numero,n):
   lista_numero.append(n)
   list.sort(lista_numero)
   maiores = lista_numero[n+1:]
   return maiores