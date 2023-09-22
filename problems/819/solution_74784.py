def filtraMultiplos(l, n):
    '''
    Esta função recebe uma lista contedo números, um número qualquer e retorna uma outra lista
    que contém todos os números da lista original que são divisíveis pelo número fornecido.
    
    Parametros
    ----------
    l (list) : lista
    n (int) : número
    '''
    l0 = []
    i = 0
    while i < len(l):
        if l[i]%n == 0:
            l0.append(l[i])
        i += 1
    return l0