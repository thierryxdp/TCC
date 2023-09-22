def filtraMultiplos (lista,n):
    """função que dado uma lista contendo apenas números inteiros(lista) e um número (n),
    ela calcula e retorna todos os números da lista que forem divisíveis'divisão exata' por n
    entrada -> list,int
    retorna-> list"""
    
    TMlista= len (lista)
    indice=0
    multiplos=[]
    
    while indice <TMlista:
        if lista [indice]%n ==0:
            multiplos= multiplos+ [lista [indice]]
        indice= indice+1
        
    return multiplos