def filtraMultiplos(numeros,n):
    
multiplos = numeros[c]
 for c in numeros:
    if c % n == 0:
        multiplos.append(c)
        multiplos.sort()
         return multiplos