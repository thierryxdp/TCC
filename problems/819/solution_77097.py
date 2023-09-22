def filtraMultiplos (list,n):
    
    """Função que filtra os múltiplos de um némro n.
    A função recebe como entrada uma lista de números e um número e retorna outra lista contendo os elementos da lista original que forem divisíveis por n."""
    
    multiplos=[]
    proximo=0
    while proximo<len(list):
    if list[proximo]%n==0:
            multiplos=multiplos=(list[proximo],)
            proximo=proximo+1
    return multiplos