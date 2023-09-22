def filtraMultiplos(lista, n):
    '''retorna uma lista contendo todos os elementos da lista original
    que são divisíveis por 'n'.
    lista, int -> lista'''
    
    lista.sort
    divisiveis = []
  
    for i in range(len(lista)):
        if lista[i]%n == 0:
            divisiveis.append(lista[i])
            
    lista = divisiveis
    return lista