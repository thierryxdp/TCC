def maiores(ni,n):
    """A função recebe um lista de números inteiros e um
    número inteiro n, retorna outra lista, que contenha
    todos os números maiores que n na lista original
    Entrada: Int
    Saída: Int"""
    
    ni1 = list(ni)
    ni_ordem = list.sort(ni1)
    
    
    return ni_ordem