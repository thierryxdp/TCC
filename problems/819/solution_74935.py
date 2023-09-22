def filtraMultiplos(lista,n):
    """Função que recebe como entrada uma lista de números e um número 
    qualquer "n" e retorna outra lista contendo todos os elementos da 
    lista original que forem divisíveis por "n"."""
    """list,int-->list"""
    i=0
    multiplos=[]
    while i<len(lista):
        if lista[i]%n==0:
            multiplos=multiplos+[lista[i]]
        i=i+1
    return multiplos