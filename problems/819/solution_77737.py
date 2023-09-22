def filtraMultiplos(lista, n):
    """Função que recebe uma lista e retorna a mesma porem so os numeros divisiveis por n
     list, int-> list"""
    i = 0
    novalista = []
    while i <= len(lista)-1:
        if lista[i] % n == 0:
            novalista.append(lista[i])
            
            i += 1 
            return novalista