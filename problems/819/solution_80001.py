def filtraMultiplos (listanum,num):
    """retorna uma lista contendo todos os elementos da lista
    original que forem divisíveis por n"""
    n = 0
    listafinal = []
    while listanum[n]%num == 0:
   		listafinal += [ listanum[n] ]
      	n = n+1
        
    return listafinal