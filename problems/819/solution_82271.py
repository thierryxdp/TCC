def filtraMultiplos (listan: list, n: int)-> list:
    '''retorna uma nova lista contendo apenas os elementos da lista original
    que forem múltiplos de n'''
    i = 0
    lista = []
    while i < len(listan):
        if listan[i] % n == 0:
            lista.append(listan[i])
        i += 1
    return lista