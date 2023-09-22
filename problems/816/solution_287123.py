def maiores(lista, n):
    """Retorna uma lista de números que contém todos os elementos do parametro 'lista'
    	que sejam maiores que o parametro 'n' em ordem crescente"""
    
    l_final = []
    
    for i in lista:
        if i > n:
            l_final.append(i)
            
    l_final.sort()
           
    return l_final