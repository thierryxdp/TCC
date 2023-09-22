def filtraMultiplos(lista,n):
    numero = ()
    
    if lista[0]%n == 0:
        numero += (lista[0],)
    if lista[1]%n == 0 :
        numero += (lista[1],)
    if lista[2]%n == 0:
        numero += (lista[2],)
    if lista[3]%n == 0:
        numero += (lista[3],)
                  
    return lista