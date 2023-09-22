def filtraMultiplos(lista,n):
    """funcao que dada uma lista de numeros inteiros e um 
    numero n de entrada, retorna outra lista contendo todos 
    os elementos da lista original que forem divisiveis por n;
    list, int -> list"""
    
    multiplos = []
    numero = 0
    while numero <len(lista):
        if lista[numero]%n == 0:
            multiplos =  multiplos + lista[numero]
        numero = numero + 1
    return multiplos