def faltante(lista):
   
    n=0
    contador=1
        
    while n<len(lista):
        if n not in lista:
            return n
        if n in lista:
            n=n+contador
    return n