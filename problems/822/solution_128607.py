def repetidos(nums):
    '''Dada um lista com números retorna o números de vezes que aparece
    um número igual ao seu anterior
    list - int'''
    lista = []
    c = -1

    while c > -len(nums):
        if nums[c] == nums[c -1]:
            lista.append(nums[c])
        c -= 1
    return len(lista)