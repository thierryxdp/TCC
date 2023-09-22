def filtraMultiplos(lista,n):
    """Função que recebe como entrada uma lista de números e um número, e retorna outra lista contendo todos os elementos da lista original que forem divisíveis por n; lista,int->lista"""
    
    indice = 0
    multiplos = []
    
    while indice < len(lista):
        
        if lista[indice]%n == 0:
            multiplos = multiplos+lista[indice]
        
        indice = indice+1
        
    return multiplos