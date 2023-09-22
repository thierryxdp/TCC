def falante(lista):
    n=0
    contador=0
        
        while n<len(lista):
            if n not in lista:
                return n 
            contador=contador+1
        return lista