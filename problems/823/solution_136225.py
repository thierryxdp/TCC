def faltante(lista):
   
    n=max(lista)
    contador=1
        
    while 0>n<len(lista):
          if n in lista:
            n=n+contador
    return n