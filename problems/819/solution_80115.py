def filtraMultiplos (lista,numero):
    ''' Entrada: lista -> lista de números, 
    			 parâmetro do tipo string
                 numero -> número, parâmetro do tipo float
        
         Saída: A função retorna uma outra lista contendo todos
         		os elementos da lista original que forem divisíveis
                por n
                
         list,float -> str'''
    divisiveis =[]
    proximo = 0
    while proximo <len(lista):
        if lista[proximo]%n == 0:
            divisiveis = divisiveis + (lista[proximo],)
        proximo = proximo + 1 
    return divisiveis