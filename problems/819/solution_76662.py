def filtraMultiplos ( lista , y ) :
    """essa função irá receber uma lista de números e um número, e irá retornar outra lista contendo todos elementos da lista original que forem divisíveis pelo número ; lista -> lista"""
    multiplos= []
    c = 0
    while c < len (lista):
        if lista [c] % y == 0:
            multiplos.append(lista[c])
        c += 1
    return multiplos