def filtra_pares(tupla):
   tupla == str(tupla)
   x = tupla[0]
   y = tupla[1]
   a = tupla[2]
   b = tupla[3]
   if x %2==0 and y %2==0 and a %2==0:
        return tupla(x,y,a)
    if x %2==0 and y %2==0 and b%2==0:
        return tupla(x,y,b)
    if x %2==0 and a %2==0 and b %2==0:
        return tupla (x,a,b)
    if y %2==0 and a 2%==0 and b %2==0:
        return tupla (y,a,b)