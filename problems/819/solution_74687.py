def filtraMultiplos(lista,n):
    """Funçao que calcula os multiplos de uma detrminada lista de um valor n de entrada de retornar os numeros que sao multiplos desse valor
    list, int -> list"""
    lista1 = []
    proximo = 0
    while proximo <len(lista):
        if lista[proximo]%n == 0:
            list.append(lista1,lista[proximo])
           
        proximo = proximo + 1    	
            
            
  
            
    return lista1