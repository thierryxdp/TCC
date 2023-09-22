def colchao(dimensoes,H,L):
    """Essa funcao recebe as dimensoes de um colchao em formato de lista e a altura e largura de uma porta, ela 
    retorna True caso o colchao possa passar pela porta e False caso contrario;
    lista, int, int -> Bool"""
    [A,B,C] = dimensoes
    if B > H:
        return False
    elif A > L:
        return False
    else:
        return True